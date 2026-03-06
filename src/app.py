import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class DocumentManager:
    """Gerencia o carregamento e a indexação."""
    def __init__(self, folder_path, db_path="./chroma_db"):
        self.folder_path = folder_path
        self.db_path = db_path
        self.embeddings = OllamaEmbeddings(model="mxbai-embed-large")
        # Chunk size de 600 para evitar estouro de contexto
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)

    def create_vectorstore(self):
        # Tentar carregar banco existente (Performance)
        if os.path.exists(self.db_path):
            print(f"--- Carregando banco de dados existente de {self.db_path} ---")
            return Chroma(
                persist_directory=self.db_path, 
                embedding_function=self.embeddings
            )

        # Validação de caminho
        if not os.path.exists(self.folder_path):
            raise FileNotFoundError(f"Erro: A pasta {self.folder_path} não existe.")
            
        # Carregamento dos PDFs
        print(f"--- Iniciando leitura dos PDFs em: {self.folder_path} ---")
        loader = DirectoryLoader(
            self.folder_path, 
            glob="**/*.pdf", 
            loader_cls=PyPDFLoader, 
            recursive=True, 
            silent_errors=True
        )
        
        docs = loader.load()
        
        if not docs:
            print("Aviso: Nenhum conteúdo extraído. Verifique se os PDFs estão protegidos.")
            return None

        # Log profissional com contagem única de arquivos
        sources = {d.metadata.get('source', 'desconhecido') for d in docs}
        print(f"--- Sucesso: {len(docs)} páginas de {len(sources)} arquivos detectados ---")

        # 4. Processamento e Persistência
        splits = self.text_splitter.split_documents(docs)
        print(f"--- Criando {len(splits)} chunks e salvando no ChromaDB... ---")
        
        vectorstore = Chroma.from_documents(
            documents=splits, 
            embedding=self.embeddings,
            persist_directory=self.db_path
        )
        
        print("--- Banco de dados criado e salvo com sucesso! ---")
        return vectorstore

class AIAssistant:
    """Especialista Construído com a moderna LCEL (LangChain Expression Language)."""
    def __init__(self, vectorstore):
        self.llm = ChatOllama(model="llama3", temperature=0.3, num_ctx=8192)
        self.retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
        
        # Definindo o Template de Prompt (Best Practice: Storytelling e Contexto)
        template = """
        Você é um Analista Financeiro da Petrobras. 
        Use estritamente o contexto abaixo para responder. 
        Se o contexto não tiver os números exatos (como produção ou lucro), 
        diga explicitamente: 'O trecho consultado não contém o valor exato'.

        Contexto: {context}
        Pergunta: {question}
        
        Resposta Técnica em Português:"""
        
        self.prompt = ChatPromptTemplate.from_template(template)
        
        # A 'Chain' moderna (LCEL)
        self.chain = (
            {"context": self.retriever, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

    def ask(self, question):
        return self.chain.invoke(question)

# --- Orquestração ---
if __name__ == "__main__":
    try:
        manager = DocumentManager("./data/relatorios_petrobras")
        vector_db = manager.create_vectorstore()
        
        bot = AIAssistant(vector_db)
        
        pergunta = "Com base nos Destaques Operacionais do 3T25, analise como o recorde de produção no Pré-Sal (3,88 MMboed) e o Fator de Utilização das Refinarias (94%) posicionam a Petrobras frente à estratégia de descarbonização e novos produtos como o SAF. O aumento da eficiência operacional está financiando a transição energética?"
        print(f"\nSua Pergunta: {pergunta}")
        
        resposta = bot.ask(pergunta)
        print(f"\nResposta do Analista IA:\n{resposta}")
        
    except Exception as e:
        print(f"\nErro no sistema: {e}")
try:
    from langchain_ollama import OllamaEmbeddings
    from langchain_chroma import Chroma
    print("As bibliotecas foram carregadas corretamente.")
except Exception as e:
    print(f"❌ Erro detectado: {e}")
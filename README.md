# 🛢️ Oil & Gas Financial AI Assistant (RAG)

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![LangChain](https://img.shields.io/badge/framework-LangChain-green.svg)
![Ollama](https://img.shields.io/badge/LLM-Llama3-orange.svg)
![License](https://img.shields.io/badge/license-CC%20BY--NC-red.svg)

## 🎯 Project Overview
This is a high-performance **RAG (Retrieval-Augmented Generation)** system designed to act as a **Senior Financial Analyst** specialized in the Oil & Gas sector. The assistant autonomously processes hundreds of pages from quarterly reports and financial statements, cross-referencing operational metrics to generate strategic insights.

In this implementation, the system analyzed **9 months of Petrobras operations (Q1, Q2, and Q3 2025)**, correlating record-breaking production data with energy transition feasibility.

## 🚀 Technical Highlights
- **Total Privacy:** 100% local processing using **Ollama** and **Llama 3**. Sensitive financial data never leaves the local environment.
- **Multi-Quarter Analysis:** Architecture designed to compare trends across 19 distinct reports (Q1 through Q3).
- **Advanced Context Engineering:** Optimized context window of **8,192 tokens**, enabling accurate extraction from dense financial tables.
- **Efficient Data Persistence:** Utilizes **ChromaDB** for vector storage, significantly reducing compute time by avoiding redundant document re-indexing.

## 🛠️ Tech Stack
- **Language:** Python 3.12
- **LLM:** Llama 3 (via Ollama)
- **Embeddings:** `mxbai-embed-large`
- **Orchestration:** LangChain (LCEL)
- **Vector Store:** ChromaDB
- **Document Loading:** PyPDFLoader / PDFPlumber (Optimized for financial tables)

## 📈 Strategic Insights Generated
The assistant successfully identified a critical strategic correlation:
- **Operational Excellence:** A **94% Refinery Utilization Factor** (FUT).
- **Production Records:** Total operated production reaching **4.54 MMboed**.
- **Conclusion:** These metrics function as the primary financial pillars supporting the company's decarbonization investments and the production of **SAF (Sustainable Aviation Fuel)**.

## 🔧 How to Run

### 1. Prerequisites
Ensure you have [Ollama](https://ollama.ai/) installed and the `llama3` model downloaded:
```bash ```
```
ollama pull llama3
```
### 2. Setup
Clone the repository and install dependencies:
```
git clone [https://github.com/Alandersonjs/oil-gas-financial-rag.git](https://github.com/Alandersonjs/oil-gas-financial-rag.git)
cd oil-gas-financial-rag
pip install -r requirements.txt
```

### 3. Execution
Place your PDF files in the ./data/relatorios_petrobras directory and run:
```
python src/app.py
```

# 📄 License
This project is licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).

Attribution
You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

Non-Commercial
You may not use the material for commercial purposes. This includes any use intended for or directed toward commercial advantage or private monetary compensation.

Full legal code: https://creativecommons.org/licenses/by-nc/4.0/legalcode

see the [LICENSE.md](LICENSE.md) file for details.

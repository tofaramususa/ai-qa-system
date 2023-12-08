# code_analysis_llms
Using LangChain, ChromaDB and llama to analyse and understand github code repos. 


Tools:
activeloop.ai
tavily.ai
chromadb

Steps:
1. We need to load the documents first using documentLoaders. Then split the documents -- langchain
2. We need to the create embeddings from them -- using chromadb and store them as embeddings
3. Query the database and We need to retrieve the embeddings using similarity search
4. Then pass the LLM and get the response
5. Then parse the response or do further function calling
6. 

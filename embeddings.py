from langchain.embeddings import GPT4AllEmbeddings
from load_split import docs
# Create embeddings from the documents we have in load_split

embedder = GPT4AllEmbeddings()

sentences = "This framework generates embeddings for each input sentence",
    # 'Sentences are passed as a list of string.',
    # 'The quick brown fox jumps over the lazy dog.']
# for doc in docs:
# print(docs)

docs_embed = []
for doc in docs:
	docs_embed.append(embedder.embed_documents(doc.page_content))	
print(docs_embed)

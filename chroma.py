#We have the documents plus their embeddings and then we need to create the vector store and be able to retrieve from it
import chromadb
from load_split import docs 
from embeddings import docs_embed
from langchain.vectorstores import Chroma

#we want the collection to be create once and then we either add to it or retrieve from it
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.create_collection(name="twitter_db")

collection.add(
	documents=docs,
	embeddings=docs_embed
)

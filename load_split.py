# Load the documents and split them into train and test sets
import os
from array import array
from langchain.document_loaders import TextLoader


root_dir = './twitter_algorithm'

docs = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        try:
            loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
            docs.extend(loader.load_and_split())
        except Exception as e:
            pass
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import pandas as pd
import os
from langchain_community.document_loaders import PyPDFLoader

df = pd.read_csv("realistic_restaurant_reviews.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_loc = "./chroma_langchain_db"
add_docs = not os.path.exists(db_loc)

if add_docs:
    docs = []
    ids = []


    for i, row in df.iterrows():
        doc = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        docs.append(doc)

# if add_docs:
#     loader = PyPDFLoader("my_doc.pdf")
#     docs = loader.load()


vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_loc,   # to store the DB in the storage
    embedding_function=embeddings
)

if add_docs:
    vector_store.add_documents(documents=docs, ids=ids)
    # vector_store.add_documents(documents=docs)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)
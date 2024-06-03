import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")
collection.add(
    documents=[
        "This is a document about homework",
        "This is a document about deadlines"
    ],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
    n_results=2 # how many results to return
)
print(results)


client = chromadb.PersistentClient(path="BE/storage/chromadb")

from sentence_transformers import SentenceTransformer

def getEmbeddings():
    sentences = ["This is an example sentence", "Each sentence is converted"]

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)
    return embeddings

# embeddings = getEmbeddings()
# print("embeddings len : ", len(embeddings))
# print("embeddings first element len : ", len(embeddings[0]))
# print("embeddings second element len : ", len(embeddings[1]))

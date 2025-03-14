from sentence_transformers import SentenceTransformer
import logging

logging.basicConfig(level=logging.INFO)

def getEmbeddings():
    logging.info("getEmbeddings")
    sentences = ["This is an example sentence", "Each sentence is converted"]

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)
    return embeddings

def demoCheck():
    embeddings = getEmbeddings()
    print("embeddings len : ", len(embeddings))
    print("embeddings first element len : ", len(embeddings[0]))
    print("embeddings second element len : ", len(embeddings[1]))

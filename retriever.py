import faiss
import numpy as np

index = None
stored_chunks = []


def create_faiss_index(embeddings, chunks):

    global index
    global stored_chunks

    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings).astype('float32'))

    stored_chunks = chunks


def retrieve_chunks(query_embedding, top_k=3):

    global index
    global stored_chunks

    if index is None:
        return ["No documents uploaded yet."]

    distances, indices = index.search(
        np.array([query_embedding]).astype('float32'),
        top_k
    )

    retrieved = []

    for idx in indices[0]:

        if idx < len(stored_chunks):
            retrieved.append(stored_chunks[idx])

    return retrieved
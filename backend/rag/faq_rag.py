from sentence_transformers import SentenceTransformer
import chromadb, json

class FAQ_RAG:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.db = chromadb.PersistentClient(path="./data/vectordb")
        self.col = self.db.get_or_create_collection("faq")

        if self.col.count() == 0:
            self._load()

    def _load(self):
        with open("data/clinic_info.json") as f:
            data = json.load(f)

        docs = [f"{k}: {v}" for k, v in data.items()]
        ids = [str(i) for i in range(len(docs))]
        embeddings = self.model.encode(docs).tolist()

        self.col.add(ids=ids, embeddings=embeddings, documents=docs)

    def query(self, question):
        q_emb = self.model.encode([question]).tolist()
        result = self.col.query(query_embeddings=q_emb, n_results=1)
        return result["documents"][0][0]

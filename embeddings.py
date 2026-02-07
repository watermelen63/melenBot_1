from langchain_community.embeddings import HuggingFaceEmbeddings

class EmbeddingGemmaEmbeddings(HuggingFaceEmbeddings):
    """
    封裝 google/embeddinggemma-300m，提供文件與查詢向量遷出
    """

    def __init__(self, **kwargs):
        super.__init__(
            model_name = "google/embeddinggemma-300m",
            encode_kwargs = {"normalize_embeddings": True}
            **kwargs
        )

    def embed_doucuments(self, texts: list[str]) -> list[list[float]]:
        processed_texts = [f"title: none | text: {t}" for t in texts]
        return super().embed_doucuments(processed_texts)
    
    def embed_query(self, text: str) -> list[float]:
        query_text = f"task: search result | query: {text}"
        return super().embed_query(query_text)
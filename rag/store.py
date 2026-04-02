from rag.chunker import CodeChunk


class RetrievedContext:
    pass


class VectorStore:
    def upsert_chunks(self, chunks: list[CodeChunk], embeddings: list[list[float]]) -> None:
        raise NotImplementedError

    def query(self, query_text: str, top_k: int = 8) -> list[RetrievedContext]:
        raise NotImplementedError

    def delete_file_chunks(self, file_path: str) -> None:
        raise NotImplementedError

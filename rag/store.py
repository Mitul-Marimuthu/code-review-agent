from rag.chunker import CodeChunk
from dataclasses import dataclass, field


@dataclass(slots=True)
class RetrievedContext:
    chunk_id: str
    file_path: str
    symbol_name: str
    content: str
    score: float
    start_line: int
    end_line: int
    metadata: dict[str, str] = field(default_factory=dict)


class VectorStore:
    def upsert_chunks(self, chunks: list[CodeChunk], embeddings: list[list[float]]) -> None:
        raise NotImplementedError

    def query(self, query_text: str, top_k: int = 8) -> list[RetrievedContext]:
        raise NotImplementedError

    def delete_file_chunks(self, file_path: str) -> None:
        raise NotImplementedError

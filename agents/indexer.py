from pathlib import Path
from dataclasses import dataclass, field

from rag.chunker import CodeChunk, CodeChunker
from rag.embedder import Embedder
from rag.store import VectorStore


@dataclass(slots=True)
class IndexingResult:
    repository_path: str
    total_files_scanned: int
    total_chunks_created: int
    total_chunks_embedded: int
    indexed_files: list[str] = field(default_factory=list)
    skipped_files: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)


class IndexerAgent:
    def __init__(
        self,
        chunker: CodeChunker,
        embedder: Embedder,
        store: VectorStore,
    ) -> None:
        self.chunker = chunker
        self.embedder = embedder
        self.store = store

    def index_repository(self, repo_path: Path) -> IndexingResult:
        raise NotImplementedError

    def index_file(self, file_path: Path) -> list[CodeChunk]:
        raise NotImplementedError

    def reindex_changed_files(
        self,
        repo_path: Path,
        changed_files: list[Path],
    ) -> IndexingResult:
        raise NotImplementedError

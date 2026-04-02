from pathlib import Path

from rag.chunker import CodeChunk, CodeChunker
from rag.embedder import Embedder
from rag.store import VectorStore


class IndexingResult:
    pass


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

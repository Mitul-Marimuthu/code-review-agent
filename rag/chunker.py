from pathlib import Path


class CodeChunk:
    pass


class CodeChunker:
    def chunk_file(self, file_path: Path) -> list[CodeChunk]:
        raise NotImplementedError

    def chunk_repository(self, repo_path: Path) -> list[CodeChunk]:
        raise NotImplementedError

    def detect_language(self, file_path: Path) -> str:
        raise NotImplementedError

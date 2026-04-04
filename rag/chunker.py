from pathlib import Path
from dataclasses import dataclass, field

from models import ChunkType


@dataclass(slots=True)
class CodeChunk:
    chunk_id: str
    file_path: str
    symbol_name: str
    chunk_type: ChunkType
    language: str
    start_line: int
    end_line: int
    content: str
    summary: str = ""
    imports: list[str] = field(default_factory=list)
    references: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)


class CodeChunker:
    def chunk_file(self, file_path: Path) -> list[CodeChunk]:
        raise NotImplementedError

    def chunk_repository(self, repo_path: Path) -> list[CodeChunk]:
        raise NotImplementedError

    def detect_language(self, file_path: Path) -> str:
        raise NotImplementedError

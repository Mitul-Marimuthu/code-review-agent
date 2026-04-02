from rag.store import RetrievedContext, VectorStore


class RetrieverAgent:
    def __init__(self, store: VectorStore) -> None:
        self.store = store

    def get_related_context(
        self,
        query: str,
        top_k: int = 8,
    ) -> list[RetrievedContext]:
        raise NotImplementedError

    def get_context_for_diff(
        self,
        diff_text: str,
        changed_files: list[str],
    ) -> list[RetrievedContext]:
        raise NotImplementedError

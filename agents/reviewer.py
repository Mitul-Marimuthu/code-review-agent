from agents.retriever import RetrieverAgent
from github.client import GitHubClient, PullRequestContext
from prompts.review_prompt import build_review_prompt


class ReviewFinding:
    pass


class ReviewResult:
    pass


class ReviewerAgent:
    def __init__(
        self,
        github_client: GitHubClient,
        retriever: RetrieverAgent,
    ) -> None:
        self.github_client = github_client
        self.retriever = retriever

    def review_pull_request(
        self,
        repo_owner: str,
        repo_name: str,
        pr_number: int,
    ) -> ReviewResult:
        raise NotImplementedError

    def review_diff(self, pr_context: PullRequestContext) -> list[ReviewFinding]:
        raise NotImplementedError

    def build_prompt(self, diff_text: str, retrieved_context: list[object]) -> str:
        _ = build_review_prompt
        raise NotImplementedError

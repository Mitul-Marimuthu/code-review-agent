from dataclasses import dataclass, field

from agents.retriever import RetrieverAgent
from github.client import GitHubClient, PullRequestContext
from prompts.review_prompt import build_review_prompt


@dataclass(slots=True)
class ReviewFinding:
    finding_id: str
    title: str
    description: str
    severity: str
    category: str
    file_path: str
    line_start: int
    line_end: int
    confidence: float
    suggested_fix: str = ""
    rule_ids: list[str] = field(default_factory=list)
    related_chunk_ids: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(slots=True)
class ReviewResult:
    repo_owner: str
    repo_name: str
    pr_number: int
    summary: str
    findings: list[ReviewFinding] = field(default_factory=list)
    overall_risk: str = "unknown"
    model_name: str = ""
    prompt_version: str = ""
    metadata: dict[str, str] = field(default_factory=dict)


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

from dataclasses import dataclass, field

from agents.reviewer import ReviewFinding
from github.client import GitHubClient
from models import ActionType


@dataclass(slots=True)
class ActionResult:
    success: bool
    action_type: ActionType
    target_url: str = ""
    branch_name: str = ""
    commit_sha: str = ""
    created_ids: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)


class ActionAgent:
    def __init__(self, github_client: GitHubClient) -> None:
        self.github_client = github_client

    def post_review_comments(
        self,
        repo_owner: str,
        repo_name: str,
        pr_number: int,
        findings: list[ReviewFinding],
    ) -> ActionResult:
        raise NotImplementedError

    def create_fix_pull_request(
        self,
        repo_owner: str,
        repo_name: str,
        finding: ReviewFinding,
    ) -> ActionResult:
        raise NotImplementedError

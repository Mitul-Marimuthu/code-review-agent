from agents.reviewer import ReviewFinding
from github.client import GitHubClient


class ActionResult:
    pass


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

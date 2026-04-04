from dataclasses import dataclass, field

from models import FileChangeStatus


@dataclass(slots=True)
class ChangedFile:
    path: str
    status: FileChangeStatus
    additions: int = 0
    deletions: int = 0
    patch: str = ""
    previous_path: str | None = None


@dataclass(slots=True)
class PullRequestContext:
    repo_owner: str
    repo_name: str
    pr_number: int
    title: str
    body: str
    base_branch: str
    head_branch: str
    head_sha: str
    author: str
    diff_text: str = ""
    changed_files: list[ChangedFile] = field(default_factory=list)
    labels: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)


class GitHubClient:
    def get_pull_request(
        self,
        repo_owner: str,
        repo_name: str,
        pr_number: int,
    ) -> PullRequestContext:
        raise NotImplementedError

    def get_pull_request_diff(self, repo_owner: str, repo_name: str, pr_number: int) -> str:
        raise NotImplementedError

    def get_changed_files(
        self,
        repo_owner: str,
        repo_name: str,
        pr_number: int,
    ) -> list[ChangedFile]:
        raise NotImplementedError

    def post_review_comment(
        self,
        repo_owner: str,
        repo_name: str,
        pr_number: int,
        body: str,
        commit_id: str | None = None,
        path: str | None = None,
        line: int | None = None,
    ) -> None:
        raise NotImplementedError

    def create_pull_request(
        self,
        repo_owner: str,
        repo_name: str,
        title: str,
        head: str,
        base: str,
        body: str,
    ) -> str:
        raise NotImplementedError

class PullRequestContext:
    pass


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

    def get_changed_files(self, repo_owner: str, repo_name: str, pr_number: int) -> list[str]:
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

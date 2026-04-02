import typer


app = typer.Typer()


@app.command()
def index(repo_path: str) -> None:
    raise NotImplementedError


@app.command()
def review(repo_owner: str, repo_name: str, pr_number: int) -> None:
    raise NotImplementedError


@app.command()
def serve(host: str = "0.0.0.0", port: int = 8000) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    app()

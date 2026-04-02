from fastapi import FastAPI, Request


app = FastAPI()


@app.get("/health")
async def healthcheck() -> dict[str, str]:
    raise NotImplementedError


@app.post("/webhooks/github")
async def github_webhook(request: Request) -> dict[str, str]:
    raise NotImplementedError

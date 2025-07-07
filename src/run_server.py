"""Run Server."""

import asyncio

import uvicorn


async def run_server() -> None:
    """Run Server."""
    config = uvicorn.Config(
        "app.main:app",
        port=8000,
        log_level="info",
        reload=True,
        root_path="app",
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(run_server())

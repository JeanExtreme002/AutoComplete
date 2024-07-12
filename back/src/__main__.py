import uvicorn

from src.config import Config


def main() -> None:

    uvicorn.run(
        "src.api.app:get_app",
        workers=Config.WORKERS_COUNT,
        host=Config.HOST,
        port=Config.PORT,
        reload=Config.RELOAD,
        log_level=Config.LOG_LEVEL,
        factory=True,
    )


if __name__ == "__main__":
    main()

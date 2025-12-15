from fastapi import FastAPI

from entrypoints.routes import v1


def application() -> FastAPI:
    app = FastAPI(title="Password Challange")

    app.include_router(v1)

    return app


app = application()

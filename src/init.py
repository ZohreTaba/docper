from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from settings import settings
from routers import member, category, author, document, permission


def create_app():
    app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

    register_tortoise(
        app,
        db_url=get_db_uri(
            user=settings.POSTGRES_USERNAME,
            passwd=settings.POSTGRES_PASSWORD,
            host=settings.POSTGRES_HOSTNAME,
            db=settings.POSTGRES_DATABASE,
            port=settings.POSTGRES_PORT
        ),
        modules={"models": ["models.document", "models.member", "models.permission"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    register_router(app=app)

    return app


def get_db_uri(user, passwd, host, db, port):
    return f"postgres://{user}:{passwd}@{host}:{port}/{db}"


def register_router(app: FastAPI):
    app.include_router(member.router, prefix="/member", tags=["Member"])
    app.include_router(category.router, prefix="/category", tags=["Category"])
    app.include_router(author.router, prefix="/author", tags=["Author"])
    app.include_router(document.router, prefix="/document", tags=["Document"])
    app.include_router(permission.router, prefix="/permission", tags=["Permission"])

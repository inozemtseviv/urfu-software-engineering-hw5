from fastapi import APIRouter

from app.models import HomeResponse


def get_home_router():
    router = APIRouter()

    @router.get("/")
    def home() -> HomeResponse:
        return HomeResponse(text="Привет!")

    return router

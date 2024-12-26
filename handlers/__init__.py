from fastapi import APIRouter
from .example import router as example_router
from .auth import auth_router

router = APIRouter()

router.include_router(example_router)
router.include_router(auth_router)

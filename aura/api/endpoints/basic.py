# aura/api/endpoints/basic.py

from fastapi import (
    APIRouter,
)

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Welcome to AURA"}


@router.get("/ping")
def ping():
    return {"message": "pong"}

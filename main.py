# main.py

from fastapi import (
    FastAPI,
)
from sqlalchemy.orm import Session
import uvicorn
from app.api.endpoints import (
    user,
)
from app.database.session import (
    Base,
    engine,
)

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user.router)


def get_session():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()

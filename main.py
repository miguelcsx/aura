# main.py

from fastapi import (
    FastAPI,
)
from sqlalchemy.orm import Session
import uvicorn
from app.api.endpoints import (
    activity,
    answer,
    question,
    study_session,
    user,
)
from app.database.session import (
    Base,
    engine,
)

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(activity.router)
app.include_router(answer.router)
app.include_router(question.router)
app.include_router(study_session.router)
app.include_router(user.router)


def get_session():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Welcome to AURA"}


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()

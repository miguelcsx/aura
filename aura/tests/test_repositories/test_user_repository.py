# aura/tests/test_repositories/test_user_repository.py

from datetime import datetime
from aura.repositories.user_repository import (
    create_user,
    get_user,
    update_user,
    delete_user,
)
from aura.schemas.user import UserCreate, UserUpdate
from aura.database.models import UserRole


def test_create_user(test_db) -> None:
    user_create = UserCreate(
        username="test_create_user",
        email="test_user@example.com",
        role=UserRole.student,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    user = create_user(test_db, user_create)

    assert user.id is not None
    assert user.username == "test_create_user"
    assert user.email == "test_user@example.com"
    assert user.role == UserRole.student


def test_get_user(test_db) -> None:
    user_create = UserCreate(
        username="test_get_user",
        email="test_get_user@example.com",
        role=UserRole.student,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    user = create_user(test_db, user_create)
    retrieved_user = get_user(test_db, user.id)

    assert retrieved_user is not None
    assert retrieved_user.id == user.id
    assert retrieved_user.username == "test_get_user"
    assert retrieved_user.email == "test_get_user@example.com"


def test_update_user(test_db) -> None:
    user_create = UserCreate(
        username="test_user_update",
        email="test_user_update@example.com",
        role=UserRole.student,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    created_user = create_user(test_db, user_create)

    user_update = UserUpdate(
        username="updated_user",
        email="updated_user@example.com",
        role=UserRole.teacher,
        updated_at=datetime.now(),
    )

    updated_user = update_user(test_db, created_user.id, user_update)

    assert updated_user.username == "updated_user"
    assert updated_user.email == "updated_user@example.com"
    assert updated_user.role == UserRole.teacher


def test_delete_user(test_db) -> None:
    user_create = UserCreate(
        username="test_delete_user",
        email="test_delete_user@example.com",
        role=UserRole.student,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    user = create_user(test_db, user_create)
    delete_user(test_db, user.id)

    assert get_user(test_db, user.id) is None

# aura/tests/test_database/test_models.py

from aura.database.models import User, UserRole


user = User(
    username="test_user_model",
    email="test@example.com",
    role=UserRole.student,
)


def test_user_model(test_db):
    test_db.add(user)
    test_db.commit()

    assert user.id is not None
    assert user.username == "test_user_model"
    assert user.email == "test@example.com"
    assert user.role == UserRole.student

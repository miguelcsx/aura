# tests/app/database/models/test_user_model.py

import pytest
from datetime import datetime
from app.database.models.user_model import UserModel
from app.database.models.subject_model import SubjectModel

@pytest.fixture
def sample_user_model():
    discord_id = "123456789"
    username = "test_user"
    created_at = datetime(2024, 4, 10)
    subjects = [SubjectModel(name="Math"), SubjectModel(name="Science")]
    return UserModel(discord_id=discord_id, username=username, created_at=created_at, subjects=subjects)

def test_user_model_creation(sample_user_model):
    user = sample_user_model

    assert user.discord_id == "123456789"
    assert user.username == "test_user"
    assert user.created_at == datetime(2024, 4, 10)
    assert user.subjects[0].name == "Math"
    assert user.subjects[1].name == "Science"

def test_user_model_repr(sample_user_model):
    user = sample_user_model

    expected_repr = f"<User(id={user.id}, discord_id={user.discord_id}, username={user.username}, created_at={user.created_at})>"
    assert repr(user) == expected_repr

def test_user_model_relationships(sample_user_model):
    user = sample_user_model

    assert len(user.subjects) == 2
    assert isinstance(user.subjects[0], SubjectModel)
    assert isinstance(user.subjects[1], SubjectModel)

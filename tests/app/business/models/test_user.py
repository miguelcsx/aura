# test/app/business/models/test_user.py

import pytest
from datetime import datetime
from app.business.models.user import User

@pytest.fixture
def sample_user():
    return User(
        id=1,
        discord_id="123456789",
        username="test_user",
        created_at=datetime(2024, 4, 10),
        subjects=["Math", "Science"]
    )

def test_user_init(sample_user):
    assert sample_user.id == 1
    assert sample_user.discord_id == "123456789"
    assert sample_user.username == "test_user"
    assert sample_user.created_at == datetime(2024, 4, 10)
    assert sample_user.subjects == ["Math", "Science"]

def test_user_repr(sample_user):
    expected_repr = "User(id=1, discord_id=123456789, username=test_user, created_at={})".format(sample_user.created_at)
    assert repr(sample_user) == expected_repr

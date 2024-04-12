# test/app/business/models/test_subject.py

import pytest
from app.business.models.subject import Subject

@pytest.fixture
def sample_subject():
    return Subject(
        id=1,
        name="Math",
        description="Mathematics",
        user_id=1,
        topics=["Algebra", "Geometry"]
    )

def test_subject_init(sample_subject):
    assert sample_subject.id == 1
    assert sample_subject.name == "Math"
    assert sample_subject.description == "Mathematics"
    assert sample_subject.user_id == 1
    assert sample_subject.topics == ["Algebra", "Geometry"]

def test_subject_repr(sample_subject):
    expected_repr = "Subject(id=1, name=Math, description=Mathematics, user_id=1)"
    assert repr(sample_subject) == expected_repr

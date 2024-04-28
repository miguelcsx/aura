# tests/app/database/models/test_user_model.py

import pytest
from app.database.models.subject_model import SubjectModel
from app.database.models.topic_model import TopicModel


@pytest.fixture
def sample_subject_model():
    name = "Math"
    description = "Mathematics"
    user_id = 1
    topics = [TopicModel(title="Algebra"), TopicModel(title="Geometry")]
    return SubjectModel(name=name, description=description,
                        user_id=user_id, topics=topics)


def test_subject_model_creation(sample_subject_model):
    subject = sample_subject_model

    assert subject.name == "Math"
    assert subject.description == "Mathematics"
    assert subject.user_id == 1
    assert subject.topics[0].title == "Algebra"
    assert subject.topics[1].title == "Geometry"


def test_subject_model_representation(sample_subject_model):
    subject = sample_subject_model

    expected_repr = (
        f"Subject(id={subject.id}, "
        f"name={subject.name}, "
        f"description={subject.description}, "
        f"user_id={subject.user_id})"
    )
    assert repr(subject) == expected_repr


def test_subject_model_relationships(sample_subject_model):
    subject = sample_subject_model

    assert len(subject.topics) == 2
    assert isinstance(subject.topics[0], TopicModel)
    assert isinstance(subject.topics[1], TopicModel)

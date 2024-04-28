# tests/app/database/models/test_topic_model.py

import pytest
from app.database.models.topic_model import TopicModel


@pytest.fixture
def sample_topic_model():
    return TopicModel(
        title="Math",
        content="Mathematics",
        subject_id=1
    )


def test_topic_model_creation(sample_topic_model):
    topic = sample_topic_model

    assert topic.title == "Math"
    assert topic.content == "Mathematics"
    assert topic.subject_id == 1


def test_topic_model_representation(sample_topic_model):
    topic = sample_topic_model

    expected_repr = f"<Topic(id={topic.id}, title={topic.title}, content={topic.content}, subject_id={topic.subject_id})>"
    assert repr(topic) == expected_repr

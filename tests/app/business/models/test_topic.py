# test/app/business/models/test_topic.py

import pytest
from app.business.models.topic import Topic

@pytest.fixture
def sample_topic():
    return Topic(
        id=1,
        title="Math",
        content="Mathematics",
        subject_id=1
    )

def test_topic_init(sample_topic):
    assert sample_topic.id == 1
    assert sample_topic.title == "Math"
    assert sample_topic.content == "Mathematics"
    assert sample_topic.subject_id == 1

def test_topic_repr(sample_topic):
    expected_repr = "<Topic(id=1, title=Math, content=Mathematics, subject_id=1)>"
    assert repr(sample_topic) == expected_repr

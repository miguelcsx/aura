# tests/app/database/test_db.py

from unittest.mock import patch
import pytest
from app.database.db import create_tables, engine


@pytest.fixture
def mock_inspector():
    with patch("app.database.db.inspect") as mock_inspector:
        yield mock_inspector


@pytest.fixture
def mock_create_all():
    with patch("app.database.db.Base.metadata.create_all") as mock_create_all:
        yield mock_create_all


def test_create_tables_when_no_tables_exist(mock_inspector, mock_create_all):
    # Arrange
    mock_inspector.return_value.get_table_names.return_value = []
    # Act
    create_tables()
    # Assert
    mock_inspector.assert_called_once_with(engine)
    mock_create_all.assert_called_once_with(bind=engine)


def test_create_tables_when_tables_exist(mock_inspector, mock_create_all):
    # Arrange
    mock_inspector.return_value.get_table_names.return_value = ["users", "subjects"]
    # Act
    create_tables()
    # Assert
    mock_inspector.assert_called_once_with(engine)
    mock_create_all.assert_not_called()

# tests/app/wikipedia_api/test_scraper.py

import pytest
from unittest.mock import patch, MagicMock
from wikipedia.exceptions import PageError, DisambiguationError, WikipediaException
from app.wikipedia_api.scraper import WikiDocs

@patch('wikipedia.page')
def test_valid_theme(mock_page):
    mock_page.return_value.title = "Python (programming language)"
    mock_page.return_value.content = "Python is an interpreted high-level programming language."
    mock_page.return_value.url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    theme = "Python (programming language)"
    wiki_docs = WikiDocs(theme)

    assert wiki_docs.name == "Python (programming language)"
    assert wiki_docs.content == mock_page.return_value.content
    assert wiki_docs.url == mock_page.return_value.url

@patch('wikipedia.page', side_effect=PageError)
def test_auto_suggest(mock_page):
    mock_page.side_effect = None
    mock_page.return_value.title = "Python (programming language)"
    mock_page.return_value.content = "Python is an interpreted high-level programming language."
    mock_page.return_value.url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    theme = "Python programming"
    wiki_docs = WikiDocs(theme)

    assert wiki_docs.name == "Python (programming language)"
    assert wiki_docs.content == mock_page.return_value.content
    assert wiki_docs.url == mock_page.return_value.url

@patch('wikipedia.page', side_effect=DisambiguationError)
def test_disambiguation(mock_page):
    mock_page.side_effect = DisambiguationError("Disambiguation page", ["Option 1", "Option 2"])

    theme = "Python"
    wiki_docs = WikiDocs(theme)

    assert wiki_docs.name is None
    assert wiki_docs.content == "Disambiguation page. Please select from the following options: Option 1, Option 2"
    assert wiki_docs.url is None

@patch('wikipedia.page', side_effect=WikipediaException)
def test_wikipedia_exception(mock_page):
    theme = "NonExistentTopic"
    wiki_docs = WikiDocs(theme)

    assert wiki_docs.name is None
    assert wiki_docs.content is None
    assert wiki_docs.url is None
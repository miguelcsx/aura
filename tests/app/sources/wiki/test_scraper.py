# tests/app/wikipedia_api/test_scraper.py

import pytest
from unittest.mock import patch, MagicMock
from wikipedia.exceptions import PageError, DisambiguationError, WikipediaException
from app.sources.wiki.scraper import WikiDocs

@pytest.fixture
def mock_wikipedia_search():
    with patch('app.wikipedia_api.scraper.wikipedia.search') as mock_search:
        yield mock_search

@pytest.fixture
def mock_wikipedia_summary():
    with patch('app.wikipedia_api.scraper.wikipedia.summary') as mock_summary:
        yield mock_summary

@pytest.fixture
def mock_wikipedia_page():
    with patch('app.wikipedia_api.scraper.wikipedia.page') as mock_page:
        yield mock_page

def test_search_with_results(mock_wikipedia_search):
    mock_wikipedia_search.return_value = ['Result 1', 'Result 2']
    wiki = WikiDocs('Python')
    assert wiki.search() == "Result 1\nResult 2"

def test_search_with_no_results(mock_wikipedia_search):
    mock_wikipedia_search.return_value = []
    wiki = WikiDocs('Nonexistent')
    assert wiki.search() == "No results found"

def test_search_exception(mock_wikipedia_search):
    mock_wikipedia_search.side_effect = Exception('Some error')
    wiki = WikiDocs('Python')
    assert wiki.search() == "An error occurred: Some error"

def test_summary(mock_wikipedia_summary, mock_wikipedia_page):
    mock_wikipedia_summary.return_value = "Summary text\n\nAdditional info"
    mock_wikipedia_page.return_value.url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    wiki = WikiDocs('Python')
    theme, content, url = wiki.summary()
    assert theme == 'Python'
    assert content == 'Summary text'
    assert url == 'https://en.wikipedia.org/wiki/Python_(programming_language)'

def test_summary_exception(mock_wikipedia_summary, mock_wikipedia_page):
    mock_wikipedia_summary.side_effect = Exception('Summary error')
    wiki = WikiDocs('Python')
    result = wiki.summary()
    assert result == "An error occurred: Summary error"

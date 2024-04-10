import wikipedia

class WikiDocs():

    def __init__(self, theme: str) -> None:
        """is search wikipedia don't exist, self.name
        is None"""

        result: list[str] = wikipedia.search(theme)

        if len(result) == 0:
            self.name: str | None = None
        else:
            page: wikipedia.wikipedia.WikipediaPage = wikipedia.page(result[0])
            self.name = page.title
            self.content: str = page.summary
            self.url: str = page.url
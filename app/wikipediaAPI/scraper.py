import wikipedia

class wikidocs():
    def __init__(self, title: str) -> None:
        names: list[str] = wikipedia.search(title)
        if len(names) != 0:
            self.name: str | None  = wikipedia.page(names[0]).title
            self.summary: str = wikipedia.page(title).summary
            self.link: str = wikipedia.page(title).url
        else:
            self.name = None

    def __str__(self) -> str:
        return self.name

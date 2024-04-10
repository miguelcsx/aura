import wikipedia

class WikiDocs():

    def __init__(self, theme: str) -> None:
        """is search wikipedia don't exist, self.name
        is None"""
        
        try:
            self.name = theme
            self.content= wikipedia.summary(self.name)
            self.url = wikipedia.page(theme).url
        except (wikipedia.exceptions.WikipediaException):
            self.name = None
            self.content = None
            self.url = None
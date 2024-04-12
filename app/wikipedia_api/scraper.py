import wikipedia

class WikiDocs:
    def __init__(self, theme: str) -> None:
        self.theme = theme

    def search(self) -> str:
        try:
            search_results = wikipedia.search(self.theme)
            if not search_results:
                return "No results found"
            else:
                return "\n".join(search_results)
        except Exception as e:
            return f"An error occurred: {e}"
    
    def summary(self):
        try:
            content = wikipedia.summary(self.theme, auto_suggest=False)
            content = content[:content.find('\n\n')]
            url = wikipedia.page(self.theme).url

            return self.theme, content, url
        except Exception as e:
            return f"An error occurred: {e}"

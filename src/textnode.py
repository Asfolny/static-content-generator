class TextNode:
    """A markdown textnode"""

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, cmp):
        return (
            self.text == cmp.text
            and self.text_type == cmp.text_type
            and self.url == cmp.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

from htmlnode import LeafNode

type_text = "text"
type_bold = "bold"
type_italic = "italic"
type_code = "code"
type_link = "link"
type_image = "image"

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
    
    def text_node_to_hmtl_node(text_node):
        if text_node.text_type == type_text:
            return LeafNode(None, text_node.text)
        if text_node.text_type == type_bold:
            return LeafNode('b', text_node.text)
        if text_node.text_type == type_italic:
            return LeafNOde('i', text_node.text)
        if text_node.text_type == type_code:
            return LeafNode('code', text_node.text)
        if text_node.text_type == type_link:
            return LeafNode('a', text_node.text, {"href": text_node.url})
        if text_node.text_type == type_image:
            return LeafNode('img', '', {"alt": text_node.text, "src": text_node.url})
        
        raise ValueError(f"Unsupported text type: {text_node.text_type}")



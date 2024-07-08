import unittest
from textnode import (
    TextNode,
    type_text,
    type_bold,
    type_italic,
    type_code,
    type_image,
    type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node",type_text)
        node2 = TextNode("This is a text node", type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", type_text)
        node2 = TextNode("This is a text node", type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", type_text)
        node2 = TextNode("This is a text node2", type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", type_italic, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", type_italic, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()


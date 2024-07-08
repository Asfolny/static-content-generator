import unittest
from inline import (
    split_nodes_delimiter,
)

from textnode import (
    TextNode,
    type_text,
    type_bold,
    type_italic,
    type_code,
)


class TestInline(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", type_text)
        new_nodes = split_nodes_delimiter([node], "**", type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", type_text),
                TextNode("bolded", type_bold),
                TextNode(" word", type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", type_text),
                TextNode("bolded", type_bold),
                TextNode(" word and ", type_text),
                TextNode("another", type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", type_text),
                TextNode("bolded word", type_bold),
                TextNode(" and ", type_text),
                TextNode("another", type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", type_text)
        new_nodes = split_nodes_delimiter([node], "*", type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", type_text),
                TextNode("italic", type_italic),
                TextNode(" word", type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", type_text)
        new_nodes = split_nodes_delimiter([node], "**", type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", type_italic)
        self.assertListEqual(
            [
                TextNode("bold", type_bold),
                TextNode(" and ", type_text),
                TextNode("italic", type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", type_text)
        new_nodes = split_nodes_delimiter([node], "`", type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", type_text),
                TextNode("code block", type_code),
                TextNode(" word", type_text),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()

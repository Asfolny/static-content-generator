import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"class": "center"})

        self.assertEqual(node.props_to_html(), 'class="center"')


class TestLeafNode(unittest.TestCase):
    def test_leaf_node_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

        node = LeafNode(None, "This is just raw text")
        self.assertEqual("This is just raw text", node.to_html())

        node = LeafNode("div", "This is an attributed node", {"class": "center"})
        self.assertEqual('<div class="center">This is an attributed node</div>', node.to_html())


class TestParentNode(unittest.TestCase):
    def test_parent_node_to_html(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "bold text"),
                    ParentNode("p", [LeafNode('i', "inner text")])
                ]
            )
        self.assertEqual("<p><b>bold text</b><p><i>inner text</i></p></p>", node.to_html())



if __name__ == "__main__":
    unittest.main()

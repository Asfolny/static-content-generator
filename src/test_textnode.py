import unittest
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
        node_with_url = TextNode("This is a text node", "bold", 'http://example.com')
        node2_with_url = TextNode("This is a text node", "bold", 'http://example.com')
        self.assertEqual(node_with_url, node2_with_url)


if __name__ == "__main__":
    unittest.main()

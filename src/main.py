from textnode import TextNode
from htmlnode import LeafNode

def main():
    print(TextNode("This is a text node", "bold", "https://www.boot.dev"))

def text_node_to_hmtl_node(text_node):
    match text_node.text_type:
        case 'text':
            return LeafNode(None, text_node.text)
        case 'bold':
            return LeafNode('b', text_node.text)
        case 'italic':
            return LeafNOde('i', text_node.text)
        case 'code':
            return LeafNode('code', text_node.text)
        case 'link':
            return LeafNode('a', text_node.text, {"href": text_node.url})
        case 'image':
            return LeafNode('img', '', {"alt": text_node.text, "src": text_node.url})
        case _:
            raise ValueError('Unsupported text type')

main()

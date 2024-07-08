class HTMLNode:
    """A node of HTML"""

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ''

        return " ".join([f"{name}=\"{value}\"" for _, (name, value) in enumerate(self.props.items())])

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    """A HTML node with no children"""

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError

        if self.tag is None:
            return str(self.value)

        html = f"<{self.tag}"
        attrs = self.props_to_html()
        
        if len(attrs) > 0:
            html += f" {attrs}"

        html += f">{self.value}</{self.tag}>"

        return html


class ParentNode(HTMLNode):
    """A HTML node with children"""

    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError

        if len(self.children) < 1:
            raise ValueError

        html = f"<{self.tag}"
        attrs = self.props_to_html()

        if len(attrs) > 0:
            html += f" {attrs}"

        html += ">"

        for child in self.children:
            html += child.to_html()

        return html + f"</{self.tag}>"

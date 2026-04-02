from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode not assigned a value")
        if self.tag is None:
            return f"{self.value}"
        prop_input = ""
        if self.props is not None:
            prop_input = " "
            for key in self.props:
                prop_input = f'{prop_input}{key}="{self.props[key]}" '
        return f"<{self.tag}{prop_input}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    
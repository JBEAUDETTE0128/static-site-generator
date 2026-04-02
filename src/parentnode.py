from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode not assigned a tag")
        if self.children is None:
            raise ValueError("ParentNode not assigned children nodes")
        prop_input = ""
        if self.props is not None:
            prop_input = " "
            for key in self.props:
                prop_input = f'{prop_input}{key}="{self.props[key]}" '

        output = f"<{self.tag}{prop_input}>"
        for child in self.children:
            output = f"{output}{child.to_html()}"
        output = f"{output}</{self.tag}>"

        return output
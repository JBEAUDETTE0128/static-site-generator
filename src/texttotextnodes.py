from textnode import TextNode
from texttype import TextType
from splitnodes import split_nodes_image, split_nodes_link
from splitnodesdelimiter import split_nodes_delimiter

def text_to_textnodes(text):
    if text is None:
        raise ValueError("Error: None Input")
    if text == "":
        raise ValueError("Error: No Text to Parse")
    if not isinstance(text, str):
        raise TypeError("Error: Input must be a string of text.")
    initial_node_list = [TextNode(text, TextType.TEXT)]
    bold_nodes = split_nodes_delimiter(initial_node_list, "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
    image_nodes = split_nodes_image(code_nodes)
    link_nodes = split_nodes_link(image_nodes)
    return link_nodes

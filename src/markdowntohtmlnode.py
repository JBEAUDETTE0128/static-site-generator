from markdowntoblocks import markdown_to_blocks
from blocktoblocktype import block_to_block_type
from blocktype import BlockType
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode
from texttohtml import text_node_to_html_node
from texttotextnodes import text_to_textnodes
from texttype import TextType
from splitnodesdelimiter import split_nodes_delimiter

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    root_html_children = []
    for block in blocks:
        type = block_to_block_type(block)
        html_child = create_new_html_node(block, type)
        root_html_children.append(html_child)
    root = ParentNode("div", root_html_children)
    return root

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        child = text_node_to_html_node(node)
        children.append(child)
    return children


def create_new_html_node(block, type):
    match type:
        case BlockType.HEADING:
            count_heading = count_heading_tag(block)
            html_block = block[count_heading + 1:]
            children = text_to_children(html_block)
            return ParentNode(f"h{count_heading}", children)
        case BlockType.QUOTE:
            block_lines = block.split('\n')
            quote_lines = []
            for line in block_lines:
                quote_lines.append(line[1:].strip())
            html_block = "\n".join(quote_lines)
            children = text_to_children(html_block)
            return ParentNode("blockquote", children)
        case BlockType.UNORDERED_LIST:
            block_lines = block.split('\n')
            ul_children = []
            for line in block_lines:
                html_children = text_to_children(line[2:].strip())
                html_child = ParentNode("li", html_children)
                ul_children.append(html_child)
            return ParentNode("ul", ul_children)
        case BlockType.ORDERED_LIST:
            block_lines = block.split('\n')
            ol_children = []
            for line in block_lines:
                html_children = text_to_children(line.split(' ', 1)[1])
                html_child = ParentNode("li", html_children)
                ol_children.append(html_child)
            return ParentNode("ol", ol_children)
        case BlockType.PARAGRAPH:
            children = text_to_children(block)
            return ParentNode("p", children)
        case BlockType.CODE:
            split_code_block = block[4:-3]
            code_node = TextNode(split_code_block, TextType.CODE)
            code_nested = text_node_to_html_node(code_node)
            return ParentNode("pre", [code_nested])

def count_heading_tag(heading_block):
    check_heading = heading_block[:6]
    count = 0
    for char in check_heading:
        if char == '#':
            count += 1
        else:
            break
    return count



    
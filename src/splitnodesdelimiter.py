from textnode import TextNode
from texttype import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes is None:
        raise ValueError("Error: No TextNodes Found")
    if text_type is None:
        raise ValueError("Error: Text Type Required")
    match delimiter:
        case "**":
            if text_type != TextType.BOLD:
                raise TypeError("Error: Type Should Be Bold **")
        case "_":
            if text_type != TextType.ITALIC:
                raise TypeError("Error: Type Should Be Italic _")
        case "`":
            if text_type != TextType.CODE:
                raise TypeError("Error: Type Should Be Code `")
        case _:
            raise ValueError("Error: Invalid Delimiter")
    
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            partitions = node.text.split(delimiter)
            if len(partitions) % 2 != 1:
                raise Exception("Error: Invalid Markdown Syntax")
            for index in range(len(partitions)):
                if index % 2 == 0 or index == 0:
                    if partitions[index] != "":
                        new_nodes.append(TextNode(partitions[index], TextType.TEXT))
                else:
                    if partitions[index] != "":
                        new_nodes.append(TextNode(partitions[index], text_type))
                    else:
                        raise ValueError("Error: Empty Inline Text")
    print(new_nodes)
    return new_nodes
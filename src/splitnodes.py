from textnode import TextNode
from texttype import TextType

from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    if old_nodes is None:
        raise ValueError("Error: No TextNodes Found")
    new_nodes = []
    for node in old_nodes:
        if node is None:
            raise ValueError("Error: Empty List Entry in TextNodes")
        # No empty text TextNodes
        if node.text == "":
            continue
        # Only operate on Text Nodes.
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
            continue
        countdown = len(images)
        next_string = node.text
        for image in images:
            countdown -= 1
            partitions = next_string.split(f"![{image[0]}]({image[1]})", 1)
            if partitions[0] != "":
                new_nodes.append(TextNode(partitions[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            if countdown == 0 and partitions[1] != "":
                new_nodes.append(TextNode(partitions[1], TextType.TEXT))
            else:
                next_string = partitions[1]
    return new_nodes

def split_nodes_link(old_nodes):
    if old_nodes is None:
        raise ValueError("Error: No TextNodes Found")
    new_nodes = []
    for node in old_nodes:
        if node is None:
            raise ValueError("Error: Empty List Entry in TextNodes")
        # No empty text TextNodes
        if node.text == "":
            continue
        # Only operate on Text Nodes.
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
            continue
        countdown = len(links)
        next_string = node.text
        for link in links:
            countdown -= 1
            partitions = next_string.split(f"[{link[0]}]({link[1]})", 1)
            if partitions[0] != "":
                new_nodes.append(TextNode(partitions[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            if countdown == 0 and partitions[1] != "":
                new_nodes.append(TextNode(partitions[1], TextType.TEXT))
            else:
                if partitions[1] != "":
                    next_string = partitions[1]
    return new_nodes
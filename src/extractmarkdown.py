import re

def extract_markdown_images(text):
    if text is None:
        raise ValueError("Error: No text to parse.")
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images
    
def extract_markdown_links(text):
    if text is None:
        raise ValueError("Error: No text to parse.")
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links
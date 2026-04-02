from enum import Enum
from textnode import TextType, TextNode

def main():
    dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.anchor.com")
    print(dummy)

main()
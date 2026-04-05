from textnode import TextNode
from texttype import TextType

def main():
    dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.anchor.com")
    print(dummy)

main()
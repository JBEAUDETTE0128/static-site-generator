from textnode import TextNode
from texttype import TextType
from copystatictopublic import copy_static_to_public
from generatepage import generate_page

def main():
    copy_static_to_public()
    generate_page("content/index.md", "template.html", "public/index.html")
main()
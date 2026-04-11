from textnode import TextNode
from texttype import TextType
from copystatictopublic import copy_static_to_public
from generatepage import generate_page
from generatepagesrecursive import generate_pages_recursive

def main():
    copy_static_to_public()
    generate_pages_recursive("content/", "template.html", "public/")
main()
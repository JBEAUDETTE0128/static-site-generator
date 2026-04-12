import sys
from textnode import TextNode
from texttype import TextType
from copystatictopublic import copy_static_to_public
from generatepage import generate_page
from generatepagesrecursive import generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_static_to_public()
    generate_pages_recursive("content/", "template.html", "public/", basepath)
main()
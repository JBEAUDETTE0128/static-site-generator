import sys
from textnode import TextNode
from texttype import TextType
from copystatic import copy_static
from generatepage import generate_page
from generatepagesrecursive import generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_static("./docs")
    generate_pages_recursive("content/", "template.html", "./docs/", basepath)
main()
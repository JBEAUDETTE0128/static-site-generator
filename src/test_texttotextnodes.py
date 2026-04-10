import unittest

from textnode import TextNode
from texttype import TextType
from texttotextnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_standard_input(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        output = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

    def test_none_input(self):
        with self.assertRaises(ValueError):
            output = text_to_textnodes(None)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            output = text_to_textnodes("")
    
    def test_nonstring_input(self):
        with self.assertRaises(TypeError):
            output = text_to_textnodes(True)
if __name__ == "__main__":
    unittest.main()
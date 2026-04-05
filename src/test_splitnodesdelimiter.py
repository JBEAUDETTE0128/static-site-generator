import unittest

from textnode import TextNode
from texttype import TextType

from splitnodesdelimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def no_split(self):
        node = TextNode("This text is already split", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This text is already split", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_all_text(self):
        node = TextNode("This text has no delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This text has no delimiter", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("bold", TextType.BOLD, None),
            TextNode(" word", TextType.TEXT, None),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with an ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" word", TextType.TEXT, None),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE, None),
            TextNode(" word", TextType.TEXT, None),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_multiple_code(self):
        node = TextNode("This is `text` with multiple `code blocks`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT, None),
            TextNode("text", TextType.CODE, None),
            TextNode(" with multiple ", TextType.TEXT, None),
            TextNode("code blocks", TextType.CODE, None),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_empty_inline(self):
        node = TextNode("This is an `` empty inline", TextType.TEXT)
        with self.assertRaises(ValueError):
            output = split_nodes_delimiter([node], "`", TextType.CODE)

    def test_no_closing_delimiter(self):
        node = TextNode("This text is missing `code delimiter", TextType.TEXT)
        with self.assertRaises(Exception):
            output = split_nodes_delimiter([node], "`", TextType.CODE)

    def test_none_nodes(self):
        with self.assertRaises(ValueError):
            output = split_nodes_delimiter(None, "`", TextType.CODE)

    def test_none_type(self):
        node = TextNode("Empty TextType", TextType.TEXT)
        with self.assertRaises(ValueError):
            output = split_nodes_delimiter([node], "`", None)

    def test_bold_mismatch(self):
        node = TextNode("This is a **bold** mismatch", TextType.TEXT)
        with self.assertRaises(TypeError):
            output = split_nodes_delimiter([node], "**", TextType.CODE)


    def test_italic_mismatch(self):
        node = TextNode("This is an _italic_ mismatch", TextType.TEXT)
        with self.assertRaises(TypeError):
            output = split_nodes_delimiter([node], "_", TextType.CODE)

    def test_code_mismatch(self):
        node = TextNode("This is a `code` mismatch", TextType.TEXT)
        with self.assertRaises(TypeError):
            output = split_nodes_delimiter([node], "`", TextType.BOLD)

    def test_invalid_delimiter(self):
        node = TextNode("Empty Delimiter", TextType.TEXT)
        with self.assertRaises(ValueError):
            output = split_nodes_delimiter([node], None, TextType.CODE)

if __name__ == "__main__":
    unittest.main()
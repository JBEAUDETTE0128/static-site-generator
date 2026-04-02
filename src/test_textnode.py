import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_type_ineq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_text_ineq(self):
        node = TextNode("This is node one", TextType.BOLD)
        node2 = TextNode("This is node two", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_ineq(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://test.org")
        self.assertNotEqual(node, node2)

    def test_url_ineq_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://test.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
if __name__ == "__main__":
    unittest.main()
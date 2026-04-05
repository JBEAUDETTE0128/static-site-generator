import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        output = node.to_html()
        expected = '<a href="https://www.google.com" >Click me!</a>'
        self.assertEqual(output, expected)

    def test_no_tag(self):
        node = LeafNode(None, "No tag", None)
        output = node.to_html()
        expected = "No tag"
        self.assertEqual(output, expected)

    def test_no_value(self):
        node = LeafNode(None, None, None)
        with self.assertRaises(ValueError):
            output = node.to_html()
        

if __name__ == "__main__":
    unittest.main()
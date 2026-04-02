import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        prop_dict = {
            "href": "https://www.google.com",
            "target": "_blank",
            "test_key": "test_value"
        }
        node = HTMLNode(None, None, None, prop_dict)
        output = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank" test_key="test_value" '
        self.assertEqual(output, expected)
    
    def test_props_to_html_empty(self):
        node = HTMLNode()
        output = node.props_to_html()
        expected = ""
        self.assertEqual(output, expected)

    def test_repr(self):
        node = HTMLNode("tag", "value", None, None)
        output = node.__repr__()
        expected = f'HTMLNode(tag, value, None, None)'
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()
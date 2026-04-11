import unittest

from extracttitle import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_hello(self):
        md = "# Hello"
        output = extract_title(md)
        expected = "Hello"
        self.assertEqual(output, expected)

    def test_hello_extra_space(self):
        md = "#            Hello              "
        output = extract_title(md)
        expected = "Hello"
        self.assertEqual(output, expected)

    def test_no_header_one(self):
        md = "Hello"
        with self.assertRaises(ValueError):
            output = extract_title(md)

    def test_inverted(self):
        md = """
###### Inverted

##### Markdown

#### Block

### Extraction

## Test

# Header
"""
        output = extract_title(md)
        expected = "Header"
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()
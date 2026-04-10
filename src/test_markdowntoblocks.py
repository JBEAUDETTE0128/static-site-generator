import unittest

from markdowntoblocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_mtb_trailing_space_lines(self):
            md = """

    


This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

    
    
    
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_mtb_extra_lines(self):
            md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line




- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
        
        def test_mtb_markdown_not_string(self):
            md = True
            with self.assertRaises(TypeError):
                blocks = markdown_to_blocks(md)
        
        def test_mtb_none(self):
            md = None
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, [])

        def test_mtb_empty(self):
            md = ""
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, [])

        def test_mtb_only_whitespace(self):
            md = """

    

    
    
            """
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, [])

if __name__ == "__main__":
    unittest.main()
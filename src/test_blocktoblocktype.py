import unittest

from blocktoblocktype import block_to_block_type
from blocktype import BlockType

class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        output = block_to_block_type("###### T")
        expected = BlockType.HEADING
        self.assertEqual(output, expected)

    def test_not_heading_extra_delimiters(self):
        output = block_to_block_type("####### T")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_not_heading_only_delimiters(self):
        output = block_to_block_type("######")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_not_heading_no_text(self):
        output = block_to_block_type("#######  ")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_not_heading_no_delimiters(self):
        output = block_to_block_type("Test")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_not_heading_no_space(self):
        output = block_to_block_type("######Test")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_code(self):
        output = block_to_block_type("```\nCode Block\n```")
        expected = BlockType.CODE
        self.assertEqual(output, expected)

    def test_not_code_no_start_ticks(self):
        output = block_to_block_type("Not Code Block\n```")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_not_code_no_end_ticks(self):
        output = block_to_block_type("```\nNot Code Block")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_quote(self):
        output = block_to_block_type(">quote\n> testing\n> lines")
        expected = BlockType.QUOTE
        self.assertEqual(output, expected)

    def test_not_quote_extra_space(self):
        output = block_to_block_type(">  not quote\n> testing\n> lines")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_not_quote_wrong_delimiter(self):
        output = block_to_block_type("> not quote\n> testing\n# lines")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_unordered_list(self):
        output = block_to_block_type("- unordered\n- list\n- lines")
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(output, expected)

    def test_not_unordered_list_no_space(self):
        output = block_to_block_type("-not unordered\n-list\n-lines")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_not_unordered_list_wrong_delimiter(self):
        output = block_to_block_type("- not unordered\n# list\n- lines")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_ordered_list(self):
        output = block_to_block_type("1. ordered\n2. list\n3. lines")
        expected = BlockType.ORDERED_LIST
        self.assertEqual(output, expected)

    def test_not_ordered_list_no_space(self):
        output = block_to_block_type("1.not ordered\n2.list\n3.lines")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_not_ordered_list_no_period(self):
        output = block_to_block_type("1 not ordered\n2 list\n3 lines")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

    def test_not_ordered_list_wrong_index(self):
        output = block_to_block_type("A. not ordered\nB. list\nC. lines")
        expected = BlockType.PARAGRAPH
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()
import unittest

from markdowntohtmlnode import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_mix(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_one(self):
        md = """
# Heading One
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading One</h1></div>",
        )

    def test_heading_two(self):
        md = """
## Heading Two
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Heading Two</h2></div>",
        )

    def test_heading_three(self):
        md = """
### Heading Three
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Heading Three</h3></div>",
        )

    def test_heading_four(self):
        md = """
#### Heading Four
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>Heading Four</h4></div>",
        )

    def test_heading_five(self):
        md = """
##### Heading Five
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5>Heading Five</h5></div>",
        )

    def test_heading_six(self):
        md = """
###### Heading Six
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>Heading Six</h6></div>",
        )

    def test_quote_spaces(self):
        md = """
> Quote
> Block
> Test
> With
> Spaces
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Quote\nBlock\nTest\nWith\nSpaces</blockquote></div>",
        )

    def test_quote_no_spaces(self):
        md = """
>Quote
>Block
>Test
>Without
>Spaces
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Quote\nBlock\nTest\nWithout\nSpaces</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- Unordered
- List
- Block
- Test
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Unordered</li><li>List</li><li>Block</li><li>Test</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. Ordered
2. List
3. Block
4. Test
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Ordered</li><li>List</li><li>Block</li><li>Test</li></ol></div>",
        )

    def test_suite_blocks_with_inline(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

```
This is text that _should_ remain
the **same** even with inline stuff
```

1. **Bold**
2. _Italic_

- **Bold**
- _Italic_

> **Bold**
> _Italic_

### **Bold**
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre><ol><li><b>Bold</b></li><li><i>Italic</i></li></ol><ul><li><b>Bold</b></li><li><i>Italic</i></li></ul><blockquote><b>Bold</b>\n<i>Italic</i></blockquote><h3><b>Bold</b></h3></div>",
        )
if __name__ == "__main__":
    unittest.main()
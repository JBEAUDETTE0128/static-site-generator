import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_family_tree(self):
        one_node_one = LeafNode("c", "grandchild one one")
        one_node_two = LeafNode("d", "grandchild one two")
        two_node_one = LeafNode("b", "grandchild two one")
        two_node_two = LeafNode("a", "grandchild two two")
        root_node_one = ParentNode("test", [one_node_one, one_node_two])
        root_node_two = ParentNode("span", [two_node_one, two_node_two])
        root_node = ParentNode("div", [root_node_one, root_node_two])
        output = root_node.to_html()
        expected = "<div><test><c>grandchild one one</c><d>grandchild one two</d></test><span><b>grandchild two one</b><a>grandchild two two</a></span></div>"
        self.assertEqual(output, expected)

    def test_to_html_no_children(self):
        defective_node = ParentNode("tag", None, None)
        with self.assertRaises(ValueError) as ve:
            output = defective_node.to_html()
        self.assertEqual(str(ve.exception), "ParentNode not assigned children nodes")
    
    def test_to_html_no_tag(self):
        test_node = LeafNode("test", "test value")
        defective_node = ParentNode(None, test_node, None)
        with self.assertRaises(ValueError) as ve:
            output = defective_node.to_html()
        self.assertEqual(str(ve.exception), "ParentNode not assigned a tag")

    def test_to_html_with_props(self):
        grandchild_node = LeafNode("b", "grandchild_value", {"gch": "url_gch"})
        child_node = ParentNode("span", [grandchild_node], {"ch": "url_ch"})
        parent_node = ParentNode("div", [child_node], {"root": "url_root"})
        self.assertEqual(
            parent_node.to_html(),
            '<div root="url_root" ><span ch="url_ch" ><b gch="url_gch" >grandchild_value</b></span></div>',
        )

if __name__ == "__main__":
    unittest.main()
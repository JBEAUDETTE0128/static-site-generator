import unittest

from textnode import TextNode
from texttype import TextType

from splitnodes import split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )       
        output = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(output, expected)

    def test_split_nodes_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_none_link(self):
        with self.assertRaises(ValueError):
            output = split_nodes_link(None)

    def test_none_image(self):
        with self.assertRaises(ValueError):
            output = split_nodes_image(None)

    def test_none_in_list_link(self):
        old_nodes = [
            TextNode("TestOne", TextType.TEXT),
            None,
            TextNode("TestTwo", TextType.TEXT),
        ]
        with self.assertRaises(ValueError):
            output = split_nodes_link(old_nodes)

    def test_none_in_list_image(self):
        old_nodes = [
            TextNode("TestOne", TextType.TEXT),
            None,
            TextNode("TestTwo", TextType.TEXT),
        ]
        with self.assertRaises(ValueError):
            output = split_nodes_image(old_nodes)

    def test_all_text_link(self):
        node = [TextNode("TestOne", TextType.TEXT)]
        output = split_nodes_link(node)
        self.assertListEqual(node, output)

    def test_all_text_image(self):
        node = [TextNode("TestOne", TextType.TEXT)]
        output = split_nodes_image(node)
        self.assertListEqual(node, output)

    def test_no_split_link(self):
        node = [TextNode("CodeTest", TextType.CODE)]
        output = split_nodes_link(node)
        self.assertListEqual(node, output)

    def test_no_split_image(self):
        node = [TextNode("CodeTest", TextType.CODE)]
        output = split_nodes_link(node)
        self.assertListEqual(node, output)

    def test_duplicate_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )       
        output = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertListEqual(output, expected)

    def test_duplicate_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and again ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and again ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
 
    def test_initial_link(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )       
        output = split_nodes_link([node])
        expected = [
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(output, expected)

    def test_initial_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_empty_string_link(self):
        nodes = [
            TextNode("", TextType.TEXT),
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT,),
            TextNode("", TextType.TEXT)
        ]    
        output = split_nodes_link(nodes)
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(output, expected)

    def test_empty_string_image(self):
        nodes = [
            TextNode("", TextType.TEXT),
            TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            TextNode("", TextType.TEXT),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
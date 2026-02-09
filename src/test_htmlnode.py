from htmlnode import ParentNode, LeafNode
import unittest

class TestTextNode(unittest.TestCase):
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

    def test_to_html_with_grandchildren_and_props(self):
        grandchild_node = LeafNode("b", "grandchild", {"style":"font_family=monserat"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b style="font_family=monserat">grandchild</b></span></div>',
        )

    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("span", "child")
        grandchild_node = LeafNode("b", "bold")
        grandchild_node2 = LeafNode("b", "bold2")
        child_node2 = ParentNode("p", [grandchild_node, grandchild_node2])
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><p><b>bold</b><b>bold2</b></p></div>")

if __name__ == "__main__":
    unittest.main()
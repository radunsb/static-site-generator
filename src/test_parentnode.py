import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
	def test_basic_parent_node(self):
		node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
		self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

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
	def test_to_html_with_no_children(self):
		node = ParentNode("div", [])
		self.assertRaises(ValueError, node.to_html)

	def test_to_html_no_tag(self):
		child_node = LeafNode("b", "child")
		parent_node = ParentNode(None, [child_node])
		self.assertRaises(ValueError, parent_node.to_html)


if __name__ == "__main__":
	unittest.main()

import unittest

from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
		self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
	def test_leaf_no_value(self):
		node = LeafNode(None, None)
		self.assertRaises(ValueError, node.to_html)
	def test_leaf_no_tag(self):
		node = LeafNode(value="Hello", tag=None)
		self.assertEqual(node.to_html(), "Hello")

if __name__ == "__main__":
	unittest.main()

import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_neq(self):
		node = TextNode("This is a text node", TextType.BOLD, url="12345")
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node, node2)

	def test_repr(self):
		node = TextNode("This is a text node", TextType.ITALIC, url="12345.com")
		self.assertEqual(node.__repr__(), "TextNode(This is a text node, italic, 12345.com)")

	def test_repr_nourl(self):
		node = TextNode("This is a text node", TextType.ITALIC)
		self.assertEqual(node.__repr__(), "TextNode(This is a text node, italic, None)")


if __name__ == "__main__":
	unittest.main()

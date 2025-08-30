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
	
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = node.text_node_to_html_node()
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")

	def test_italic(self):
		node = TextNode("This is an italic node", TextType.ITALIC)
		html_node = node.text_node_to_html_node()
		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "This is an italic node")

	def test_link(self):
		node = TextNode("This is a link node", TextType.LINK, "https://google.com")
		html_node = node.text_node_to_html_node()
		self.assertEqual(html_node.tag, "a")
		self.assertEqual(html_node.value, "This is a link node")
		self.assertEqual(html_node.props["href"], "https://google.com")

if __name__ == "__main__":
	unittest.main()

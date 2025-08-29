import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
	def test_one_prop_to_html(self):
		node = HTMLNode(props={"href": "https://www.google.com"})
		self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\"")
	def test_no_prop_to_html(self):
		node=HTMLNode()
		self.assertEqual(node.props_to_html(), "")
	def test_two_props_to_html(self):
		node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
		self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
	def test_print_nothing(self):
		node = HTMLNode()
		self.assertEqual(node.__repr__(), "HTMLNode(\nNone, \nNone, \nNone, \nNone, \n)")
	def test_print_children(self):
		child1 = HTMLNode(tag="p", value="Hello There")
		child2 = HTMLNode(tag="div")
		child3 = HTMLNode()
		parent = HTMLNode(tag="div", children=[child1, child2, child3])
		self.assertEqual(parent.__repr__(), "HTMLNode(\ndiv, \nNone, \n[p, div, None], \nNone, \n)")
	def test_print_props(self):
		node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
		self.assertEqual(node.__repr__(), "HTMLNode(\nNone, \nNone, \nNone, \n href=\"https://www.google.com\" target=\"_blank\", \n)")

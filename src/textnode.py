from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
	TEXT = "text"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode():

	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		return self.text == other.text and self.text_type == other.text_type and self.url == other.url

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
	
	def text_node_to_html_node(self):
		match(self.text_type):
			case TextType.TEXT:
				return LeafNode(tag=None, value=self.text)
			case TextType.ITALIC:
				return LeafNode(tag="i", value=self.text)
			case TextType.BOLD:
				return LeafNode(tag="b", value=self.text)
			case TextType.CODE:
				return LeafNode(tag="code", value=self.text)
			case TextType.LINK:
				return LeafNode(tag="a", value=self.text, props={"href": self.url})
			case TextType.IMAGE:
				return LeafNode(tag="img", value="", props={"src": self.url, "alt": self.text})
			case _:
				raise Exception("Text node is of an unsupported type")

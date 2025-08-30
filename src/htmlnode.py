

class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
	
	def to_html(self):
		raise NotImplementedError("to_html not implemented")

	def props_to_html(self):
		to_return = ""
		if not self.props:
			return to_return
		for k, v in self.props.items():
			to_return += " " + k + "=\"" + v + "\""
		return to_return

	def __repr__(self):
		if not self.children:
			child_print=None
		else:
			child_tags = list(map(lambda child: child.tag if child.tag else "None", self.children))
			child_print = "[" + ", ".join(child_tags) + "]"
		prop_print = self.props_to_html()
		if(prop_print == ""): prop_print = None
		return f"HTMLNode(\n{self.tag}, \n{self.value}, \n{child_print}, \n{prop_print}, \n)"
		

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, children=None, props=props)

	def to_html(self):
		if not self.value:
			raise ValueError("Leaf node must have a value")
		if not self.tag:
			return self.value
		else:
			return "<" + self.tag + self.props_to_html() + ">" + self.value + "</" + self.tag + ">"

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)
	
	def to_html(self):
		if not self.tag:
			raise ValueError("Parent node must have a tag")
		if not self.children or len(self.children) < 1:
			raise ValueError("Parent node must have children")
		else:
			to_return = "<" + self.tag + ">"
			for child in self.children:
				to_return += child.to_html()
			to_return += "</" + self.tag + ">"
			return to_return


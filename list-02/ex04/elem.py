#!/usr/bin/python3


class Text(str):
	def __str__(self):
		return super().__str__().replace('"', '&quot;').replace('>', '&gt;').replace('<', '&lt;').replace('\n', '\n<br />\n')
class Elem:

	def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
		self.tag = tag
		self.attr = attr
		self.tag_type = tag_type
		self.content = []
	 
		if not self.check_type(content) and content is not None:
			raise Elem.ValidationError
		elif content:
			self.add_content(content)                  

	def __str__(self):
					   
		if self.tag_type == 'double':
			result = f"<{self.tag}>{self.__make_content()}</{self.tag}>"
			
		elif self.tag_type == 'simple':
			result = f"<{self.tag}{self.__make_attr()}/>"
		return result

	def __make_attr(self):
		result = ''
		for pair in sorted(self.attr.items()):
			result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
		return result

	def __make_content(self):
		if len(self.content) == 0:
			return ''
		result = '\n'
		for elem in self.content:
			result += '  ' + str(elem).replace('\n','\n  ') + '\n'
		return result

	def add_content(self, content):
		if not Elem.check_type(content):
			raise Elem.ValidationError
		if type(content) == list:
			self.content += [elem for elem in content if elem != Text('')]
		elif content != Text(''):
			self.content.append(content)
	class ValidationError(Exception):
		pass
   
	@staticmethod
	def check_type(content):
		return (isinstance(content, Elem) or type(content) == Text or
				(type(content) == list and all([type(elem) == Text or
												isinstance(elem, Elem)
												for elem in content])))


if __name__ == '__main__':
	elem = Elem(tag = "html", content=[Elem(tag="head", content=
										   Elem(tag="title", content=Text("'Hello Ground!'"))), 
											  Elem(tag="body", content=[
												   Elem(tag="h1", content=Text("'Oh no, not again!'")), 
													   Elem(tag="img", attr={"src":"http://i.imgur.com/pfp3T.jpg"}, tag_type='simple')])])
	print(elem)
	
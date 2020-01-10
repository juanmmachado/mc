import xml.parsers.expat
from TS import TS
from ParserGraphML import ParserGraphML

class ParserGraphML_yEd(ParserGraphML):
	def __init__(self):
		ParserGraphML.__init__(self)

	def char_data(self, data):
		tagActual = self.getTags().pop()
		self.getTags().append(tagActual)
		if (tagActual == "y:NodeLabel"):
			self.setNombreActual(data)
		elif (tagActual == "y:EdgeLabel"):
			self.setAccionActual(data)

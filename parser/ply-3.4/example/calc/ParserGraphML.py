import xml.parsers.expat
from TS import TS

class ParserGraphML(object):
	def __init__(self):
		self.__idActual = ""
		self.__nombreActual = ""
		self.__tags = []
		self.__parser = xml.parsers.expat.ParserCreate()
		self.__parser.StartElementHandler = self.start_element
		self.__parser.EndElementHandler = self.end_element
		self.__parser.CharacterDataHandler = self.char_data
	
	def start_element(self, name, attrs):
		self.__tags.append(name)
		if (name == "node"):
			self.__idActual = attrs['id']
		elif (name == "edge"):
			self.__ts.agregarTransicionId(attrs['source'], attrs['target'])

	def end_element(self, name):
		self.__tags.pop()
		if (name == "node"):
			if (self.__nombreActual == ""):
				self.__nombreActual = self.__idActual
			if (self.__nombreActual.find("INI_") == 0):
				self.__ts.agregarEstadoInicial(self.__idActual, self.__nombreActual[4:])
			else:
				self.__ts.agregarEstado(self.__idActual, self.__nombreActual)
			self.__idActual = ""
			self.__nombreActual = ""
	
	def char_data(self, data):
		tagActual = self.__tags.pop()
		self.__tags.append(tagActual)
		if (tagActual == "y:NodeLabel"):
			self.__nombreActual = data

	def parsearTS(self, arch):
		self.__ts = TS([], [])
		try:
			self.__parser.ParseFile(open(arch, "r"))
		except:
			print "ERROR: No se pudo abrir el archivo graphml."
		return self.__ts

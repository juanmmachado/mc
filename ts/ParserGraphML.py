import xml.parsers.expat
from TS import TS

class ParserGraphML(object):
	def __init__(self):
		self.__idActual = ""
		self.__nombreActual = ""
		self.__sourceActual = ""
		self.__targetActual = ""
		self.__accionActual = ""
		self.__tags = []
		self.__parser = xml.parsers.expat.ParserCreate()
		self.__parser.StartElementHandler = self.start_element
		self.__parser.EndElementHandler = self.end_element
		self.__parser.CharacterDataHandler = self.char_data
	
	def setIdActual(self, idActual):
		self.__idActual = idActual

	def setNombreActual(self, nombreActual):
		self.__nombreActual = nombreActual

	def setSourceActual(self, sourceActual):
		self.__sourceActual = sourceActual

	def setTargetActual(self, targetActual):
		self.__targetActual = targetActual

	def setAccionActual(self, accionActual):
		self.__accionActual = accionActual

	def setTags(self, tags):
		self.__tags = tags

	def getIdActual(self):
		return self.__idActual

	def getNombreActual(self):
		return self.__nombreActual

	def getSourceActual(self):
		return self.__sourceActual

	def getTargetActual(self):
		return self.__targetActual

	def getAccionActual(self):
		return self.__accionActual
	
	def getTags(self):
		return self.__tags

	def start_element(self, name, attrs):
		self.__tags.append(name)
		if (name == "node"):
			self.__idActual = int((attrs['id'])[1:])
		elif (name == "edge"):
			self.__sourceActual = int(attrs['source'][1:])
			self.__targetActual = int(attrs['target'][1:])

	def end_element(self, name):
		self.__tags.pop()
		if (name == "node"):
			if (self.__nombreActual.find("INI_") == 0):
				self.__ts.agregarEstadoInicial(self.__idActual, (self.__nombreActual[4:]).split(','))
			else:
				self.__ts.agregarEstado(self.__idActual, self.__nombreActual.split(','))
			self.__idActual = ""
			self.__nombreActual = ""
		elif (name == "edge"):
			self.__ts.agregarTransicionId(self.__sourceActual, self.__accionActual, self.__targetActual)
			self.__sourceActual = ""
			self.__targetActual = ""
			self.__accionActual = ""

	
	def char_data(self, data):
		None
	
	def parsearTS(self, arch):
		self.__ts = TS([], [])
		try:
			self.__parser.ParseFile(open(arch, "r"))
		except:
			print "ERROR: No se pudo parsear el archivo", arch
		return self.__ts

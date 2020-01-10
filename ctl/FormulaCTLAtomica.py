from FormulaCTL import FormulaCTL
from TS import TS

class FormulaCTLAtomica(FormulaCTL):
	"Formula LTL atomica"
	def __init__(self, nombre):
		self.__nombre = nombre
		self.__sat = None

	def normalizar(self):
		return self
	
	def getSat(self, ts):
		"Devuelve los estados de ts que la satisfacen"
		self.__sat = ts.getSatAtomica(self.__nombre)
		return self.__sat[:]

	def verificaAtomica(self, nombre):
		"Se compara con la proposicion nombre o True"
		return (self.__nombre == nombre) or (nombre == "TRUE")

	def imprimirFormula(self):
		return self.__nombre
	
	def getAtrSat(self):
		"Devuelve los estados de ts que la satisfacen (guardados previamente)"
		return self.__sat[:]
	
	def setAtrSat(self, sat):
		"Guarda los estados de ts que la satisfacen"
		self.__sat = sat

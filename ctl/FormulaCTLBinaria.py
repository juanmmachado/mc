from FormulaCTL import FormulaCTL

class FormulaCTLBinaria(FormulaCTL):
	"Formula CTL con conectivo binario"
	def __init__(self, sfizq, sfder):
		self.__subFormulaIzq = sfizq
		self.__subFormulaDer = sfder
		self.__sat = None

	def getSubFormulaIzq(self):
		"Devuelve la subformula izquierda"
		return self.__subFormulaIzq

	def getSubFormulaDer(self):
		"Devuelve la subformula derecha"
		return self.__subFormulaDer
		
	def isTrue(self):
		return False

	def normalizar(self):
		self.__subFormulaIzq = self.__subFormulaIzq.normalizar()
		self.__subFormulaDer = self.__subFormulaDer.normalizar()
		return self
	
	def getSubFormulas(self):
		"Devuelve el conjunto de todas las subformulas"
		sfs = self.__subFormulaIzq.getSubFormulas()
		sfs2 = self.__subFormulaDer.getSubFormulas()
		for sf in sfs2:
			if sf not in sfs:
				sfs.append(sf)
		sfs.append(self)
		return sfs

	def verificaAtomica(self, nombre):
		return (nombre == "TRUE")

	def getAtrSat(self):
		"Devuelve los estados de ts que la satisfacen (guardados previamente)"
		return self.__sat[:]
	
	def setAtrSat(self, sat):
		"Guarda los estados de ts que la satisfacen"
		self.__sat = sat

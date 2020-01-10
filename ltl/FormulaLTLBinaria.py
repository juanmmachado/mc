from FormulaLTL import FormulaLTL
from Herramientas import Herramientas

class FormulaLTLBinaria(FormulaLTL):
	"Formula LTL con conectivo binario"
	def __init__(self, sfizq, sfder):
		self.__subFormulaIzq = sfizq
		self.__subFormulaDer = sfder
	
	def getSubFormulaIzq(self):
		"Devuelve la subformula izquierda."
		return self.__subFormulaIzq

	def getSubFormulaDer(self):
		"Devuelve la subformula derecha."
		return self.__subFormulaDer
		
	def isTrue(self):
		return False
	
	def normalizar(self):
		self.__subFormulaIzq = self.__subFormulaIzq.normalizar()
		self.__subFormulaDer = self.__subFormulaDer.normalizar()
		return self
	
	def obtenerNombreAtomica(self):
		"Al no ser una formula atomica devuelve el string vacio."
		return ""
	
	def obtenerNombreNegacionAtomica(self):
		"Al no ser una negacion de atomica devuelve el string vacio."
		return ""
	
	def getAtomicas(self):
		"Devuelve el conjunto de todas las subformulas atomicas."
		h = Herramientas()
		return h.combinarListas(self.__subFormulaIzq.getAtomicas(), self.__subFormulaDer.getAtomicas())
	
	def getSubFormulas(self):
		"Devuelve el conjunto de todas las subformulas."
		sfs = self.__subFormulaIzq.getSubFormulas()
		sfs2 = self.__subFormulaDer.getSubFormulas()
		for sf in sfs2:
			if sf not in sfs:
				sfs.append(sf)
		sfs.append(self)
		return sfs
		
	def getSubFormulasPositivas(self):
		"Devuelve el conjunto de todas las subformulas cuyo conectivo principal no es una negacion."
		sfs = self.__subFormulaIzq.getSubFormulasPositivas()
		sfs2 = self.__subFormulaDer.getSubFormulasPositivas()
		for sf in sfs2:
			if sf not in sfs:
				sfs.append(sf)
		sfs.append(self)
		return sfs

	def verificaAtomica(self, nombre):
		return (nombre == "TRUE")

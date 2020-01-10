from FormulaLTL import FormulaLTL
from Herramientas import Herramientas

class FormulaLTLBinaria(FormulaLTL):
	"Formula LTL con conectivo binario"
	def __init__(self, sfizq, sfder):
		self.__subFormulaIzq = sfizq
		self.__subFormulaDer = sfder
		
	def getSubFormulaIzq(self):
		return self.__subFormulaIzq

	def getSubFormulaDer(self):
		return self.__subFormulaDer
		
	def isTrue(self):
		return False
	
	def getAtomicas(self):
		h = Herramientas()
		return h.combinarListas(self.__subFormulaIzq.getAtomicas(), self.__subFormulaDer.getAtomicas())
	
	def getSubFormulas(self):
		sfs = self.__subFormulaIzq.getSubFormulas()
		sfs2 = self.__subFormulaDer.getSubFormulas()
		for sf in sfs2:
			if sf not in sfs:
				sfs.append(sf)
		sfs.append(self)
		return sfs
		
	def getSubFormulasPositivas(self):
		sfs = self.__subFormulaIzq.getSubFormulasPositivas()
		sfs2 = self.__subFormulaDer.getSubFormulasPositivas()
		for sf in sfs2:
			if sf not in sfs:
				sfs.append(sf)
		sfs.append(self)
		return sfs

	def verificaAtomica(self, nombre):
		return (nombre == "TRUE")

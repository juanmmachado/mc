from FormulaLTL import FormulaLTL

class FormulaLTLUnaria(FormulaLTL):
	"Formula LTL con conectivo unario"
	def __init__(self, sf):
		self.__subFormula = sf

	def getAtomicas(self):
		return self.__subFormula.getAtomicas()

	def getSubFormula(self):
		return self.__subFormula

	def isTrue(self):
		return False

	def getSubFormulas(self):
		sfs = self.__subFormula.getSubFormulas()
		sfs.append(self)
		return sfs
	
	def getSubFormulasPositivas(self):
		sfs = self.__subFormula.getSubFormulasPositivas()
		sfs.append(self)
		return sfs

	def verificaAtomica(self, nombre):
		return (nombre == "TRUE")

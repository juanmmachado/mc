from FormulaLTLAtomica import FormulaLTLAtomica

class FormulaLTLTrue(FormulaLTLAtomica):
	"Formula LTL True"
	def __init__(self):
		FormulaLTLAtomica.__init__(self, "TRUE")

	def isTrue(self):
		return True
	
	def getSubFormulasPositivas(self):
		"Devuelve el conjunto de todas las subformulas cuyo conectivo principal no es una negacion."
		return [self]

	def compararFormula(self, f):
		"Devuelve True si la formula es igual a f."
		if isinstance(f, FormulaLTLTrue):
			return True
		else:
			return False

	def verificaAtomica(self, nombre):
		return (nombre == "TRUE")

	def verificarTraza(self, traza):
		return traza

	def verificarTrazaV(self, traza):
		if traza == []:
			return traza
		return [traza[0]]

	def verificarTrazaF(self, traza):
		return traza
	
	def verificarTrazaVTrans(self, traza):
		if traza == []:
			return traza
		return [traza[0]]

	def verificarTrazaFTrans(self, traza):
		return traza
		
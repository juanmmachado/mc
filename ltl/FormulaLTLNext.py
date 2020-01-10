from FormulaLTLUnaria import FormulaLTLUnaria

class FormulaLTLNext(FormulaLTLUnaria):
	"Formula LTL (next)"
	def __init__(self, sf):
		FormulaLTLUnaria.__init__(self, sf)
	
	def obtenerNombreNegacionAtomica(self):
		"Al no ser una negacion de atomica devuelve el string vacio."
		return ""
	
	def compararFormula(self, f):
		"Devuelve True si la formula es igual a f."
		if isinstance(f, FormulaLTLNext):
			return self.getSubFormula().compararFormula(f.getSubFormula())
		else:
			return False

	def imprimirFormula(self):
		return ("(NEXT " + self.getSubFormula().imprimirFormula() + ")")
		
	def verificarTrazaV(self, traza):
		return [traza[0]] + self.getSubFormula().verificarTrazaVTrans(traza[1:])

	def verificarTrazaF(self, traza):
		return [traza[0]] + self.getSubFormula().verificarTrazaFTrans(traza[1:])

	def verificarTrazaVTrans(self, traza):
		return [traza[0]] + self.getSubFormula().verificarTrazaVTrans(traza[1:])

	def verificarTrazaFTrans(self, traza):
		return [traza[0]] + self.getSubFormula().verificarTrazaFTrans(traza[1:])

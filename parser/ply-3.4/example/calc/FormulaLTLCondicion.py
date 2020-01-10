from FormulaLTLBinaria import FormulaLTLBinaria

class FormulaLTLCondicion(FormulaLTLBinaria):
	"Formula LTL (condicion)"
	def __init__(self, sfizq, sfder):
		FormulaLTLBinaria.__init__(self, sfizq, sfder)
		
	def compararFormula(self, f):
		if isinstance(f, FormulaLTLCondicion):
			return (self.getSubFormulaIzq().compararFormula(f.getSubFormulaIzq()) and self.getSubFormulaDer().compararFormula(f.getSubFormulaDer()))
		else:
			return False

	def imprimirFormula(self):
		return ("(" + self.getSubFormulaIzq().imprimirFormula() + " THEN " + self.getSubFormulaDer().imprimirFormula() + ")")
		
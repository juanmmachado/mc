from FormulaLTLBinaria import FormulaLTLBinaria

class FormulaLTLUntil(FormulaLTLBinaria):
	"Formula LTL (until)"
	def __init__(self, sfizq, sfder):
		FormulaLTLBinaria.__init__(self, sfizq, sfder)
	
	def compararFormula(self, f):
		if isinstance(f, FormulaLTLUntil):
			return (self.getSubFormulaIzq().compararFormula(f.getSubFormulaIzq()) and self.getSubFormulaDer().compararFormula(f.getSubFormulaDer()))
		else:
			return False

	def imprimirFormula(self):
		return ("(" + self.getSubFormulaIzq().imprimirFormula() + " UNTIL " + self.getSubFormulaDer().imprimirFormula() + ")")
		
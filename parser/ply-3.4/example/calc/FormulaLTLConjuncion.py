from FormulaLTLBinaria import FormulaLTLBinaria

class FormulaLTLConjuncion(FormulaLTLBinaria):
	"Formula LTL (conjuncion)"
	def __init__(self, sfizq, sfder):
		FormulaLTLBinaria.__init__(self, sfizq, sfder)
		
	def compararFormula(self, f):
		if isinstance(f, FormulaLTLConjuncion):
			return (self.getSubFormulaIzq().compararFormula(f.getSubFormulaIzq()) and self.getSubFormulaDer().compararFormula(f.getSubFormulaDer()))
		else:
			return False

	def imprimirFormula(self):
		return ("(" + self.getSubFormulaIzq().imprimirFormula() + " AND " + self.getSubFormulaDer().imprimirFormula() + ")")
		
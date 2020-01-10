from FormulaLTLBinaria import FormulaLTLBinaria

class FormulaLTLDisyuncion(FormulaLTLBinaria):
	"Formula LTL (disyuncion)"
	def __init__(self, sfizq, sfder):
		FormulaLTLBinaria.__init__(self, sfizq, sfder)
		
	def compararFormula(self, f):
	# idem valuacion
		if isinstance(f, FormulaLTLDisyuncion):
			return (self.getSubFormulaIzq().compararFormula(f.getSubFormulaIzq()) and self.getSubFormulaDer().compararFormula(f.getSubFormulaDer()))
		else:
			return False

	def imprimirFormula(self):
		return ("(" + self.getSubFormulaIzq().imprimirFormula() + " OR " + self.getSubFormulaDer().imprimirFormula() + ")")
		
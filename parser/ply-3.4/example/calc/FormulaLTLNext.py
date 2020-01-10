from FormulaLTLUnaria import FormulaLTLUnaria

class FormulaLTLNext(FormulaLTLUnaria):
	"Formula LTL (next)"
	def __init__(self, sf):
		FormulaLTLUnaria.__init__(self, sf)
	
	def compararFormula(self, f):
		if isinstance(f, FormulaLTLNext):
			return self.getSubFormula().compararFormula(f.getSubFormula())
		else:
			return False

	def imprimirFormula(self):
		return ("(NEXT " + self.getSubFormula().imprimirFormula() + ")")
		
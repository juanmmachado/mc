from FormulaLTLUnaria import FormulaLTLUnaria

class FormulaLTLEventually(FormulaLTLUnaria):
	"Formula LTL (eventually)"
	def __init__(self, sf):
		FormulaLTLUnaria.__init__(self, sf)
	
	def compararFormula(self, f):
		if isinstance(f, FormulaLTLEventually):
			return self.getSubFormula().compararFormula(f.getSubFormula())
		else:
			return False

	def imprimirFormula(self):
		return ("(EVENTUALLY " + self.getSubFormula().imprimirFormula() + ")")
		
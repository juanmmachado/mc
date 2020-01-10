from FormulaLTLUnaria import FormulaLTLUnaria

class FormulaLTLAlways(FormulaLTLUnaria):
	"Formula LTL (negacion)"
	def __init__(self, sf):
		FormulaLTLUnaria.__init__(self, sf)
	
	def compararFormula(self, f):
		if isinstance(f, FormulaLTLAlways):
			return self.getSubFormula().compararFormula(f.getSubFormula())
		else:
			return False

	def imprimirFormula(self):
		return ("(ALWAYS " + self.getSubFormula().imprimirFormula() + ")")
		
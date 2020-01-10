from FormulaLTLUnaria import FormulaLTLUnaria

class FormulaLTLNegacion(FormulaLTLUnaria):
	"Formula LTL (negacion)"
	def __init__(self, sf):
		FormulaLTLUnaria.__init__(self, sf)
	
	def getSubFormulasPositivas(self):
		return self.getSubFormula().getSubFormulasPositivas()

	def compararFormula(self, f):
		if isinstance(f, FormulaLTLNegacion):
			return self.getSubFormula().compararFormula(f.getSubFormula())
		else:
			return False

	def imprimirFormula(self):
		return ("(NOT " + self.getSubFormula().imprimirFormula() + ")")
		
from FormulaLTLUnaria import FormulaLTLUnaria
from FormulaLTLUntil import FormulaLTLUntil
from FormulaLTLTrue import FormulaLTLTrue

class FormulaLTLEventually(FormulaLTLUnaria):
	"Formula LTL (eventually)"
	def __init__(self, sf):
		FormulaLTLUnaria.__init__(self, sf)
	
	def obtenerNombreNegacionAtomica(self):
		"Al no ser una negacion de atomica devuelve el string vacio."
		return ""
	
	def compararFormula(self, f):
		"Devuelve True si la formula es igual a f."
		if isinstance(f, FormulaLTLEventually):
			return self.getSubFormula().compararFormula(f.getSubFormula())
		else:
			return False
	
	def normalizar(self):
		return FormulaLTLUntil(FormulaLTLTrue(),self.getSubFormula().normalizar())

	def imprimirFormula(self):
		return ("(EVENTUALLY " + self.getSubFormula().imprimirFormula() + ")")
		
from FormulaLTLUnaria import FormulaLTLUnaria
from FormulaLTLNegacion import FormulaLTLNegacion
from FormulaLTLUntil import FormulaLTLUntil
from FormulaLTLTrue import FormulaLTLTrue

class FormulaLTLAlways(FormulaLTLUnaria):
	"Formula LTL (always)"
	def __init__(self, sf):
		FormulaLTLUnaria.__init__(self, sf)
	
	def obtenerNombreNegacionAtomica(self):
		"Al no ser una negacion de atomica devuelve el string vacio."
		return ""
	
	def compararFormula(self, f):
		"Devuelve True si la formula es igual a f."
		if isinstance(f, FormulaLTLAlways):
			return self.getSubFormula().compararFormula(f.getSubFormula())
		else:
			return False

	def normalizar(self):
		return FormulaLTLNegacion(FormulaLTLUntil(FormulaLTLTrue(),FormulaLTLNegacion(self.getSubFormula()).normalizar()))
	
	def imprimirFormula(self):
		return ("(ALWAYS " + self.getSubFormula().imprimirFormula() + ")")
		
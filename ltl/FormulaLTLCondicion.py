from FormulaLTLBinaria import FormulaLTLBinaria
from FormulaLTLNegacion import FormulaLTLNegacion
from FormulaLTLConjuncion import FormulaLTLConjuncion

class FormulaLTLCondicion(FormulaLTLBinaria):
	"Formula LTL (condicion)"
	def __init__(self, sfizq, sfder):
		FormulaLTLBinaria.__init__(self, sfizq, sfder)
		
	def compararFormula(self, f):
		"Devuelve True si la formula es igual a f."
		if isinstance(f, FormulaLTLCondicion):
			return (self.getSubFormulaIzq().compararFormula(f.getSubFormulaIzq()) and self.getSubFormulaDer().compararFormula(f.getSubFormulaDer()))
		else:
			return False

	def normalizar(self):
		return FormulaLTLNegacion(FormulaLTLConjuncion(self.getSubFormulaIzq().normalizar(),FormulaLTLNegacion(self.getSubFormulaDer().normalizar())))
	
	def imprimirFormula(self):
		return ("(" + self.getSubFormulaIzq().imprimirFormula() + " THEN " + self.getSubFormulaDer().imprimirFormula() + ")")
		
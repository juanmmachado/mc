from FormulaLTLBinaria import FormulaLTLBinaria
from FormulaLTLNegacion import FormulaLTLNegacion
from FormulaLTLConjuncion import FormulaLTLConjuncion

class FormulaLTLDisyuncion(FormulaLTLBinaria):
	"Formula LTL (disyuncion)"
	def __init__(self, sfizq, sfder):
		FormulaLTLBinaria.__init__(self, sfizq, sfder)
		
	def compararFormula(self, f):
		"Devuelve True si la formula es igual a f."
		if isinstance(f, FormulaLTLDisyuncion):
			return (self.getSubFormulaIzq().compararFormula(f.getSubFormulaIzq()) and self.getSubFormulaDer().compararFormula(f.getSubFormulaDer()))
		else:
			return False
	
	def normalizar(self):
		return FormulaLTLNegacion(FormulaLTLConjuncion(FormulaLTLNegacion(self.getSubFormulaIzq()).normalizar(),FormulaLTLNegacion(self.getSubFormulaDer()).normalizar()))
	
	def imprimirFormula(self):
		return ("(" + self.getSubFormulaIzq().imprimirFormula() + " OR " + self.getSubFormulaDer().imprimirFormula() + ")")
		
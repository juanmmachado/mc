from FormulaCTLBinaria import FormulaCTLBinaria
from FormulaCTLNegacion import FormulaCTLNegacion
from FormulaCTLConjuncion import FormulaCTLConjuncion

class FormulaCTLDisyuncion(FormulaCTLBinaria):
	"Formula CTL (conjuncion)"
	def __init__(self, sfizq, sfder):
		FormulaCTLBinaria.__init__(self, sfizq, sfder)

	def normalizar(self):
		return FormulaCTLNegacion(FormulaCTLConjuncion(FormulaCTLNegacion(self.getSubFormulaIzq()).normalizar(),FormulaCTLNegacion(self.getSubFormulaDer()).normalizar()))
		
	def imprimirFormula(self):
		return ("(" + self.getSubFormulaIzq().imprimirFormula() + " OR " + self.getSubFormulaDer().imprimirFormula() + ")")
		
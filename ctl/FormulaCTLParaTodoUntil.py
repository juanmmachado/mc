from FormulaCTLBinaria import FormulaCTLBinaria
from FormulaCTLConjuncion import FormulaCTLConjuncion
from FormulaCTLNegacion import FormulaCTLNegacion
from FormulaCTLExisteUntil import FormulaCTLExisteUntil
from FormulaCTLExisteAlways import FormulaCTLExisteAlways
from TS import TS

class FormulaCTLParaTodoUntil(FormulaCTLBinaria):
	"Formula CTL (para todo until)"
	def __init__(self, sfizq, sfder):
		FormulaCTLBinaria.__init__(self, sfizq, sfder)

	def normalizar(self):
		sfizq_norm = self.getSubFormulaIzq().normalizar() 
		sfder_norm = self.getSubFormulaDer().normalizar()
		return FormulaCTLConjuncion(FormulaCTLNegacion(FormulaCTLExisteUntil(FormulaCTLNegacion(sfder_norm), FormulaCTLConjuncion(FormulaCTLNegacion(sfizq_norm), FormulaCTLNegacion(sfder_norm)))), FormulaCTLNegacion(FormulaCTLExisteAlways(FormulaCTLNegacion(sfder_norm))))
	
	def imprimirFormula(self):
		return ("( PARATODO " + self.getSubFormulaIzq().imprimirFormula() + " UNTIL " + self.getSubFormulaDer().imprimirFormula() + ")")
		
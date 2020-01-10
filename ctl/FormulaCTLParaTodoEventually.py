from FormulaCTLUnaria import FormulaCTLUnaria
from FormulaCTLNegacion import FormulaCTLNegacion
from FormulaCTLExisteAlways import FormulaCTLExisteAlways
from TS import TS

class FormulaCTLParaTodoEventually(FormulaCTLUnaria):
	"Formula CTL (para todo eventually)"
	def __init__(self, sf):
		FormulaCTLUnaria.__init__(self, sf)
	
	def normalizar(self):
		return FormulaCTLNegacion(FormulaCTLExisteAlways(FormulaCTLNegacion(self.getSubFormula()).normalizar()))
	
	def imprimirFormula(self):
		return ("(PARATODO EVENTUALLY " + self.getSubFormula().imprimirFormula() + ")")
		
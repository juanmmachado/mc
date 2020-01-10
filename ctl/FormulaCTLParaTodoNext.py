from FormulaCTLUnaria import FormulaCTLUnaria
from FormulaCTLNegacion import FormulaCTLNegacion
from FormulaCTLExisteNext import FormulaCTLExisteNext
from TS import TS

class FormulaCTLParaTodoNext(FormulaCTLUnaria):
	"Formula CTL (para todo next)"
	def __init__(self, sf):
		FormulaCTLUnaria.__init__(self, sf)
	
	def normalizar(self):
		return FormulaCTLNegacion(FormulaCTLExisteNext(FormulaCTLNegacion(self.getSubFormula().normalizar())))
	
	def imprimirFormula(self):
		return ("(PARATODO NEXT " + self.getSubFormula().imprimirFormula() + ")")
		
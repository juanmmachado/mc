from FormulaCTLUnaria import FormulaCTLUnaria
from FormulaCTLNegacion import FormulaCTLNegacion
from FormulaCTLExisteUntil import FormulaCTLExisteUntil
from FormulaCTLTrue import FormulaCTLTrue
from TS import TS
from TSEstado import TSEstado

class FormulaCTLParaTodoAlways(FormulaCTLUnaria):
	"Formula CTL (para todo always)"
	def __init__(self, sf):
		FormulaCTLUnaria.__init__(self, sf)
	
	def normalizar(self):
		return FormulaCTLNegacion(FormulaCTLExisteUntil(FormulaCTLTrue(), FormulaCTLNegacion(self.getSubFormula()).normalizar()))
	
	def imprimirFormula(self):
		return ("(PARATODO ALWAYS " + self.getSubFormula().imprimirFormula() + ")")
		
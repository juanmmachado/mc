from FormulaCTLUnaria import FormulaCTLUnaria
from FormulaCTLExisteUntil import FormulaCTLExisteUntil
from FormulaCTLTrue import FormulaCTLTrue
from TS import TS
from TSEstado import TSEstado

class FormulaCTLExisteEventually(FormulaCTLUnaria):
	"Formula CTL (existe eventually)"
	def __init__(self, sf):
		FormulaCTLUnaria.__init__(self, sf)
	
	def normalizar(self):
		return FormulaCTLExisteUntil(FormulaCTLTrue(), self.getSubFormula().normalizar())
	
	def imprimirFormula(self):
		return ("(EXISTE EVENTUALLY " + self.getSubFormula().imprimirFormula() + ")")
		
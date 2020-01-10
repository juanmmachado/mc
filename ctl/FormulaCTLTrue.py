from FormulaCTLAtomica import FormulaCTLAtomica
from TS import TS

class FormulaCTLTrue(FormulaCTLAtomica):
	"Formula CTL True"
	def __init__(self):
		FormulaCTLAtomica.__init__(self, "TRUE")
	
	def getSat(self, ts):
		"Devuelve los estados de ts que la satisfacen"
		self.setAtrSat(ts.getEstados()[:])
		return self.getAtrSat()
	
	def verificaAtomica(self, nombre):
		"Se compara con la proposicion nombre o True"
		return (nombre == "TRUE")

	def imprimirFormula(self):
		return "TRUE"

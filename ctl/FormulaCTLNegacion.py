from FormulaCTLUnaria import FormulaCTLUnaria
from TS import TS

class FormulaCTLNegacion(FormulaCTLUnaria):
	"Formula CTL (negacion)"
	def __init__(self, sf):
		FormulaCTLUnaria.__init__(self, sf)
	
	def normalizar(self):
		sf_norm = self.getSubFormula().normalizar()
		if isinstance(sf_norm, FormulaCTLNegacion):
			f_norm = sf_norm.getSubFormula()
			return f_norm
		else:
			f_norm = FormulaCTLNegacion(sf_norm)
			return f_norm
		
	def getSat(self, ts):
		"Devuelve el conjunto de estados de ts que satisfacen la formula"
		# Se calcula el paso recursivo
		satSub = self.getSubFormula().getSat(ts)
		# Se calcula el complemento
		sat = ts.getEstados()[:]
		for estado in satSub:
			sat.remove(estado)
		self.setAtrSat(sat)
		return sat[:]
	
	def imprimirFormula(self):
		return ("(NOT " + self.getSubFormula().imprimirFormula() + ")")
		
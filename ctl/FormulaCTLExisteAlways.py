from FormulaCTLUnaria import FormulaCTLUnaria
from TS import TS
from TSEstado import TSEstado

class FormulaCTLExisteAlways(FormulaCTLUnaria):
	"Formula CTL (existe always)"
	def __init__(self, sf):
		FormulaCTLUnaria.__init__(self, sf)
	
	def getSat(self, ts):
		"Devuelve el conjunto de estados de ts que satisfacen la formula"
		# Considerando la formula E[]phi
		# Se obtiene el conjunto de estados que satisfacen phi
		sat = self.getSubFormula().getSat(ts)
		expand = ts.getEstados()[:]
		c = []
		# Se crea e inicializa un arreglo de ceros
		for s in expand:
			c.append(0)
		for s in sat:
			expand.remove(s)
			c[s.getId()] = len(ts.getPost(s))
		while expand != []:
			s2 = expand.pop()
			pre_s2 = ts.getPre(s2)
			for s in pre_s2:
				if s in sat:
					c[s.getId()] = c[s.getId()] - 1
					if c[s.getId()] == 0:
						sat.remove(s)
						expand.append(s)
		self.setAtrSat(sat)
		return sat[:]
	
	def imprimirFormula(self):
		return ("(EXISTE ALWAYS " + self.getSubFormula().imprimirFormula() + ")")
		
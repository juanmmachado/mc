class FormulaCTL(object):
	"Formula CTL"
	def getSat(self, ts):
		"Devuelve los estados de ts que la satisfacen"
		pass
	
	def normalizar(self):
		"Devuelve una formula equivalente normalizada."
		pass
	
	def perteneceLista(self, listaForms):
		"Devuelve True si pertenece a la lista listaForms"
		for f in listaForms:
			if self.compararFormula(f):
				return True
		return False
		
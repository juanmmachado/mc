from FormulaCTLUnaria import FormulaCTLUnaria
from TS import TS

class FormulaCTLExisteNext(FormulaCTLUnaria):
	"Formula CTL (existe next)"
	def __init__(self, sf):
		FormulaCTLUnaria.__init__(self, sf)
		
	def getSat(self, ts):
		"Devuelve el conjunto de estados de ts que satisfacen la formula"
		sat = []
		# Se calcula el paso recursivo
		satSub = self.getSubFormula().getSat(ts)
		# Se buscan los predecesores de todos los estados en el conjunto satSub
		estados = ts.getEstados()
		for estado in estados:
			posts = ts.getPost(estado)
			disjuntos = True
			i = 0
			fin = len(posts)
			while (i < fin) and disjuntos:
				if posts[i] in satSub:
					disjuntos = False
					sat.append(estado)
				i += 1
		self.setAtrSat(sat)
		return sat[:]
	
	def imprimirFormula(self):
		return ("(EXISTE NEXT " + self.getSubFormula().imprimirFormula() + ")")
		
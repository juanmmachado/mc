from FormulaCTLBinaria import FormulaCTLBinaria
from FormulaCTLNegacion import FormulaCTLNegacion
from FormulaCTLConjuncion import FormulaCTLConjuncion

class FormulaCTLCondicion(FormulaCTLBinaria):
	"Formula CTL (conjuncion)"
	def __init__(self, sfizq, sfder):
		FormulaCTLBinaria.__init__(self, sfizq, sfder)
	
	def normalizar(self):
		return FormulaCTLNegacion(FormulaCTLConjuncion(self.getSubFormulaIzq().normalizar(),FormulaCTLNegacion(self.getSubFormulaDer()).normalizar()))

	def getSat(self, ts):
		"Devuelve el conjunto de estados de ts que satisfacen la formula"
		# Se calculan los pasos recursivos
		satIzq = self.getSubFormulaIzq().getSat(ts)
		satDer = self.getSubFormulaDer().getSat(ts)
		# Se calcula la interseccion
		sat = satIzq[:]
		for estado in satDer:
			if estado not in satIzq:
				sat.append(estado)
		return sat
	
	def imprimirFormula(self):
		return ("(" + self.getSubFormulaIzq().imprimirFormula() + " AND " + self.getSubFormulaDer().imprimirFormula() + ")")
		
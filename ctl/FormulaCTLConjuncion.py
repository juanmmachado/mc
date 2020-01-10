from FormulaCTLBinaria import FormulaCTLBinaria

class FormulaCTLConjuncion(FormulaCTLBinaria):
	"Formula CTL (conjuncion)"
	def __init__(self, sfizq, sfder):
		FormulaCTLBinaria.__init__(self, sfizq, sfder)

	def getSat(self, ts):
		"Devuelve el conjunto de estados de ts que satisfacen la formula"
		# Se calculan los pasos recursivos
		satIzq = self.getSubFormulaIzq().getSat(ts)
		satDer = self.getSubFormulaDer().getSat(ts)
		# Se calcula la interseccion
		sat = []
		for estado in satDer:
			if estado in satIzq:
				sat.append(estado)
		self.setAtrSat(sat)
		return sat[:]
	
	def imprimirFormula(self):
		return ("(" + self.getSubFormulaIzq().imprimirFormula() + " AND " + self.getSubFormulaDer().imprimirFormula() + ")")
		
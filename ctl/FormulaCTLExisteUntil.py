from FormulaCTLBinaria import FormulaCTLBinaria
from TS import TS

class FormulaCTLExisteUntil(FormulaCTLBinaria):
	"Formula CTL (existe until)"
	def __init__(self, sfizq, sfder):
		FormulaCTLBinaria.__init__(self, sfizq, sfder)
	
	def getSat(self, ts):
		"Devuelve el conjunto de estados de ts que satisfacen la formula"
		# Considerando la formula phi_1 U phi_2
		# Se obtiene el conjunto de estados que satisface phi_2
		sat = self.getSubFormulaDer().getSat(ts)
		# Se obtiene el conjunto de estados que satisface phi_1
		sat_phi1 = self.getSubFormulaIzq().getSat(ts)
		expand = sat[:]
		# Se quitan los estados que satisfacen phi_2, ya que estos ya forman parte de la solucion
		for s in sat:
			if s in sat_phi1:
				sat_phi1.remove(s)
		# Se expande el conjunto solucion incluyendo los predecesores que satisfacen phi_1
		while expand != []:
			s2 = expand.pop()
			pre_s2 = ts.getPre(s2)
			for s in pre_s2:
				if s in sat_phi1:
					sat_phi1.remove(s)
					sat.append(s)
					expand.append(s)
		self.setAtrSat(sat)
		return sat[:]
	
	def imprimirFormula(self):
		return ("( EXISTE " + self.getSubFormulaIzq().imprimirFormula() + " UNTIL " + self.getSubFormulaDer().imprimirFormula() + ")")
		
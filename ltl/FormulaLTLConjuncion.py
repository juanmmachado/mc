from FormulaLTLBinaria import FormulaLTLBinaria

class FormulaLTLConjuncion(FormulaLTLBinaria):
	"Formula LTL (conjuncion)"
	def __init__(self, sfizq, sfder):
		FormulaLTLBinaria.__init__(self, sfizq, sfder)
		
	def compararFormula(self, f):
		"Devuelve True si la formula es igual a f."
		if isinstance(f, FormulaLTLConjuncion):
			return (self.getSubFormulaIzq().compararFormula(f.getSubFormulaIzq()) and self.getSubFormulaDer().compararFormula(f.getSubFormulaDer()))
		else:
			return False

	def imprimirFormula(self):
		return ("(" + self.getSubFormulaIzq().imprimirFormula() + " AND " + self.getSubFormulaDer().imprimirFormula() + ")")
	
	def verificarTrazaV(self, traza):
		if traza == []:
			return traza
		trazaIzq = self.getSubFormulaIzq().verificarTrazaV(traza)
		if trazaIzq == traza:
			return traza
		return self.getSubFormulaDer().verificarTrazaV(traza)
	
	def verificarTrazaF(self, traza):
		if traza == []:
			return traza
		trazaIzq = self.getSubFormulaIzq().verificarTrazaF(traza)
		if trazaIzq == traza:
			return self.getSubFormulaDer().verificarTrazaF(traza)
		return trazaIzq
	
	def verificarTrazaVTrans(self, traza):
		if traza == []:
			return traza
		trazaIzq = self.getSubFormulaIzq().verificarTrazaVTrans(traza)
		if trazaIzq == traza:
			return traza
		return self.getSubFormulaDer().verificarTrazaVTrans(traza)
	
	def verificarTrazaFTrans(self, traza):
		if traza == []:
			return traza
		trazaIzq = self.getSubFormulaIzq().verificarTrazaFTrans(traza)
		if trazaIzq == traza:
			return self.getSubFormulaDer().verificarTrazaFTrans(traza)
		return trazaIzq
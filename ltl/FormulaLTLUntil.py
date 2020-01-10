from FormulaLTLBinaria import FormulaLTLBinaria

class FormulaLTLUntil(FormulaLTLBinaria):
	"Formula LTL (until)"
	def __init__(self, sfizq, sfder):
		FormulaLTLBinaria.__init__(self, sfizq, sfder)
	
	def compararFormula(self, f):
		"Devuelve True si la formula es igual a f."
		if isinstance(f, FormulaLTLUntil):
			return (self.getSubFormulaIzq().compararFormula(f.getSubFormulaIzq()) and self.getSubFormulaDer().compararFormula(f.getSubFormulaDer()))
		else:
			return False

	def imprimirFormula(self):
		return ("(" + self.getSubFormulaIzq().imprimirFormula() + " UNTIL " + self.getSubFormulaDer().imprimirFormula() + ")")
		
	def verificarTrazaV(self, traza):
		if traza == []:
			return traza
		trazaDer = self.getSubFormulaDer().verificarTrazaV(traza)
		if trazaDer != traza:
			return trazaDer
		trazaIzq = self.getSubFormulaIzq().verificarTrazaV(traza)
		if trazaIzq == traza:
			return traza
		return [traza[0]] + self.verificarTrazaVTrans(traza[1:])

	def verificarTrazaF(self, traza):
		if traza == []:
			return traza
		trazaDer = self.getSubFormulaDer().verificarTrazaF(traza)
		if trazaDer == traza:
			return traza
		trazaIzq = self.getSubFormulaIzq().verificarTrazaF(traza)
		if trazaIzq != traza:
			return trazaIzq
		return [traza[0]] + self.verificarTrazaFTrans(traza[1:])

	def verificarTrazaVTrans(self, traza):
		if traza == []:
			return traza
		trazaDer = self.getSubFormulaDer().verificarTrazaVTrans(traza)
		if trazaDer != traza:
			return trazaDer
		trazaIzq = self.getSubFormulaIzq().verificarTrazaVTrans(traza)
		if trazaIzq == traza:
			return traza
		return [traza[0]] + self.verificarTrazaVTrans(traza[1:])

	def verificarTrazaFTrans(self, traza):
		if traza == []:
			return traza
		trazaDer = self.getSubFormulaDer().verificarTrazaFTrans(traza)
		if trazaDer == traza:
			return traza
		trazaIzq = self.getSubFormulaIzq().verificarTrazaFTrans(traza)
		if trazaIzq != traza:
			return trazaIzq
		return [traza[0]] + self.verificarTrazaFTrans(traza[1:])

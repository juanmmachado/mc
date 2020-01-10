from FormulaLTLUnaria import FormulaLTLUnaria

class FormulaLTLNegacion(FormulaLTLUnaria):
	"Formula LTL (negacion)"
	def __init__(self, sf):
		FormulaLTLUnaria.__init__(self, sf)
	
	def normalizar(self):
		sf_norm = self.getSubFormula().normalizar()
		if isinstance(sf_norm, FormulaLTLNegacion):
			f_norm = sf_norm.getSubFormula()
			return f_norm
		else:
			f_norm = FormulaLTLNegacion(sf_norm)
			return f_norm
	
	def negar(self):
		return self.getSubFormula()
	
	def obtenerNombreNegacionAtomica(self):
		"Devuelve el nombre de la formula negada en caso de que esta sea atomica."
		return self.getSubFormula().obtenerNombreAtomica()
	
	def getSubFormulasPositivas(self):
		"Devuelve el conjunto de todas las subformulas cuyo conectivo principal no es una negacion."
		return self.getSubFormula().getSubFormulasPositivas()

	def compararFormula(self, f):
		"Devuelve True si la formula es igual a f."
		if isinstance(f, FormulaLTLNegacion):
			return self.getSubFormula().compararFormula(f.getSubFormula())
		else:
			return False

	def imprimirFormula(self):
		return ("(NOT " + self.getSubFormula().imprimirFormula() + ")")
		
	# def verificarTraza(self, traza):
		# return (not self.getSubFormula().verificarTraza(traza))

	def verificarTrazaV(self, traza):
		return self.getSubFormula().verificarTrazaF(traza)
	
	def verificarTrazaF(self, traza):
		return self.getSubFormula().verificarTrazaV(traza)
	
	def verificarTrazaVTrans(self, traza):
		return self.getSubFormula().verificarTrazaFTrans(traza)
	
	def verificarTrazaFTrans(self, traza):
		return self.getSubFormula().verificarTrazaVTrans(traza)
	
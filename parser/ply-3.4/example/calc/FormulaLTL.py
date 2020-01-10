class FormulaLTL(object):
	"Formula LTL"
	def perteneceLista(self, listaForms):
		for f in listaForms:
			if self.compararFormula(f):
				return True
		return False

	def obtenerUntils(self, listaFormulas):
		from FormulaLTLUntil import FormulaLTLUntil
		untils = []
		for formula in listaFormulas:
			if isinstance(formula, FormulaLTLUntil):
				untils.append(formula)
		return untils

	def obtenerNexts(self, listaFormulas):
		from FormulaLTLNext import FormulaLTLNext
		nexts = []
		for formula in listaFormulas:
			if isinstance(formula, FormulaLTLNext):
				nexts.append(formula)
		return nexts

	def normalizarNegacion(self):
		from FormulaLTLNegacion import FormulaLTLNegacion
		if isinstance(self, FormulaLTLNegacion):
			return self.getSubFormula()
		else:
			return FormulaLTLNegacion(self)

	def normalizarFormula(self):
		from FormulaLTLDisyuncion import FormulaLTLDisyuncion
		if isinstance(self, FormulaLTLDisyuncion):
			return FormulaLTLNegacion(FormulaLTLConjuncion(self.getSubFormulaIzq().normalizarNegacion(), self.getSubFormulaDer().normalizarNegacion()))
		elif isinstance(self, FormulaLTLCondicion):
			return FormulaLTLNegacion(FormulaLTLConjuncion(self.getSubFormulaIzq(), self.getSubFormulaDer().normalizarNegacion()))
		elif isinstance(self, FormulaLTLEventually):
			return FormulaLTLUntil(FormulaLTLAtomica("TRUE"), self.getSubFormula())
		elif isinstance(self, FormulaLTLAlways):
			return FormulaLTLNegacion(FormulaLTLUntil(FormulaLTLAtomica("TRUE"), FormulaLTLNegacion(self.getSubFormula())))
		else:
			return self

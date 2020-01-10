from FormulaLTLAtomica import FormulaLTLAtomica
from FormulaLTLNext import FormulaLTLNext
from FormulaLTLNegacion import FormulaLTLNegacion
from FormulaLTLConjuncion import FormulaLTLConjuncion
from FormulaLTLUntil import FormulaLTLUntil

class ParserFormulaLTL(object):
	def __init__(self):
		self.__THEN = "->"
		self.__SSI = "<->"
		self.__AND = "&&"
		self.__OR = "||"
		self.__UNTIL = "U"
		self.__NOT = "-"
		self.__NEXT = "()"
		self.__ALWAYS = "[]"
		self.__EVENTUALLY = "<>"
	
	def parsearFormula(self, formula):
		i_1 = formula.find(self.__THEN)
		i_2 = formula.find(self.__SSI)
		if ((i_2 != -1) and ((i_2 < i_1) or (i_1 == -1))):
			subIzq = self.parsearFormula2(formula[:i_2].rstrip())
			subDer = self.parsearFormula(formula[(i_2+len(self.__SSI)):].lstrip())
			return FormulaLTLConjuncion(FormulaLTLNegacion(FormulaLTLConjuncion(subIzq, FormulaLTLNegacion(subDer))), FormulaLTLNegacion(FormulaLTLConjuncion(subDer, FormulaLTLNegacion(subIzq))))
		elif (i_1 != -1):
			subIzq = self.parsearFormula2(formula[:i_1].rstrip())
			subDer = self.parsearFormula(formula[(i_1+len(self.__THEN)):].lstrip())
			return FormulaLTLNegacion(FormulaLTLConjuncion(subIzq, FormulaLTLNegacion(subDer)))
		else:
			return self.parsearFormula2(formula)
	
	def parsearFormula2(self, formula):
		i_1 = formula.find(self.__AND)
		i_2 = formula.find(self.__OR)
		if ((i_2 != -1) and ((i_2 < i_1) or (i_1 == -1))):
			subIzq = self.parsearFormula3(formula[:i_2].rstrip())
			subDer = self.parsearFormula2(formula[(i_2+len(self.__OR)):].lstrip())
			return FormulaLTLNegacion(FormulaLTLConjuncion(FormulaLTLNegacion(subIzq), FormulaLTLNegacion(subDer)))
		elif (i_1 != -1):
			subIzq = self.parsearFormula3(formula[:i_1].rstrip())
			subDer = self.parsearFormula2(formula[(i_1+len(self.__AND)):].lstrip())
			return FormulaLTLConjuncion(subIzq, subDer)
		else:
			return self.parsearFormula3(formula)
		
	def parsearFormula3(self, formula):
		i = formula.find(self.__UNTIL)
		if (i != -1):
			subIzq = self.parsearFormula4(formula[:i].rstrip())
			subDer = self.parsearFormula3(formula[(i+len(self.__UNTIL)):].lstrip())
			return FormulaLTLUntil(subIzq, subDer)
		else:
			return self.parsearFormula4(formula)
	
	def parsearFormula4(self, formula):
		i_1 = formula.find(self.__NOT)
		i_2 = formula.find(self.__NEXT)
		i_3 = formula.find(self.__ALWAYS)
		i_4 = formula.find(self.__EVENTUALLY)
		if (i_1 == 0):
			subForm = self.parsearFormula4(formula[len(self.__NOT):].lstrip())
			return FormulaLTLNegacion(subForm)
		elif (i_2 == 0):
			subForm = self.parsearFormula4(formula[len(self.__NEXT):].lstrip())
			return FormulaLTLNext(subForm)
		elif (i_3 == 0):
			subForm = self.parsearFormula4(formula[len(self.__ALWAYS):].lstrip())
			return FormulaLTLNegacion(FormulaLTLUntil(FormulaLTLAtomica("TRUE"), FormulaLTLNegacion(subForm)))
		elif (i_4 == 0):
			subForm = self.parsearFormula4(formula[len(self.__EVENTUALLY):].lstrip())
			return FormulaLTLUntil(FormulaLTLAtomica("TRUE"), subForm)
		else:
			return self.parsearFormula5(formula)

	def parsearFormula5(self, formula):
		return FormulaLTLAtomica(formula.strip())
	
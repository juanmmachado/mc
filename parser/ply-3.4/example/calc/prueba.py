from ProductoTSNBA import ProductoTSNBA
from TS import TS
from NBA import NBA
from GNBA import GNBA
from FormulaLTLAtomica import FormulaLTLAtomica
from FormulaLTLNext import FormulaLTLNext
from FormulaLTLNegacion import FormulaLTLNegacion
from FormulaLTLConjuncion import FormulaLTLConjuncion
from FormulaLTLUntil import FormulaLTLUntil
from ParserFormulaLTL import ParserFormulaLTL

class prueba(object):
	def __init__(self):
		pass
	
	def prueba1(self):
		alfa = FormulaLTLAtomica("alfa")
		nextalfa = FormulaLTLNext(alfa)
		nextalfa.imprimirFormula()
		
	def prueba2(self):
		alfa = FormulaLTLAtomica("alfa")
		nextalfa = FormulaLTLNext(alfa)
		g = GNBA()
		g.LTLtoGNBA(nextalfa)
		g.imprimirGNBA()
	
	def prueba3(self):
		alfa = FormulaLTLAtomica("alfa")
		beta = FormulaLTLAtomica("beta")
		notalfa = FormulaLTLNegacion(alfa)
		naab = FormulaLTLConjuncion(notalfa, beta)
		g = GNBA()
		g.LTLtoGNBA(naab)
		g.imprimirGNBA()
	
	def prueba4(self):
		beta = FormulaLTLAtomica("beta")
		bub = FormulaLTLUntil(beta, beta)
		g = GNBA()
		g.LTLtoGNBA(bub)
		g.imprimirGNBA()
		ts = TS(["alfa", "beta"], ["alfa"])
		ts.agregarTransicion("alfa", "beta")
		ts.agregarTransicion("beta", "beta")
		prod = ProductoTSNBA(ts, g)
		print "########################################################"
		ts. imprimirTS()
		print "########################################################"
		g.imprimirGNBA()
		print "########################################################"
		prod.imprimirProductoTSNBA()
		print "########################################################"
		return prod.verificar()

	def prueba5(self):
		alfa = FormulaLTLAtomica("alfa")
		nextalfa = FormulaLTLNext(alfa)
		g = GNBA()
		g.LTLtoGNBA(nextalfa)
		ts = TS(["TRUE", "alfa"], ["TRUE"])
		ts.agregarTransicion("TRUE", "alfa")
		ts.agregarTransicion("alfa", "alfa")
		prod = ProductoTSNBA(ts, g)
		print "########################################################"
		ts. imprimirTS()
		print "########################################################"
		g.imprimirGNBA()
		print "########################################################"
		prod.imprimirProductoTSNBA()
		print "########################################################"
		return prod.verificar()
	
	def prueba6(self):
		alfa = FormulaLTLAtomica("alfa")
		beta = FormulaLTLAtomica("beta")
		aub = FormulaLTLUntil(alfa, beta)
		bua = FormulaLTLUntil(beta, alfa)
		nextalfa = FormulaLTLNext(alfa)
		notnextalfa = FormulaLTLNegacion(nextalfa)
		nextbeta = FormulaLTLNext(beta)
		g = GNBA()
		g.LTLtoGNBA(aub)
#		print "CAS:"
#		print g.cantAcceptanceSets()
		g1 = GNBA()
		g1.LTLtoGNBA(notnextalfa)
		g2 = GNBA()
		g2.LTLtoGNBA(nextbeta)
		g3 = GNBA()
		g3.LTLtoGNBA(aub)
		# genaro TS
		ts = TS(["alfa", "beta"], ["beta"])
		ts.agregarTransicion("alfa", "beta")
		ts.agregarTransicion("beta", "beta")
		# prod = ProductoTSNBA(ts, g)
		# prod1 = ProductoTSNBA(ts, g1)
		# prod2 = ProductoTSNBA(ts, g2)
		prod3 = ProductoTSNBA(ts, g3)
		print "########################################################"
		ts. imprimirTS()
		print "########################################################"
		g3.imprimirGNBA()
		print "########################################################"
		prod3.imprimirProductoTSNBA()
		print "########################################################"
		# print prod.verificar()
		print prod3.verificar()
		# print prod2.verificar()
		# print prod3.verificar()
		
	def prueba7(self):
		alfa = FormulaLTLAtomica("alfa")
		beta = FormulaLTLAtomica("beta")
		ayb = FormulaLTLConjuncion(alfa, beta)
		aub = FormulaLTLUntil(alfa, beta)
		bua = FormulaLTLUntil(beta, alfa)
		aybub = FormulaLTLUntil(ayb, beta)
		g = GNBA()
		g.LTLtoGNBA(aybub)
#		print "CAS:"
#		print g.cantAcceptanceSets()
		# genero TS
		ts = TS(["alfa", "beta"], ["alfa"])
		ts.agregarTransicion("alfa", "beta")
		ts.agregarTransicion("beta", "beta")
		print "########################################################"
		g.imprimirGNBA()
		print "########################################################"
		prod = ProductoTSNBA(ts, g)
		prod.imprimirProductoTSNBA()
		print "########################################################"
		print prod.verificar()
		
	def prueba8(self):
		alfa = FormulaLTLAtomica("alfa")
		beta = FormulaLTLAtomica("beta")
		ayb = FormulaLTLConjuncion(alfa, beta)
		aub = FormulaLTLUntil(alfa, beta)
		bua = FormulaLTLUntil(beta, alfa)
		aybub = FormulaLTLUntil(ayb, beta)
		naybub = FormulaLTLNegacion(aybub)
		g = GNBA()
		g.LTLtoGNBA(aub)
#		print "CAS:"
#		print g.cantAcceptanceSets()
		# genero TS
		ts = TS(["alfa", "beta"], ["alfa"])
		ts.agregarTransicion("alfa", "beta")
		ts.agregarTransicion("beta", "beta")
		prod = ProductoTSNBA(ts, g)
#		prod.imprimirProductoTSNBA()
		print prod.verificar()

	def pruebaParser(self):
		parser = ParserFormulaLTL()
		f = parser.parsearFormula("alfa || beta")
		print f.imprimirFormula()
		f1 = parser.parsearFormula("alfa && beta")
		print f1.imprimirFormula()
		f2 = parser.parsearFormula("alfa <-> beta")
		print f2.imprimirFormula()
		f3 = parser.parsearFormula("alfa -> beta")
		print f3.imprimirFormula()
		f4 = parser.parsearFormula("[]alfa")
		print f4.imprimirFormula()
		f5 = parser.parsearFormula("<>alfa")
		print f5.imprimirFormula()
	

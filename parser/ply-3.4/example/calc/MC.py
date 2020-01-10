from ParserGraphML import ParserGraphML
from ParserFormulaLTL import ParserFormulaLTL
from GNBA import GNBA
from ProductoTSNBA import ProductoTSNBA
import sys

parserLTL = ParserFormulaLTL()
parserGML = ParserGraphML()
formula = parserLTL.parsearFormula(sys.argv[2])
print formula.imprimirFormula()
ts = parserGML.parsearTS(sys.argv[1])
print "############## TS ###############"
ts.imprimirTS()
g = GNBA()
g.LTLtoGNBA(formula)
print "############## GNBA ###############"
g.imprimirGNBA()
prod = ProductoTSNBA(ts, g)
print "############## PRODUCTO ###############"
prod.imprimirProductoTSNBA()
print prod.verificar()

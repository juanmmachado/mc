from GNBA import GNBA
from ProductoTSNBA import ProductoTSNBA

class LTLMC(object):
	"LTL Model Checker"
	def __init__(self):
		pass
	
	def verificar(self, ts, formula):
		"Verifica si ts satisface formula"
		f = formula.negar().normalizar()
		g = GNBA()
		g.LTLtoGNBA(f)
		prod = ProductoTSNBA(ts, g)
		traza = prod.verificar()
		if traza == []:
			print "El sistema cumple la propiedad."
		else:
			print "El sistema no cumple la propiedad."
			print "Contraejemplo:"
			prod.imprimirTraza(f.verificarTrazaV(traza))
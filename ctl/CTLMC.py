from FormulaCTLTrue import FormulaCTLTrue
from FormulaCTLAtomica import FormulaCTLAtomica
from FormulaCTLExisteNext import FormulaCTLExisteNext
from FormulaCTLNegacion import FormulaCTLNegacion
from FormulaCTLConjuncion import FormulaCTLConjuncion
from FormulaCTLExisteUntil import FormulaCTLExisteUntil
from FormulaCTLExisteAlways import FormulaCTLExisteAlways

class CTLMC(object):
	"CTL Model Checker"
	def __init__(self):
		pass
	
	def verificar(self, ts, formula):
		"Verifica si ts satisface formula"
		f = formula.normalizar()
		iniciales = ts.getIniciales()
		sat = f.getSat(ts)
		res = True
		for ini in iniciales:
			if ini not in sat:
				res = False
				print "El sistema NO cumple la propiedad."
				traza = self.contraejemplo(ts, ini, f)
				if traza != []:
					print "Contraejemplo:"
					ts.imprimirTraza(traza)
		if res:
			print "El sistema cumple la propiedad."
			trazas = self.testigos(ts, f)
			if trazas != []:
				print "Testigos para cada estado inicial:"
				for traza in trazas:
					print "Estado inicial", traza[0].getId()
					ts.imprimirTraza(traza)

	def testigos(self, ts, formula):
		#formula debe estar normalizada
		if isinstance(formula, FormulaCTLExisteNext):
			return self.testigosNext(ts, formula)
		elif isinstance(formula, FormulaCTLExisteAlways):
			return self.testigosAlways(ts, formula)
		elif isinstance(formula, FormulaCTLExisteUntil):
			return self.testigosUntil(ts, formula)
		return []
		
	def testigosNext(self, ts, f_norm):
		sf_sat = f_norm.getSubFormula().getAtrSat()
		trazas = []
		for s in ts.getIniciales():
			listo = False
			i = 0
			fin = len(s.getTransiciones())
			while (i < fin) and (not listo):
				t = (s.getTransiciones())[i]
				if t.getDestino() in sf_sat:
					trazas.append([s, t])
					listo = True
				i += 1
		return trazas
	
	def testigosAlways(self, ts, f_norm):
		sf_sat = f_norm.getSubFormula().getAtrSat()
		trazas = []
		for s in ts.getIniciales():
			listo = False
			i = 0
			fin = len(s.getTransiciones())
			while (i < fin) and (not listo):
				t = (s.getTransiciones())[i]
				traza = self.DFStestigoAlways(sf_sat, t, [s]) # [s] = marcados
				if traza != []:
					trazas.append([s] + traza)
					listo = True
				i += 1
		return trazas
		
	def testigosUntil(self, ts, f_norm):
		sfIzq_sat = f_norm.getSubFormulaIzq().getAtrSat()
		sfDer_sat = f_norm.getSubFormulaDer().getAtrSat()
		trazas = []
		for s in ts.getIniciales():
			if s in sfDer_sat:
				trazas.append([s])
			elif s in sfIzq_sat:
				listo = False
				i = 0
				fin = len(s.getTransiciones())
				while (i < fin) and (not listo):
					t = (s.getTransiciones())[i]
					traza = self.DFStestigoUntil(sfIzq_sat, sfDer_sat, t, [s])
					if traza != []:
						trazas.append([s] + traza)
						listo = True
					i += 1
		return trazas
	
	def DFStestigoAlways(self, sat, t, marcados):
		s = t.getDestino()
		if s in sat:
			if s in marcados:
				return [t]
			for t2 in s.getTransiciones():
				res = self.DFStestigoAlways(sat, t2, [s] + marcados)
				if res != []:
					return res
		return []
		
	def DFStestigoUntil(self, sat1, sat2, t, marcados):
		s = t.getDestino()
		if s in marcados:
			return []
		if s in sat2:
			return [t]
		for t2 in s.getTransiciones():
			res = self.DFStestigoUntil(sat1, sat2, t2, [s] + marcados)
			if res != []:
				return [t] + res
		return []

	def contraejemplo(self, ts, ini, formula):
		traza = []
		if isinstance(formula, FormulaCTLNegacion):
			sf = formula.getSubFormula()
			if isinstance(sf, FormulaCTLExisteNext):
				sat = sf.getSubFormula().getAtrSat()
				for t in ini.getTransiciones():
					if t.getDestino() in sat:
						return [ini, t]
			elif isinstance(sf, FormulaCTLExisteAlways):
				sat = sf.getSubFormula().getAtrSat()
				for t in ini.getTransiciones():
					traza = self.DFStestigoAlways(sat, t, [ini])
					if traza != []:
						return ([ini] + traza)
			elif isinstance(sf, FormulaCTLExisteUntil):
				satIzq = sf.getSubFormulaIzq().getAtrSat()
				satDer = sf.getSubFormulaDer().getAtrSat()
				if ini in satDer:
					return [ini]
				elif ini in satIzq:
					for t in ini.getTransiciones():
						traza = self.DFStestigoUntil(satIzq, satDer, t, [ini])
						if traza != []:
							return ([ini] + traza)
		return [ini]

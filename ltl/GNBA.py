from FormulaLTL import FormulaLTL
from FormulaLTLAtomica import FormulaLTLAtomica
from FormulaLTLNext import FormulaLTLNext
from FormulaLTLNegacion import FormulaLTLNegacion
from FormulaLTLUntil import FormulaLTLUntil
from FormulaLTLConjuncion import FormulaLTLConjuncion
from Nodo import Nodo
from Herramientas import Herramientas

class GNBA(object):
	"Automata de Buchi"
	def __init__(self):
		self.__estados = []
		self.__iniciales = []
		self.__acceptanceSets = []
		self.__atomicas = []

	def getAtomicas(self):
		return self.__atomicas
	
	def isInicial(self, id):
		"Devuelve True si el nodo id es inicial."
		for nodo in self.__iniciales:
			if (nodo.getId() == id):
				return True
		return False
	
	def isFinalN(self, id, n):
		"Devuelve True si el nodo id esta en el n-esimo conjunto de aceptacion."
		for nodo in self.__acceptanceSets[n]:
			if (nodo.getId() == id):
				return True
		return False

	def getAdycentesIniciales(self, props):
		"Devuelve los nodos iniciales que verifican las proposiciones dadas."
		adys = []
		for ini in self.__iniciales:
			if ini.verificaAtomicas(props):
				adys.append(ini)
		return adys
	
	def cantAcceptanceSets(self):
		"Devuelve la cantidad de conjuntos de aceptacion del GNBA"
		return len(self.__acceptanceSets)
		
	def buscarAdyacentes(self, id):
		"Devuelve los nodos adyacentes al nodo id."
		for nodo in self.__estados:
			if (nodo.getId() == id):
				return nodo.getAdyacentes()
		return []
	
	def obtenerEstados(self, positivas, estados, actual):
		""
		if positivas == []:
			estados.append(actual)
		else:
			phi = positivas.pop()
			nphi = phi.normalizarNegacion()
			if not phi.perteneceLista(actual):
				if not nphi.perteneceLista(actual):
					if isinstance(phi, FormulaLTLAtomica):
						actual2 = actual[:]
						positivas2 = positivas[:]
						actual.append(phi)
						actual2.append(nphi)
						self.obtenerEstados(positivas, estados, actual)
						self.obtenerEstados(positivas2, estados, actual2)
					elif isinstance(phi, FormulaLTLNext):
						actual2 = actual[:]
						positivas2 = positivas[:]
						actual.append(phi)
						actual2.append(nphi)
						self.obtenerEstados(positivas, estados, actual)
						self.obtenerEstados(positivas2, estados, actual2)
					elif isinstance(phi, FormulaLTLConjuncion):
						phi1 = phi.getSubFormulaIzq()
						phi2 = phi.getSubFormulaDer()
						nphi1 = phi1.normalizarNegacion()
						nphi2 = phi2.normalizarNegacion()
						if not phi1.perteneceLista(actual):
							if not nphi1.perteneceLista(actual):
								if not phi2.perteneceLista(actual):
									if not nphi2.perteneceLista(actual):
										actual2 = actual[:]
										actual3 = actual[:]
										positivas2 = positivas[:]
										positivas3 = positivas[:]
										actual.append(phi)
										actual.append(phi1)
										actual.append(phi2)
										self.obtenerEstados(positivas, estados, actual)
										actual2.append(nphi)
										actual2.append(nphi1)
										self.obtenerEstados(positivas2, estados, actual2)
										actual3.append(nphi)
										actual3.append(nphi2)
										self.obtenerEstados(positivas3, estados, actual3)
									else:	# nphi2 in actual
										actual.append(nphi)
										self.obtenerEstados(positivas, estados, actual)
								else:	# phi2 in actual
									actual2 = actual[:]
									positivas2 = positivas[:]
									actual.append(phi)
									actual.append(phi1)
									self.obtenerEstados(positivas, estados, actual)
									actual2.append(nphi)
									actual2.append(nphi1)
									self.obtenerEstados(positivas2, estados, actual2)
							else:	# nphi1 in actual
								actual.append(nphi)
								self.obtenerEstados(positivas, estados, actual)
						else:	# phi1 in actual
							if not phi2.perteneceLista(actual):
								if not nphi2.perteneceLista(actual):
									actual2 = actual[:]
									positivas2 = positivas[:]
									actual.append(phi)
									actual.append(phi2)
									self.obtenerEstados(positivas, estados, actual)
									actual2.append(nphi)
									actual2.append(nphi2)
									self.obtenerEstados(positivas2, estados, actual2)
								else:
									actual.append(nphi)
									self.obtenerEstados(positivas, estados, actual)
							else:
								actual.append(phi)
								self.obtenerEstados(positivas, estados, actual)
					elif isinstance(phi, FormulaLTLUntil):
						phi1 = phi.getSubFormulaIzq()
						phi2 = phi.getSubFormulaDer()
						nphi1 = phi1.normalizarNegacion()
						nphi2 = phi2.normalizarNegacion()
						if not phi1.perteneceLista(actual):
							if not nphi1.perteneceLista(actual):
								if not phi2.perteneceLista(actual):
									if not nphi2.perteneceLista(actual):
										actual2 = actual[:]
										actual3 = actual[:]
										positivas2 = positivas[:]
										positivas3 = positivas[:]
										actual.append(phi)
										actual.append(phi1)
										actual.append(nphi2)
										self.obtenerEstados(positivas, estados, actual)
										actual2.append(phi)
										actual2.append(phi2)
										self.obtenerEstados(positivas2, estados, actual2)
										actual3.append(nphi)
										actual3.append(nphi2)
										self.obtenerEstados(positivas3, estados, actual3)
									else:	# nphi2 in actual
										actual2 = actual[:]
										positivas2 = positivas[:]
										actual.append(phi)
										actual.append(phi1)
										self.obtenerEstados(positivas, estados, actual)
										actual2.append(nphi)
										self.obtenerEstados(positivas2, estados, actual2)
								else:	# phi2 in actual
									actual.append(phi)
									self.obtenerEstados(positivas, estados, actual)
							else:	# nphi1 in actual
								if not phi2.perteneceLista(actual):
									if not nphi2.perteneceLista(actual):
										actual2 = actual[:]
										positivas2 = positivas[:]
										actual.append(phi)
										actual.append(phi2)
										self.obtenerEstados(positivas, estados, actual)
										actual2.append(nphi)
										actual2.append(nphi2)
										self.obtenerEstados(positivas2, estados, actual2)
									else:	# nphi2 in actual
										actual.append(nphi)
										self.obtenerEstados(positivas, estados, actual)
								else: # phi2 in actual
									actual.append(phi)
									self.obtenerEstados(positivas, estados, actual)
						else:	# phi1 in actual
							if not phi2.perteneceLista(actual):
								if not nphi2.perteneceLista(actual):
									actual.append(phi)
									self.obtenerEstados(positivas, estados, actual)
								else: # nphi2 in actual
									actual2 = actual[:]
									positivas2 = positivas[:]
									actual.append(nphi)
									self.obtenerEstados(positivas, estados, actual)
									actual2.append(phi)
									self.obtenerEstados(positivas2, estados, actual2)
							else:	# phi2 in actual
								actual.append(phi)
								self.obtenerEstados(positivas, estados, actual)
				else:	# nphi in actual
					if isinstance(phi, FormulaLTLAtomica):
						self.obtenerEstados(positivas, estados, actual)
					elif isinstance(phi, FormulaLTLNext):
						self.obtenerEstados(positivas, estados, actual)
					elif isinstance(phi, FormulaLTLConjuncion):
						phi1 = phi.getSubFormulaIzq()
						phi2 = phi.getSubFormulaDer()
						nphi1 = phi1.normalizarNegacion()
						nphi2 = phi2.normalizarNegacion()
						if not phi1.perteneceLista(actual):
							if not nphi1.perteneceLista(actual):
								if not phi2.perteneceLista(actual):
									if not nphi2.perteneceLista(actual):
										actual2 = actual[:]
										positivas2 = positivas[:]
										actual.append(nphi1)
										self.obtenerEstados(positivas, estados, actual)
										actual2.append(nphi2)
										self.obtenerEstados(positivas2, estados, actual2)
									else:	# nphi2 in actual
										self.obtenerEstados(positivas, estados, actual)
								else:	# phi2 in actual
									actual.append(nphi1)
									self.obtenerEstados(positivas, estados, actual)
							else:	# nphi1 in actual
								self.obtenerEstados(positivas, estados, actual)
						else:	# phi1 in actual
							if not phi2.perteneceLista(actual):
								if not nphi2.perteneceLista(actual):
									actual.append(nphi2)
									self.obtenerEstados(positivas, estados, actual)
								else:
									self.obtenerEstados(positivas, estados, actual)
							else:
								pass
					elif isinstance(phi, FormulaLTLUntil):
						phi1 = phi.getSubFormulaIzq()
						phi2 = phi.getSubFormulaDer()
						nphi1 = phi1.normalizarNegacion()
						nphi2 = phi2.normalizarNegacion()
						if not phi1.perteneceLista(actual):
							if not nphi1.perteneceLista(actual):
								if not phi2.perteneceLista(actual):
									if not nphi2.perteneceLista(actual):
										actual.append(nphi2)
										self.obtenerEstados(positivas, estados, actual)
									else:	# nphi2 in actual
										self.obtenerEstados(positivas, estados, actual)
								else:	# phi2 in actual
									pass
							else:	# nphi1 in actual
								if not phi2.perteneceLista(actual):
									if not nphi2.perteneceLista(actual):
										actual.append(nphi2)
										self.obtenerEstados(positivas, estados, actual)
									else:	# nphi2 in actual
										self.obtenerEstados(positivas, estados, actual)
								else: # phi2 in actual
									pass
						else:	# phi1 in actual
							if not phi2.perteneceLista(actual):
								if not nphi2.perteneceLista(actual):
									pass
								else: # nphi2 in actual
									self.obtenerEstados(positivas, estados, actual)
							else:	# phi2 in actual
								pass
			else:	# phi in actual
				if not nphi.perteneceLista(actual):
					if isinstance(phi, FormulaLTLAtomica):
						self.obtenerEstados(positivas, estados, actual)
					elif isinstance(phi, FormulaLTLNext):
						self.obtenerEstados(positivas, estados, actual)
					elif isinstance(phi, FormulaLTLConjuncion):
						phi1 = phi.getSubFormulaIzq()
						phi2 = phi.getSubFormulaDer()
						nphi1 = phi1.normalizarNegacion()
						nphi2 = phi2.normalizarNegacion()
						if not phi1.perteneceLista(actual):
							if not nphi1.perteneceLista(actual):
								if not phi2.perteneceLista(actual):
									if not nphi2.perteneceLista(actual):
										actual.append(phi1)
										actual.append(phi2)
										self.obtenerEstados(positivas, estados, actual)
									else:	# nphi2 in actual
										pass
								else:	# phi2 in actual
									actual.append(phi1)
									self.obtenerEstados(positivas, estados, actual)
							else:	# nphi1 in actual
								pass
						else:	# phi1 in actual
							if not phi2.perteneceLista(actual):
								if not nphi2.perteneceLista(actual):
									actual.append(phi2)
									self.obtenerEstados(positivas, estados, actual)
								else:
									pass
							else:
								self.obtenerEstados(positivas, estados, actual)
					elif isinstance(phi, FormulaLTLUntil):
						phi1 = phi.getSubFormulaIzq()
						phi2 = phi.getSubFormulaDer()
						nphi1 = phi1.normalizarNegacion()
						nphi2 = phi2.normalizarNegacion()
						if not phi1.perteneceLista(actual):
							if not nphi1.perteneceLista(actual):
								if not phi2.perteneceLista(actual):
									if not nphi2.perteneceLista(actual):
										actual2 = actual[:]
										positivas2 = positivas[:]
										actual.append(phi1)
										actual.append(nphi2)
										self.obtenerEstados(positivas, estados, actual)
										actual2.append(phi2)
										self.obtenerEstados(positivas2, estados, actual2)
									else:	# nphi2 in actual
										actual.append(phi1)
										self.obtenerEstados(positivas, estados, actual)
								else:	# phi2 in actual
									self.obtenerEstados(positivas, estados, actual)
							else:	# nphi1 in actual
								if not phi2.perteneceLista(actual):
									if not nphi2.perteneceLista(actual):
										actual.append(phi2)
										self.obtenerEstados(positivas, estados, actual)
									else:	# nphi2 in actual
										pass
								else: # phi2 in actual
									self.obtenerEstados(positivas, estados, actual)
						else:	# phi1 in actual
							if not phi2.perteneceLista(actual):
								if not nphi2.perteneceLista(actual):
									self.obtenerEstados(positivas, estados, actual)
								else: # nphi2 in actual
									self.obtenerEstados(positivas, estados, actual)
							else:	# phi2 in actual
								self.obtenerEstados(positivas, estados, actual)
				else:	# nphi in actual
					pass

	def LTLtoGNBA(self, formula):
		"Genera un GNBA correspondiente a la formula dada."
		#obtengo los conjuntos elementales de formulas
		self.__atomicas = formula.getAtomicas()
		positivas = formula.getSubFormulasPositivas()
		untilsCl = formula.obtenerUntils(positivas)							# corregir
		nextsCl = formula.obtenerNexts(positivas)
		estados = []
		estadosInicial = []
		atomicaTrue = FormulaLTLAtomica("TRUE")
		if  atomicaTrue.perteneceLista(self.__atomicas):
			estadosInicial.append(atomicaTrue)
		self.obtenerEstados(positivas, estados, estadosInicial)
		#creo los estados del automata con los conjuntos elementales
		idNodo = 0
		for est in estados:
			nodo = Nodo(est, idNodo)
			self.__estados.append(nodo)
			idNodo += 1
		#obtengo los estados iniciales
		for nodo in self.__estados:
			if nodo.perteneceFormula(formula):
				self.__iniciales.append(nodo)
		#obtengo los acceptance sets
		for ucl in untilsCl:
			aSet = []
			for nodo in self.__estados:
				if ((not nodo.perteneceFormula(ucl)) or nodo.perteneceFormula(ucl.getSubFormulaDer())):
					aSet.append(nodo)
			self.__acceptanceSets.append(aSet)
		#agrego transiciones entre estados
		for nodo in self.__estados:
			nexts = formula.obtenerNexts(nodo.getFormulas())
			h = Herramientas()
			notnexts = h.restarListas(nextsCl, nexts)
			adys = self.__estados[:]
			for n in nexts: # next pertenece
				adys_act = []
				for nodoady in adys:
					if nodoady.perteneceFormula(n.getSubFormula()):
						adys_act.append(nodoady)
				adys = adys_act[:]
			for nn in notnexts: #not next pertenece
				adys_act = []
				for nodoady in adys:
					if not nodoady.perteneceFormula(nn.getSubFormula()):
						adys_act.append(nodoady)
				adys = adys_act[:]
			# para las formulas until
			untils = formula.obtenerUntils(nodo.getFormulas())
			notuntils = h.restarListas(untilsCl, untils)
			for u in untils:
				adys_act = []
				for nodoady in adys: # until pertenece
					if nodo.perteneceFormula(u.getSubFormulaDer()) or (nodo.perteneceFormula(u.getSubFormulaIzq()) and nodoady.perteneceFormula(u)):
						adys_act.append(nodoady)
				adys = adys_act[:]
			for nu in notuntils: #not until pertenece
				adys_act = []
				for nodoady in adys:
					if not (nodo.perteneceFormula(nu.getSubFormulaDer()) or (nodo.perteneceFormula(nu.getSubFormulaIzq()) and nodoady.perteneceFormula(nu))):
						adys_act.append(nodoady)
				adys = adys_act[:]
			for ady in adys:
				nodo.agregarAdyacente(ady)
		#elimino estados terminales
		for nodo in self.__estados:
			if (nodo.getAdyacentes() == []):
				pozo = Nodo([FormulaLTLAtomica("TRUE")], -1)
				pozo.agregarAdyacente(pozo)
				nodo.agregarAdyacente(pozo)

	def imprimirGNBA(self):
		print "Estados:"
		i = 1
		for estado in self.__estados:
			print i
			estado.imprimirEstado()
			for ady in estado.getNodosAdyacentes():
				ady.imprimirEstado()
			i = i + 1
		print "Iniciales:"
		for ini in self.__iniciales:
			ini.imprimirEstado()
		print "Acceptance sets"
		i = 1
		for aSet in self.__acceptanceSets:
			print i
			for q in aSet:
				q.imprimirEstado()
			i = i + 1

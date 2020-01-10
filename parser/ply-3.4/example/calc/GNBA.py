from FormulaLTL import FormulaLTL
from FormulaLTLAtomica import FormulaLTLAtomica
from FormulaLTLNext import FormulaLTLNext
from FormulaLTLNegacion import FormulaLTLNegacion
from FormulaLTLUntil import FormulaLTLUntil
from FormulaLTLConjuncion import FormulaLTLConjuncion
from Nodo import Nodo

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
		for nodo in self.__iniciales:
			if (nodo.getId() == id):
				return True
		return False
	
	def isFinalN(self, id, n):
		for nodo in self.__acceptanceSets[n]:
			if (nodo.getId() == id):
				return True
		return False

	def getAdycentesIniciales(self, nombre):
		adys = []
		for ini in self.__iniciales:
			for ady in ini.getEstadosAdyacentes(nombre):							#for ady in ini.getAdyacentes():
#				if ady.verificaAtomica(nombre):
				if ady not in adys:
					adys.append(ady)
		return adys
	
	def cantAcceptanceSets(self):
		return len(self.__acceptanceSets)
		
	def buscarAdyacentes(id):
		for nodo in self.__estados:
			if (nodo.getId() == id):
				return nodo.getAdyacentes()
		return []
	
	def obtenerEstados(self, positivas, estados, actual):
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
	#seguir creo
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
		#obtengo los conjuntos elementales de formulas
		self.__atomicas = formula.getAtomicas()
		positivas = formula.getSubFormulasPositivas()
		# debug
		#print "POSITIVAS:"
		#for pos in positivas:
		#	pos.imprimirFormula()
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
		for ncl in nextsCl:
			for nodo in self.__estados:
				if nodo.perteneceFormula(ncl):
					for nodoady in self.__estados:
						if nodoady.perteneceFormula(ncl.getSubFormula()):
							nodo.agregarAdyacente(nodoady)
				else:	# not next pertenece
					for nodoady in self.__estados:
						if not nodoady.perteneceFormula(ncl.getSubFormula()):
							nodo.agregarAdyacente(nodoady)
		for ucl in untilsCl:
			for nodo in self.__estados:
				if nodo.perteneceFormula(ucl):
					for nodoady in self.__estados:
						if nodo.perteneceFormula(ucl.getSubFormulaDer()) or (nodo.perteneceFormula(ucl.getSubFormulaIzq()) and nodoady.perteneceFormula(ucl)):
							nodo.agregarAdyacente(nodoady)
				else:	# not until pertenece
					for nodoady in self.__estados:
						if not (nodo.perteneceFormula(ucl.getSubFormulaDer()) or (nodo.perteneceFormula(ucl.getSubFormulaIzq()) and nodoady.perteneceFormula(ucl))):
							nodo.agregarAdyacente(nodoady)

	def copiarEstadosGNBA(self, n):
		# crea una copia de los estados
		copia = []
		for nodo in self.__estados:
			nodoNBA = NodoNBA(nodo, n)
			copia.append(nodoNBA)
		return copia

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
		
	def GNBAtoNBA(self):
		# obtengo k copias
		nba = NBA()
		for i in range(0,len(self.__acceptanceSets)):
			estados = self.copiarEstadosGNBA(i)
			nba.agregarEstados(estados)
		nba.agregarTransiciones(self)
		# set estados iniciales
		nba.setIniciales(self)
		nba.setFinales(self)
		return nba

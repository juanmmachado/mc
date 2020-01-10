from TS import TS
from NBA import NBA
from GNBA import GNBA
from NodoProductoTSNBA import NodoProductoTSNBA

class ProductoTSNBA(object):
	"Producto entre Sistema de transiciones y NBA"
	def __init__(self, ts, nba):
		#normalizar TS
		#ts.normalizarEstados(nba.getAtomicas())
		#generar iniciales
		iniciales = []
		for ini in ts.getIniciales():
			for ininba in nba.getAdycentesIniciales(ini.getNombre()):
				nodo = NodoProductoTSNBA(ini, ininba)
				iniciales.append(nodo)
		self.__iniciales = iniciales
		#generar parte alcanzable
		self.__estados = iniciales[:]
		self.parteAlcanzable(iniciales, ts, nba)
		self.generarAcceptanceSets(nba)
	
	def parteAlcanzable(self, estados, ts, nba):
		for q in estados:
			estadosNuevos = []
			for ady in q.getNodoTS().getEstadosAdyacentes():
				adysnba = q.getNodoNBA().getEstadosAdyacentes(ady.getNombre())
				for adynba in adysnba:
					if not self.perteneceEstado(ady, adynba):
						nodo = NodoProductoTSNBA(ady, adynba)
						self.__estados.append(nodo)
						q.agregarAdyacente(nodo)
						estadosNuevos.append(nodo)
					else:
						nodo = self.buscarEstado(ady, adynba)
						q.agregarAdyacente(nodo)
			self.parteAlcanzable(estadosNuevos, ts, nba)

	def perteneceEstado(self, nodots, nodonba):
		for estado in self.__estados:
			if (nodots.getId() == estado.getNodoTS().getId()) and (nodonba.getId() == estado.getNodoNBA().getId()):
				return True
		return False
	
	def buscarEstado(self, nodots, nodonba):
		for estado in self.__estados:
			if (nodots.getId() == estado.getNodoTS().getId()) and (nodonba.getId() == estado.getNodoNBA().getId()):
				return estado
		return None

	def generarAcceptanceSets(self, nba):
		self.__acceptanceSets = []
		print "cantidad de acceptance sets"
		for i in range(0, nba.cantAcceptanceSets()):
			print i
			self.__acceptanceSets.append([])
		for estado in self.__estados:
			for i in range(0, nba.cantAcceptanceSets()):
				if nba.isFinalN(estado.getNodoNBA().getId(), i):
					self.__acceptanceSets[i].append(estado)
	
	def verificar(self):
		if self.__iniciales != []:
			N = len(self.__acceptanceSets)
			if N == 0:
				N = 1
				self.__acceptanceSets.append(self.__estados)
			for ini in self.__iniciales:
				traza = self.verificarCiclo1(ini, [], N)
				if (traza != []):
					return traza
#		elif acceptance sets == []: buscar ciclo cualquiera
		return []
	
	def verificarCiclo1(self, q, marcados, N):
		marcados.append(q)
		traza = [q.getNodoTS().getNombre()]
		if N == 1:
			if q in self.__acceptanceSets[0]:
				for ady in q.getAdyacentes():
					if ady not in marcados:
						marcados_copia = marcados[:]
						trazaActual = self.verificarCiclo1(ady, marcados_copia, N)
						if ((trazaActual != []) and (trazaActual != None)):
							return trazaActual.extend(traza)
#					if q != ady:
					marcados1 = marcados[:]
					trazaActual = self.verificarCiclo3(ady, [], marcados1)
					if ((trazaActual != []) and (trazaActual != None)):
						return trazaActual.extend(traza)
			else:
				for ady in q.getAdyacentes():
					if ady not in marcados:
						marcados_copia = marcados[:]
						trazaActual = self.verificarCiclo1(ady, marcados_copia, N)
						if ((trazaActual != []) and (trazaActual != None)):
							return trazaActual.extend(traza)
		else:
			if q in self.__acceptanceSets[0]:
				for ady in q.getAdyacentes():
					if ady not in marcados:
						marcados_copia = marcados[:]
						trazaActual = self.verificarCiclo1(ady, marcados_copia, N)
						if ((trazaActual != []) and (trazaActual != None)):
							return trazaActual.extend(traza)
					if q != ady:
						marcados1 = marcados[:]
						trazaActual = self.verificarCiclo2(ady, [], marcados1, 1, len(self.__acceptanceSets) - 1)
						if ((trazaActual != []) and (trazaActual != None)):
							return trazaActual.extend(traza)
			else:
				for ady in q.getAdyacentes():
					if ady not in marcados:
						marcados_copia = marcados[:]
						trazaActual = self.verificarCiclo1(ady, marcados_copia, N)
						if ((trazaActual != []) and (trazaActual != None)):
							return trazaActual.extend(traza)
		return []
					
	def verificarCiclo2(self, q, marcados, marcados1, n, N):
		marcados.append(q)
		traza = [q.getNodoTS().getNombre()]
		if n == N:
			if q in self.__acceptanceSets[n]:
				for ady in q.getAdyacentes():
					if ady not in marcados:
						trazaActual = self.verificarCiclo2(ady, marcados, marcados1, n, N)
						if ((trazaActual != []) and (trazaActual != None)):
							return trazaActual.extend(traza)
					if q != ady:
						trazaActual = self.verificarCiclo3(ady, [], marcados1)
						if ((trazaActual != []) and (trazaActual != None)):
							return trazaActual.extend(traza)
			else:
				for ady in q.getAdyacentes():
					if ady not in marcados:
						trazaActual = self.verificarCiclo2(ady, marcados, marcados1, n, N)
						if ((trazaActual != []) and (trazaActual != None)):
							return trazaActual.extend(traza)
		else:
			if q in self.__acceptanceSets[n]:
				for ady in q.getAdyacentes():
					if ady not in marcados:
						trazaActual = self.verificarCiclo2(ady, marcados, marcados1, n, N)
						if ((trazaActual != []) and (trazaActual != None)):
							return trazaActual.extend(traza)
					if q != ady:
						trazaActual = self.verificarCiclo2(ady, [], marcados1, n + 1, N)
						if ((trazaActual != []) and (trazaActual != None)):
							return trazaActual.extend(traza)
			else:
				for ady in q.getAdyacentes():
					if ady not in marcados:
						trazaActual = self.verificarCiclo2(ady, marcados, marcados1, n, N)
						if ((trazaActual != []) and (trazaActual != None)):
							return trazaActual.extend(traza)
		return []

	def verificarCiclo3(self, q, marcados, marcados1):
		if q in marcados1:
			return [q.getNodoTS().getNombre()]
		else:
			marcados.append(q)
			traza = [q.getNodoTS().getNombre()]
			for ady in q.getAdyacentes():
				if ady not in marcados:
					trazaActual = self.verificarCiclo3(ady, marcados, marcados1)
					if ((trazaActual != []) and (trazaActual != None)):
						return trazaActual.extend(traza)
		return []

	def imprimirProductoTSNBA(self):
		i = 1000
		print "***ESTADOS***"
		for estado in self.__estados:
			print "estado"
			print i
			print "("
			print estado.getNodoTS().getId()
			print estado.getNodoNBA().getId()
			print ")"
			print "adyacentes"
			for ady in estado.getAdyacentes():
				print "("
				print ady.getNodoTS().getId()
				print ady.getNodoNBA().getId()
				print ")"
			i += 1
		print "***INICIALES***"
		for estado in self.__iniciales:
			print "estado"
			print "("
			print estado.getNodoTS().getId()
			print estado.getNodoNBA().getId()
			print ")"
		print "***ACCEPTANCE SETS***"
		i = 1000
		for aSet in self.__acceptanceSets:
			print i
			i += 1
			for estado in aSet:
				print "estado"
				print "("
				print estado.getNodoTS().getId()
				print estado.getNodoNBA().getId()
				print ")"
			
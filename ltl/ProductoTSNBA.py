from TS import TS
from GNBA import GNBA
from ProductoTSNBANodo import ProductoTSNBANodo

class ProductoTSNBA(object):
	"Producto entre Sistema de transiciones y NBA"
	def __init__(self, ts, nba):
		#generar iniciales
		iniciales = []
		for ini in ts.getIniciales():
			for ininba in nba.getAdycentesIniciales(ini.getProposiciones()):
				nodo = ProductoTSNBANodo(ini, ininba)
				iniciales.append(nodo)
		self.__iniciales = iniciales
		#generar parte alcanzable
		self.__estados = iniciales[:]
		self.parteAlcanzable(iniciales, ts, nba)
		for i in range(0, len(self.__estados)):
			self.__estados[i].setId(i)
		self.generarAcceptanceSets(nba)
	
	def parteAlcanzable(self, estados, ts, nba):
		for q in estados:
			estadosNuevos = []
			for t_ady in q.getNodoTS().getTransiciones():
				ady = t_ady.getDestino()
				adysnba = q.getNodoNBA().getEstadosAdyacentes(ady.getProposiciones())
				for adynba in adysnba:
					if not self.perteneceEstado(ady, adynba):
						nodo = ProductoTSNBANodo(ady, adynba)
						self.__estados.append(nodo)
						q.agregarTransicion(t_ady.getAccion(), nodo)
						estadosNuevos.append(nodo)
					else:
						nodo = self.buscarEstado(ady, adynba)
						q.agregarTransicion(t_ady.getAccion(), nodo)
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
		for i in range(0, nba.cantAcceptanceSets()):
			self.__acceptanceSets.append([])
		for estado in self.__estados:
			for i in range(0, nba.cantAcceptanceSets()):
				if nba.isFinalN(estado.getNodoNBA().getId(), i):
					self.__acceptanceSets[i].append(estado)
	
	def verificar(self):
		N = len(self.__acceptanceSets)
		if N == 0:
			for ini in self.__iniciales:
				trans = ini.getTransiciones()
				for t in trans:
					traza = self.verificarCiclo0(t, [])
					if (traza != []):
						return ([ini] + traza)
			return []
		for ini in self.__iniciales:
			trans = ini.getTransiciones()
			for t in trans:
				traza = self.verificarCiclo1(t, [], N)
				if (traza != []):
					return ([ini] + traza)
		return []

	def verificarCiclo0(self, t_q, marcados):
		"Busca un ciclo y devuelve la traza correspondiente."
		q = t_q.getDestino()
		if q in marcados:
			return [t_q]
		else:
			marcados.append(q)
			for t_ady in q.getTransiciones():
				trazaActual = self.verificarCiclo0(t_ady, marcados)
				if (trazaActual != []):
					return [t_q] + trazaActual
		return []
	
	def verificarCiclo1(self, t_q, marcados, N):
		"Busca un ciclo que pase por todos los Acceptance Sets y devuelve la traza correspondiente."
		q = t_q.getDestino()
		marcados.append(q)
		traza = [t_q]
		if N == 1:
			if q in self.__acceptanceSets[0]:
				for t_ady in q.getTransiciones():
					ady = t_ady.getDestino()
					if ady not in marcados:
						marcados_copia = marcados[:]
						trazaActual = self.verificarCiclo1(t_ady, marcados_copia, N)
						if (trazaActual != []):
							return traza + trazaActual
					marcados_copia = marcados[:]
					trazaActual = self.verificarCiclo3(t_ady, [], marcados_copia)
					if (trazaActual != []):
						return traza + trazaActual
			else:
				for t_ady in q.getTransiciones():
					ady = t_ady.getDestino()
					if ady not in marcados:
						marcados_copia = marcados[:]
						trazaActual = self.verificarCiclo1(t_ady, marcados_copia, N)
						if (trazaActual != []):
							return traza + trazaActual
		else: # Si tiene mas de un acceptance set
			if q in self.__acceptanceSets[0]:
				for t_ady in q.getTransiciones():
					ady = t_ady.getDestino()
					if ady not in marcados:
						marcados_copia = marcados[:]
						trazaActual = self.verificarCiclo1(t_ady, marcados_copia, N)
						if (trazaActual != []):
							return traza + trazaActual
					# if q != ady:
					marcados_copia = marcados[:]
					trazaActual = self.verificarCiclo2(t_ady, [], marcados_copia, 1, len(self.__acceptanceSets) - 1)
					if (trazaActual != []):
						return traza + trazaActual
			else:
				for t_ady in q.getTransiciones():
					ady = t_ady.getDestino()
					if ady not in marcados:
						marcados_copia = marcados[:]
						trazaActual = self.verificarCiclo1(t_ady, marcados_copia, N)
						if (trazaActual != []):
							return traza + trazaActual
		return []
					
	def verificarCiclo2(self, t_q, marcados, marcados1, n, N):
		q = t_q.getDestino()
		marcados.append(q)
		traza = [t_q]
		if n == N:
			if q in self.__acceptanceSets[n]:
				for t_ady in q.getTransiciones():
					ady = t_ady.getDestino()
					if ady not in marcados:
						marcados_copia = marcados[:]
						trazaActual = self.verificarCiclo2(t_ady, marcados_copia, marcados1, n, N)
						if (trazaActual != []):
							return traza + trazaActual
					# if q != ady:
					trazaActual = self.verificarCiclo3(t_ady, [], marcados1)
					if (trazaActual != []):
						return traza + trazaActual
			else:
				for t_ady in q.getTransiciones():
					ady = t_ady.getDestino()
					if ady not in marcados:
						marcados_copia = marcados[:]
						trazaActual = self.verificarCiclo2(t_ady, marcados_copia, marcados1, n, N)
						if (trazaActual != []):
							return traza + trazaActual
		else:
			if q in self.__acceptanceSets[n]:
				for t_ady in q.getTransiciones():
					ady = t_ady.getDestino()
					if ady not in marcados:
						marcados_copia = marcados[:]
						trazaActual = self.verificarCiclo2(t_ady, marcados_copia, marcados1, n, N)
						if (trazaActual != []):
							return traza + trazaActual
					# if q != ady:
					trazaActual = self.verificarCiclo2(t_ady, [], marcados1, n + 1, N)
					if (trazaActual != []):
						return traza + trazaActual
			else:
				for t_ady in q.getTransiciones():
					ady = t_ady.getDestino()
					if ady not in marcados:
						marcados_copia = marcados[:]
						trazaActual = self.verificarCiclo2(t_ady, marcados_copia, marcados1, n, N)
						if (trazaActual != []):
							return traza + trazaActual
		return []

	def verificarCiclo3(self, t_q, marcados, marcados1):
		q = t_q.getDestino()
		if q in marcados1:
			return [t_q]
		else:
			marcados.append(q)
			traza = [t_q]
			for t_ady in q.getTransiciones():
				ady = t_ady.getDestino()
				if ady not in marcados:
					trazaActual = self.verificarCiclo3(t_ady, marcados, marcados1)
					if (trazaActual != []):
						return traza + trazaActual
		return []

	def imprimirTraza(self, traza):
		for x in traza:
			x.imprimirTraza()
	
	def imprimirProductoTSNBA(self):
		print '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml>
  <graph edgedefault="directed" id="G">'''
		for estado in self.__estados:
			if estado in self.__iniciales:
				print '''<node id="n''', estado.getId(), '''">
      <data>
        <y:ShapeNode>
          <y:Fill color="#FFCC00" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" modelName="internal" visible="true">INI_''', estado.getNodoNBA().getFormulasString(), '''</y:NodeLabel>
          <y:Shape type="rectangle"/>
        </y:ShapeNode>
      </data>
    </node>'''
			else:
				print '''<node id="n''', estado.getId(), '''">
      <data>
        <y:ShapeNode>
          <y:Fill color="#FFCC00" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" modelName="internal" visible="true">''', estado.getNodoNBA().getFormulasString(), '''</y:NodeLabel>
          <y:Shape type="rectangle"/>
        </y:ShapeNode>
      </data>
    </node>'''
		for estado in self.__estados:
			for trans in estado.getTransiciones():
				print '''<edge id="e0" source="n''', estado.getId(), '''" target="n''', trans.getDestino().getId(), '''">
      <data>
        <y:PolyLineEdge>
          <y:LineStyle color="#000000" type="line" width="1.0"/>
          <y:Arrows source="none" target="standard"/>
        </y:PolyLineEdge>
      </data>
    </edge>'''
		print '''  </graph>
</graphml>'''
		
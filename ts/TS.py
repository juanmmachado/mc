from TSEstado import TSEstado

class TS(object):
	"Sistema de transiciones"
	def __init__(self, estados, iniciales):
		self.__estados = []
		self.__iniciales = []
		# genero estados
		idEstado = 0
		for props in estados:
			nuevo = TSEstado(props, idEstado)
			self.__estados.append(nuevo)
			# los que son iniciales los agrego a iniciales
			if idEstado in iniciales:
				self.__iniciales.append(nuevo)
			idEstado += 1
	
	def agregarTransicionId(self, origen, accion, destino):
		"Agrega la transicion por Id de estado"
		estOrigen = self.buscarEstadoId(origen)
		estDestino = self.buscarEstadoId(destino)
		estOrigen.agregarAdyacente(accion, estDestino)
	
	def getEstados(self):
		"Devuelve un alias al conjunto de estados"
		return self.__estados
	
	def getIniciales(self):
		"Devuelve un alias al conjunto de estados iniciales"
		return self.__iniciales
	
	def buscarEstadoId(self, id):
		"Devuelve el estado por Id de estado"
		if id < len(self.__estados):
			return self.__estados[id]
		return None
	
	def agregarEstado(self, id, props):
		"Agrega un nuevo estado (el Id se asigna manualmente)"
		props_str = []
		for prop in props:
			props_str.append(str(prop))
		nuevo = TSEstado(props_str, id)
		self.__estados.append(nuevo)

	def insertarEstados(self, estados, iniciales):
		"Agrega una lista de estados creados previamente."
		self.__estados = estados
		self.__iniciales = iniciales

	def agregarEstadoInicial(self, id, props):
		"Agrega un nuevo estado (el Id se asigna manualmente). No lo agrega al conjunto de estados"
		props_str = []
		for prop in props:
			props_str.append(str(prop))
		nuevo = TSEstado(props_str, id)
		self.__estados.append(nuevo)
		self.__iniciales.append(nuevo)

	def getSatAtomica(self, at):
		"Devuelve el conjunto de estados que satisfacen la formula atomica at"
		sat = []
		for estado in self.__estados:
			if (estado.satAtomica(at)):
				sat.append(estado)
		return sat
	
	def getPost(self, estado):
		"Devuelve el conjunto de estados posteriores a estado"
		return estado.getEstadosAdyacentes()
	
	def getPre(self, estado):
		"Devuelve el conjunto de estados predecesores a estado"
		pre = []
		for estadoPre in self.__estados:
			if estado in estadoPre.getEstadosAdyacentes():
				pre.append(estadoPre)
		return pre
		
	def getAcciones(self):
		acc = []
		h = Herramientas()
		for e in self.__estados:
			h.combinarListas(acc, e.getAccionesPosibles())
		return acc
	
	def intercaladoTS(self, ts):
		iniciales = []
		idEstado = 0
		for ini1 in self.__iniciales:
			ts_iniciales = ts.getIniciales()
			for ini2 in ts_iniciales:
				iniciales.append(((TSEstado(ini1.getProposiciones() + ini2.getProposiciones(), idEstado)), ini1, ini2))
				idEstado += 1
		estados = iniciales[:]
		self.parteAlcanzableIntercaladoTS(estados, iniciales, idEstado)
		#genero TS
		ts_nuevo = TS([],[])
		#inserto los estados generados
		estadosIns = []
		idEstado = 0
		for e in estados:
			(p, e1, e2) = e
			p.setId(idEstado)
			idEstado += 1
			estadosIns.append(p)
		inicialesIns = []
		for e in iniciales:
			(p, e1, e2) = e
			inicialesIns.append(p)
		ts_nuevo.insertarEstados(estadosIns, inicialesIns)
		return ts_nuevo
	
	def productoSynTS(self, ts, syn):
		iniciales = []
		for ini1 in self.__iniciales:
			ts_iniciales = ts.getIniciales()
			for ini2 in ts_iniciales:
				iniciales.append(((TSEstado(ini1.getProposiciones() + ini2.getProposiciones(), 0)), ini1, ini2))
		estados = iniciales[:]
		self.parteAlcanzableProductoSynTS(estados, iniciales, syn)
		#genero TS
		ts_nuevo = TS([],[])
		#inserto los estados generados
		estadosIns = []
		idEstado = 0
		for e in estados:
			(p, e1, e2) = e
			p.setId(idEstado)
			idEstado += 1
			estadosIns.append(p)
		inicialesIns = []
		for e in iniciales:
			(p, e1, e2) = e
			inicialesIns.append(p)
		ts_nuevo.insertarEstados(estadosIns, inicialesIns)
		return ts_nuevo
	
	def parteAlcanzableIntercaladoTS(self, estados, estadosActuales, idEstado):
		for q in estadosActuales:
			(p, e1, e2) = q
			estadosNuevos = []
			for t1_ady in e1.getTransiciones():
				# acciones solo de ts1
				nuevo_e1 = t1_ady.getDestino()
				if not self.perteneceEstadoLista(estados, nuevo_e1, e2):
					nuevo_p = TSEstado(nuevo_e1.getProposiciones() + e2.getProposiciones(), idEstado)
					idEstado += 1
					p.agregarAdyacente(t1_ady.getAccion(), nuevo_p)
					estadosNuevos.append((nuevo_p, nuevo_e1, e2))
					estados.append((nuevo_p, nuevo_e1, e2))
				else:
					nuevo_p = self.buscarEstadoLista(estados, nuevo_e1, e2)
					p.agregarAdyacente(t1_ady.getAccion(), nuevo_p)
			for t2_ady in e2.getTransiciones():
				# acciones de ts2
				nuevo_e2 = t2_ady.getDestino()
				if not self.perteneceEstadoLista(estados, e1, nuevo_e2):
					nuevo_p = TSEstado(e1.getProposiciones() + nuevo_e2.getProposiciones(), idEstado)
					idEstado += 1
					p.agregarAdyacente(t2_ady.getAccion(), nuevo_p)
					estadosNuevos.append((nuevo_p, e1, nuevo_e2))
					estados.append((nuevo_p, e1, nuevo_e2))
				else:
					nuevo_p = self.buscarEstadoLista(estados, e1, nuevo_e2)
					p.agregarAdyacente(t2_ady.getAccion(), nuevo_p)
			self.parteAlcanzableIntercaladoTS(estados, estadosNuevos, idEstado)

	def parteAlcanzableProductoSynTS(self, estados, estadosActuales, syn):
		for q in estadosActuales:
			(p, e1, e2) = q
			estadosNuevos = []
			for t1_ady in e1.getTransiciones():
				if t1_ady.getAccion() in syn:
					# acciones sincronizadas
					for t2_ady in e2.getTransicionesAccion(t1_ady.getAccion()):
						nuevo_e1 = t1_ady.getDestino()
						nuevo_e2 = t2_ady.getDestino()
						if not self.perteneceEstadoLista(estados, nuevo_e1, nuevo_e2):
							nuevo_p = TSEstado(nuevo_e1.getProposiciones() + nuevo_e2.getProposiciones(), 0)
							p.agregarAdyacente(t1_ady.getAccion(), nuevo_p)
							estadosNuevos.append((nuevo_p, nuevo_e1, nuevo_e2))
							estados.append((nuevo_p, nuevo_e1, nuevo_e2))
						else:
							nuevo_p = self.buscarEstadoLista(estados, nuevo_e1, nuevo_e2)
							p.agregarAdyacente(t1_ady.getAccion(), nuevo_p)
				else:
					# acciones solo de ts1
					nuevo_e1 = t1_ady.getDestino()
					if not self.perteneceEstadoLista(estados, nuevo_e1, e2):
						nuevo_p = TSEstado(nuevo_e1.getProposiciones() + e2.getProposiciones(), 0)
						p.agregarAdyacente(t1_ady.getAccion(), nuevo_p)
						estadosNuevos.append((nuevo_p, nuevo_e1, e2))
						estados.append((nuevo_p, nuevo_e1, e2))
					else:
						nuevo_p = self.buscarEstadoLista(estados, nuevo_e1, e2)
						p.agregarAdyacente(t1_ady.getAccion(), nuevo_p)
			for t2_ady in e2.getTransiciones():
				if t2_ady.getAccion() not in syn:
					# acciones solo de ts2
					nuevo_e2 = t2_ady.getDestino()
					if not self.perteneceEstadoLista(estados, e1, nuevo_e2):
						nuevo_p = TSEstado(e1.getProposiciones() + nuevo_e2.getProposiciones(), 0)
						p.agregarAdyacente(t2_ady.getAccion(), nuevo_p)
						estadosNuevos.append((nuevo_p, e1, nuevo_e2))
						estados.append((nuevo_p, e1, nuevo_e2))
					else:
						nuevo_p = self.buscarEstadoLista(estados, e1, nuevo_e2)
						p.agregarAdyacente(t2_ady.getAccion(), nuevo_p)
			self.parteAlcanzableProductoSynTS(estados, estadosNuevos, syn)

	def perteneceEstadoLista(self, lista, est1, est2):
		for item in lista:
			(p, e1, e2) = item
			if ((e1 == est1) and (e2 == est2)):
				return True
		return False
	
	def buscarEstadoLista(self, lista, est1, est2):
		for item in lista:
			(p, e1, e2) = item
			if ((e1 == est1) and (e2 == est2)):
				return p

	def imprimirTraza(self, traza):
		for x in traza:
			x.imprimirTraza()
	
	def guardarTS(self, arch):
		try:
		# if True:
			
			gml = open(arch, "w")
			gml.write('''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:y="http://www.yworks.com/xml/graphml" xmlns:yed="http://www.yworks.com/xml/yed/3" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
  <graph edgedefault="directed" id="G">''')
			for estado in self.__estados:
				props = estado.getProposiciones()
				proposiciones = ""
				if props != []:
					proposiciones = props[0]
				for i in range(1, len(props)):
					proposiciones = proposiciones + "," + props[i]
				if estado in self.__iniciales:
					gml.write('''
	<node id="n''' + str(estado.getId()) + '''">
      <data>
        <y:ShapeNode>
          <y:Fill color="#FFCC00" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" modelName="internal" visible="true">INI_''' + proposiciones + '''</y:NodeLabel>
          <y:Shape type="rectangle"/>
        </y:ShapeNode>
      </data>
    </node>''')
				else:
					gml.write('''
	<node id="n''' + str(estado.getId()) + '''">
      <data>
        <y:ShapeNode>
          <y:Fill color="#FFCC00" transparent="false"/>
          <y:BorderStyle color="#000000" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" modelName="internal" visible="true">''' + proposiciones + '''</y:NodeLabel>
          <y:Shape type="rectangle"/>
        </y:ShapeNode>
      </data>
    </node>''')
			idTrans = 0
			for estado in self.__estados:
				for trans in estado.getTransiciones():
					gml.write('''
	<edge id="e''' + str(idTrans) + '''" source="n''' + str(estado.getId()) + '''" target="n''' + str(trans.getDestino().getId()) + '''">
      <data>
        <y:PolyLineEdge>
          <y:LineStyle color="#000000" type="line" width="1.0"/>
          <y:Arrows source="none" target="standard"/>
		  <y:EdgeLabel>''' + str(trans.getAccion()) + '''</y:EdgeLabel>
        </y:PolyLineEdge>
      </data>
    </edge>''')
					idTrans += 1
			gml.write('''
  </graph>
</graphml>''')
			gml.close()
		
		except:
		# else:
			print "ERROR: No se pudo abrir el archivo graphml."

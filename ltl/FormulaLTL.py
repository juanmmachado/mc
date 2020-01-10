class FormulaLTL(object):
	"Formula LTL"
	def perteneceLista(self, listaForms):
		for f in listaForms:
			if self.compararFormula(f):
				return True
		return False

	def getSubFormulas(self):
		"Devuelve el conjunto de todas las subformulas."
		pass
		
	def getSubFormulasPositivas(self):
		"Devuelve el conjunto de todas las subformulas cuyo conectivo principal no es una negacion."
		pass
	
	def getAtomicas(self):
		"Devuelve el conjunto de todas las subformulas atomicas."
		pass
	
	def verificaAtomica(self, nombre):
		pass

	def normalizar(self):
		pass
		
	def negar(self):
		from FormulaLTLNegacion import FormulaLTLNegacion
		return FormulaLTLNegacion(self)
	
	def obtenerUntils(self, listaFormulas):
		"Devuelve todas las formulas de la lista cuyo conectivo principal es el conectivo Until."
		from FormulaLTLUntil import FormulaLTLUntil
		untils = []
		for formula in listaFormulas:
			if isinstance(formula, FormulaLTLUntil):
				untils.append(formula)
		return untils

	def obtenerNexts(self, listaFormulas):
		"Devuelve todas las formulas de la lista cuyo conectivo principal es el conectivo Next."
		from FormulaLTLNext import FormulaLTLNext
		nexts = []
		for formula in listaFormulas:
			if isinstance(formula, FormulaLTLNext):
				nexts.append(formula)
		return nexts

	def normalizarNegacion(self):
		"Normaliza la doble negacion."
		from FormulaLTLNegacion import FormulaLTLNegacion
		if isinstance(self, FormulaLTLNegacion):
			return self.getSubFormula()
		else:
			return FormulaLTLNegacion(self)

	def obtenerNombresAtomicas(self, formulas):
		"Devuelve los nombres de todas las formulas atomicas de la lista."
		atomicas = []
		for f in formulas:
			nombre = f.obtenerNombreAtomica()
			if (nombre != ""):
				atomicas.append(nombre)
		return atomicas
	
	def obtenerNombresNegacionesAtomicas(self, formulas):
		"Devuelve los nombres de todas las formulas atomicas que se encuentran negadas en la lista."
		negs = []
		for f in formulas:
			nombre = f.obtenerNombreNegacionAtomica()
			if (nombre != ""):
				negs.append(nombre)
		return negs

	def verificarTrazaV(self, traza):
		"Recorta la traza"
		pass
		
	def verificarTrazaF(self, traza):
		"Recorta la traza"
		pass
	
	def verificarTrazaVTrans(self, traza):
		"Recorta la traza"
		pass
		
	def verificarTrazaFTrans(self, traza):
		"Recorta la traza"
		pass
	
	# def verificarTrazaV_formulas(self, traza, forms):
		# "Recorta la traza por el OR de todas las formulas"
		# if traza == []:
			# return traza
		# min = len(traza)
		# for f in forms:
			# aux = len(f.verificarTrazaV(traza))
			# if aux < min:
				# min = aux
		# return traza[0:min]
		
	# def verificarTrazaF_formulas(self, traza, forms):
		# "Recorta la traza en el punto en donde alguna de las formulas de forms se hace falsa"
		# for f in forms:
			# res = f.verificarTrazaF(traza)
			# if res != traza:
				# return res
		# return traza
		
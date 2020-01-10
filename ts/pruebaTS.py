from TS import TS

class pruebaTS(object):
	def __init__(self):
		pass
	
	def prueba1(self):
		# genero TS1
		print "##############genero ts1##############"
		ts1 = TS([["noncrit_1"], ["crit_1"]], [0])
		ts1.agregarTransicionId(0, "request", 1)
		ts1.agregarTransicionId(1, "release", 0)
		ts1.guardarTS("prueba_ts1.graphml")
		# genero TS2
		print "##############genero ts2##############"
		ts2 = TS([["noncrit_2"], ["crit_2"]], [0])
		ts2.agregarTransicionId(0, "request", 1)
		ts2.agregarTransicionId(1, "release", 0)
		ts2.guardarTS("prueba_ts2.graphml")
		# genero TS3
		print "##############genero ts3##############"
		ts3 = TS([["unlock"], ["lock"]], [0])
		ts3.agregarTransicionId(0, "request", 1)
		ts3.agregarTransicionId(1, "release", 0)
		ts3.guardarTS("prueba_ts3.graphml")
		# intercalado
		print "##############intercalado##############"
		ts_int = ts1.intercaladoTS(ts2)
		ts_int.guardarTS("prueba_intercalado.graphml")
		print "##############producto syn##############"
		ts_syn = ts_int.productoSynTS(ts3, ["request", "release"])
		print "##############imprimir##############"
		ts_syn.guardarTS("prueba_Handshaking.graphml")

	def prueba2(self):
		# genero TS1
		print "##############genero ts1##############"
		ts1 = TS([["noncrit_1"], ["wait_1"], ["crit_1"]], [0])
		ts1.agregarTransicionId(0, "", 1)
		ts1.agregarTransicionId(1, "request", 2)
		ts1.agregarTransicionId(2, "release", 0)
		print "##############imprimir##############"
		ts1.guardarTS("prueba2.graphml")

	def prueba3(self):
		# genero TS1
		print "##############genero ts1##############"
		ts = TS([["red"], ["yellow"], ["green"], ["yellow"]], [0])
		ts.agregarTransicionId(0, "", 1)
		ts.agregarTransicionId(1, "", 2)
		ts.agregarTransicionId(2, "", 3)
		ts.agregarTransicionId(3, "", 0)
		ts.guardarTS("prueba_tl.graphml")
	
import sys
sys.path.append('./ts')
sys.path.append('./ltl')
sys.path.append('./ctl')
sys.path.append("./parser/ply-3.4")
from ltl.LTLMC import LTLMC
from ctl.CTLMC import CTLMC
import ltl.parserLTL
import ctl.parserCTL
from ts.TS import TS
from ts.ParserGraphML_yEd import ParserGraphML_yEd

if (len(sys.argv) < 2):
	print "Uso incorrecto."
	print "Opciones: ic, hs, ltl, ctl"

elif (sys.argv[1] == "ic"):
	if (len(sys.argv) != 5):
		print "Uso incorrecto."
		print "Uso: ic <ts1.graphml> <ts2.graphml> <intercalado.graphml>"
	else:
		parserGML = ParserGraphML_yEd()
		ts1 = parserGML.parsearTS(sys.argv[2])
		parserGML = ParserGraphML_yEd()
		ts2 = parserGML.parsearTS(sys.argv[3])

		ts = ts1.intercaladoTS(ts2)
		ts.guardarTS(sys.argv[4])

elif (sys.argv[1] == "hs"):
	if (len(sys.argv) != 6):
		print "Uso incorrecto."
		print "Uso: hs <ts1.graphml> <ts2.graphml> <acciones de sincronizacion> <handshaking.graphml>"
	else:
		parserGML = ParserGraphML_yEd()
		ts1 = parserGML.parsearTS(sys.argv[2])
		parserGML = ParserGraphML_yEd()
		ts2 = parserGML.parsearTS(sys.argv[3])
		# acciones = ["subir", "bajar", "llego_abajo", "llego_arriba"]
		ts = ts1.productoSynTS(ts2, sys.argv[4].split(','))
		ts.guardarTS(sys.argv[5])

elif (sys.argv[1] == "ltl"):
	if (len(sys.argv) != 4):
		print "Uso incorrecto."
		print "Uso: ltl <ts.graphml> <propiedad LTL>"
	else:
		parserGML = ParserGraphML_yEd()
		ts = parserGML.parsearTS(sys.argv[2])
		prop = ltl.parserLTL.parsearFormulaLTL(sys.argv[3])
		mc = LTLMC()
		mc.verificar(ts, prop)

elif (sys.argv[1] == "ctl"):
	if (len(sys.argv) != 4):
		print "Uso incorrecto."
		print "Uso: ctl <ts.graphml> <propiedad LTL>"
	else:
		parserGML = ParserGraphML_yEd()
		ts = parserGML.parsearTS(sys.argv[2])
		prop = ctl.parserCTL.parsearFormulaCTL(sys.argv[3])
		mc = CTLMC()
		mc.verificar(ts, prop)

else:
	print "Uso incorrecto."
	print "Opciones: ic, hs, ltl, ctl"

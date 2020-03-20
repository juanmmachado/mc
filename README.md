# Este verificador de modelos implementa operaciones entre sistemas de tran- siciones, de forma de poder trabajar con sistemas de transiciones complejos generados a partir de otros mas simples. Las operaciones implementadas son el Intercalado y el Handshaking.

# Intercalado
python MC.py ic <TS1.graphml> <TS2.graphml> <intercalado.graphml>
# Donde TS1.graphml y TS2.graphml son archivos previamente generados en los cuales se representan sistemas de transiciones en formato GraphML, e intercalado.graphml indica el archivo en el cual se escribira el sistema de transiciones resultado del intercalado.

# Handshaking
python MC.py hs <TS1.graphml> <TS2.graphml> <handshaking.graphml>
# Donde TS1.graphml y TS2.graphml son archivos previamente generados en los cuales se representan sistemas de transiciones en formato GraphML, y handshaking.graphml indica el archivo en el cual se escribira ́ el sistema de transiciones resultado del Handshaking.


# Verificar propiedades en LTL
python MC.py ltl <archivo.graphml> <formula LTL>
# Donde archivo.graphml es el archivo donde se encuentra representado el sistema de transiciones y formula LTL es la formula LTL expresada segun la seccion 6.6.1.


# Verificar propiedades en CTL
python MC.py ctl <archivo.graphml> <formula CTL>
# Donde archivo.graphml es el archivo donde se encuentra representado el sistema de transiciones y formula CTL es la formula CTL expresada segun la seccion 6.6.2.

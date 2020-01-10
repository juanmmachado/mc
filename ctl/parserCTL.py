from FormulaCTLAtomica import FormulaCTLAtomica
from FormulaCTLTrue import FormulaCTLTrue
from FormulaCTLExisteNext import FormulaCTLExisteNext
from FormulaCTLExisteAlways import FormulaCTLExisteAlways
from FormulaCTLExisteEventually import FormulaCTLExisteEventually
from FormulaCTLNegacion import FormulaCTLNegacion
from FormulaCTLConjuncion import FormulaCTLConjuncion
from FormulaCTLCondicion import FormulaCTLCondicion
from FormulaCTLDisyuncion import FormulaCTLDisyuncion
from FormulaCTLExisteUntil import FormulaCTLExisteUntil
from FormulaCTLParaTodoNext import FormulaCTLParaTodoNext
from FormulaCTLParaTodoAlways import FormulaCTLParaTodoAlways
from FormulaCTLParaTodoEventually import FormulaCTLParaTodoEventually
from FormulaCTLParaTodoUntil import FormulaCTLParaTodoUntil

import sys

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'NAME', 'TRUE',
    'EXINEXT', 'EXIALWAYS', 'EXIEVENTUALLY', 'FANEXT', 'FAALWAYS', 'FAEVENTUALLY', 'NOT',
    'EXIUNTIL', 'FAUNTIL', 'AND', 'OR', 'THEN',
    'LPAREN', 'RPAREN',
    )

# Tokens

t_TRUE    = r'TRUE'
t_EXINEXT    = r'EO'
t_EXIALWAYS    = r'E\[\]'
t_EXIEVENTUALLY    = r'E<>'
t_FANEXT    = r'AO'
t_FAALWAYS    = r'A\[\]'
t_FAEVENTUALLY    = r'A<>'
t_AND    = r'/\\'
t_OR    = r'\\/'
t_THEN    = r'->'
t_NOT    = r'-'
t_EXIUNTIL    = r'EU'
t_FAUNTIL    = r'AU'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NAME    = r'[a-z_][a-z0-9_]*'

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

precedence = (
    ('right','EXINEXT','EXIALWAYS','EXIEVENTUALLY','FANEXT','FAALWAYS','FAEVENTUALLY'),
    ('right','EXIUNTIL','FAUNTIL'),
    ('right','NOT'),
    ('right','AND','OR'),
    ('right','THEN'),
    )

# dictionary of names
names = { }

def p_statement_expr(t):
    'statement : expression'
    t[0] = t[1]

def p_expression_exiuntil(t):
    'expression : expression EXIUNTIL expression'
    t[0] = FormulaCTLExisteUntil(t[1], t[3])

def p_expression_fauntil(t):
    'expression : expression FAUNTIL expression'
    t[0] = FormulaCTLParaTodoUntil(t[1], t[3])

def p_expression_and(t):
    'expression : expression AND expression'
    t[0] = FormulaCTLConjuncion(t[1], t[3])

def p_expression_or(t):
    'expression : expression OR expression'
    t[0] = FormulaCTLDisyuncion(t[1], t[3])

def p_expression_then(t):
    'expression : expression THEN expression'
    t[0] = FormulaCTLCondicion(t[1], t[3])
    
def p_expression_exinext(t):
    'expression : EXINEXT expression'
    t[0] = FormulaCTLExisteNext(t[2])
    
def p_expression_exialways(t):
    'expression : EXIALWAYS expression'
    t[0] = FormulaCTLExisteAlways(t[2])
    
def p_expression_exieventually(t):
    'expression : EXIEVENTUALLY expression'
    t[0] = FormulaCTLExisteEventually(t[2])

def p_expression_fanext(t):
    'expression : FANEXT expression'
    t[0] = FormulaCTLParaTodoNext(t[2])
    
def p_expression_faalways(t):
    'expression : FAALWAYS expression'
    t[0] = FormulaCTLParaTodoAlways(t[2])
    
def p_expression_faeventually(t):
    'expression : FAEVENTUALLY expression'
    t[0] = FormulaCTLParaTodoEventually(t[2])
    
def p_expression_not(t):
    'expression : NOT expression'
    t[0] = FormulaCTLNegacion(t[2])

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_name(t):
    'expression : NAME'
    t[0] = FormulaCTLAtomica(t[1])

def p_expression_true(t):
    'expression : TRUE'
    t[0] = FormulaCTLTrue()
	
def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()

def parsearFormulaCTL(formula):
    return yacc.parse(formula)

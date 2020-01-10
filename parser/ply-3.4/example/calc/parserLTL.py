from FormulaLTLAtomica import FormulaLTLAtomica
from FormulaLTLNext import FormulaLTLNext
from FormulaLTLAlways import FormulaLTLAlways
from FormulaLTLEventually import FormulaLTLEventually
from FormulaLTLNegacion import FormulaLTLNegacion
from FormulaLTLConjuncion import FormulaLTLConjuncion
from FormulaLTLDisyuncion import FormulaLTLDisyuncion
from FormulaLTLUntil import FormulaLTLUntil

# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------
import sys
sys.path.insert(0,"./parser/ply-3.4")

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'NAME', 'TRUE',
    'NEXT', 'ALWAYS', 'EVENTUALLY', 'NOT',
    'UNTIL','AND', 'OR', 'THEN',
    'LPAREN', 'RPAREN',
    )

# Tokens

t_TRUE    = r'TRUE'
t_NEXT    = r'O'
t_ALWAYS    = r'\[\]'
t_EVENTUALLY    = r'<>'
t_AND    = r'/\\'
t_OR    = r'\\/'
t_THEN    = r'->'
t_NOT    = r'-'
t_UNTIL    = r'U'
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
    ('right','NEXT','ALWAYS','EVENTUALLY'),
    ('right','UNTIL'),
    ('right','NOT'),
    ('right','AND','OR'),
    ('right','THEN'),
    )

# dictionary of names
names = { }

def p_statement_expr(t):
    'statement : expression'
    t[0] = t[1]
    print("nada")

def p_expression_until(t):
    'expression : expression UNTIL expression'
    t[0] = FormulaLTLUntil(t[1], t[3])
    print("until")

def p_expression_and(t):
    'expression : expression AND expression'
    t[0] = FormulaLTLConjuncion(t[1], t[3])
    print("and")

def p_expression_or(t):
    'expression : expression OR expression'
    t[0] = FormulaLTLDisyuncion(t[1], t[3])
    print("or")

def p_expression_then(t):
    'expression : expression THEN expression'
    t[0] = FormulaLTLDisyuncion(t[1], t[3])
    print("then")
    
    
def p_expression_next(t):
    'expression : NEXT expression'
    t[0] = FormulaLTLNext(t[2])
    print("next")
    
def p_expression_always(t):
    'expression : ALWAYS expression'
    t[0] = FormulaLTLAlways(t[2])
    print("always")
    
def p_expression_eventually(t):
    'expression : EVENTUALLY expression'
    t[0] = FormulaLTLEventually(t[2])
    print("eventually")
    
def p_expression_not(t):
    'expression : NOT expression'
    t[0] = FormulaLTLNegacion(t[2])
    print("not")

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]
    print("parentesis")

#def p_expression_number(t):
#    'expression : NUMBER'
#    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    t[0] = FormulaLTLAtomica(t[1])
    print("atomica")

def p_expression_true(t):
    'expression : TRUE'
    t[0] = FormulaLTLAtomica(t[1])
    print("true")
	
def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = input('formula > ')   # Use raw_input on Python 2
    except EOFError:
        break
    yacc.parse(s).imprimirFormula()

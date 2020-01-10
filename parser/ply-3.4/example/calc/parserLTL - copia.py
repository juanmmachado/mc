from FormulaLTLAtomica import FormulaLTLAtomica
from FormulaLTLNext import FormulaLTLNext
from FormulaLTLNegacion import FormulaLTLNegacion
from FormulaLTLConjuncion import FormulaLTLConjuncion
from FormulaLTLUntil import FormulaLTLUntil

# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------
import sys
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'NAME',
    )

# literals = ['S','\[\]','<>','U','N', '/\\', '\\/', '->', '(',')']
literals = ['S','A','E','U','N', 'Y', 'O', 'I', '(',')']
	
# Tokens

t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

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
    ('right','S','A','E'),
    ('right','U'),
    ('right','N'),
    ('right','Y','O'),
    ('right','I'),
    )

# dictionary of names
names = { }

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression 'U' expression
                  | expression 'Y' expression
                  | expression 'O' expression
                  | expression 'I' expression'''
    if t[2] == 'U'  : t[0] = FormulaLTLUntil(t[1], t[3])
    elif t[2] == 'Y': t[0] = FormulaLTLConjuncion(t[1], t[3])
    elif t[2] == 'O': t[0] = FormulaLTLDisyuncion(t[1], t[3])
    elif t[2] == 'I': t[0] = FormulaLTLCondicional(t[1], t[3])


def p_expression_unop(t):
    '''expression : 'S' expression
                  | 'A' expression
                  | 'E' expression
                  | 'N' expression'''
    if t[1] == 'S'  : t[0] = FormulaLTLNext(t[2])
    elif t[1] == 'A': t[0] = FormulaLTLAlways(t[2])
    elif t[1] == 'E': t[0] = FormulaLTLEventually(t[2])
    elif t[1] == 'N': t[0] = FormulaLTLNegacion(t[2])

def p_expression_group(t):
    '''expression : '(' expression ')' '''
    t[0] = t[2]

#def p_expression_number(t):
#    'expression : NUMBER'
#    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    t[0] = FormulaLTLAtomica(t[1])
 
def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = input('formula > ')   # Use raw_input on Python 2
    except EOFError:
        break
    yacc.parse(s)

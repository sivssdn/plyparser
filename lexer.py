import ply.lex as lex

tokens = (
   'NUMBER',
   'INT',
   'BEGIN',
   'END',
   'COMMA',
   'EQUALS',
   'ID',
   'EOL',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
)

t_EQUALS = r'='
t_COMMA = r','
t_BEGIN = r'begin'
t_END = r'end'
t_INT = r'int'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ID    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_EOL = r';'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Error in character: ", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()



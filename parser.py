import ply.yacc as yacc
from lexer import tokens

def p_program(p):
	'''program : 'begin:' stmt 'end' '''
def p_stmt(p):
	'''stmt : INT expr ';' 
			| expression';'
			'''
def p_expr(p):
	'''expr : ID
			| ID ',' expr
			| ID = NUMBER ',' expr
			| ID = NUMBER
	'''	

def p_expression(p):
		'''expression : ID = term
		'''
		
def p_term(p):
	'''
		term : NUMBER
			| ID
			| NUMBER PLUS term
			| ID PLUS term
			
	'''
import ply.yacc as yacc
from lexer import tokens

def p_program(p):
	'''program : BEGIN stmt END '''
def p_stmt(p):
	'''stmt : INT expr EOL 
			| expression EOL
			'''
def p_expr(p):
	'''expr : ID
			| ID COMMA expr
			| ID EQUALS NUMBER COMMA expr
			| ID EQUALS NUMBER
	'''	

def p_expression(p):
		'''expression : ID EQUALS term
		'''
		
def p_term(p):
	'''
		term : NUMBER
			| ID
			| NUMBER PLUS term
			| ID PLUS term
			
	'''
	
yacc.yacc()
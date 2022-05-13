import ply.yacc as yacc
from analisadorLexico import *
#import SintaxeAbstrata as sa

def p_class(p):
    '''class : visibility CLASS ID LBRACE body_class RBRACE'''

#body_class 
def p_body_class(p):
  '''body_class : attribute 
              | method
              | attribute body_class 
              | method body_class 
  '''

#attribute
def p_attribute(p):
  '''attribute : visibility type ID ASSIGNMENT exp SEMICOLON 
            | visibility type ID SEMICOLON 
            | type ID ASSIGNMENT exp SEMICOLON 
            | type ID SEMICOLON
  '''

def p_constant(p):
  '''constant : '''
  
def p_type(p):
  '''type : INT 
        | ID 
        | STRING
  '''
#method
def p_method(p):
 '''method : signature body'''

#signature
def p_signature(p):
  '''signature : visibility ID ID LPAREN sigparams RPAREN
             | visibility ID ID LPAREN RPAREN'''
    
#sigParams
def p_sigparams(p):
  '''sigparams : type ID 
             | type ID COMMA sigparams
  '''

#body
def p_body(p):
  ''' body : LBRACE stms RBRACE
           | LBRACE RBRACE
  '''

def p_visibility(p):
  '''visibility : PUBLIC'''

def p_stms(p):
  '''stms : stm 
        | stm stms'''

def p_stm(p):
  '''stm : ID'''

def p_exp(p):
  '''exp : '''
#def p_exp_call(p):
 #   '''exp : call
  #          | NUMBER
   #         | ID
    #        | TRUE
     #       | FALSE'''
  
def p_call(p):
  '''call : ID LPAREN params RPAREN
        | ID LPAREN RPAREN'''

def p_params(p):
  '''params : exp COMMA params
            | exp '''
#def p_exp1_soma(p):
 #   '''exp1 : exp1 PLUS exp2
  #       | exp2'''
  

#def p_exp2_vezes(p):
 # '''exp2 : exp2 TIMES exp3
  #        | exp3'''
  

#def p_exp4_call(p):
 # '''exp4 : call
  #        | NUMBER
   #       | ID
    #      | TRUE
     #     | FALSE'''
  #if isinstance(p[1], sa.Call):
   #     p[0] = sa.CallExp(p[1])
    #elif isinstance(p[1], int):
     #   p[0] = sa.NumExp(p[1])
    #elif (p[1] == 'true' or p[1] == 'false'):
     #   p[0] = sa.BooleanExp(p[1])
    #else:
      #  p[0] = sa.IdExp(p[1])  

def p_error(p):
  print("Erro Sintático")
  
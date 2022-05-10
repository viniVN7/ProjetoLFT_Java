import ply.yacc as yacc
from analisadorLexico import *
import SintaxeAbstrata as sa

def p_class(p):
    '''class : visibility CLASS ID LBRACE body_class RBRACE'''

#body_class 
def p_body_class(p):
  '''body_class : attribute | method
                | attribute body_class | method body_class 
  '''

#attribute -> visibility ID ID “=” exp “;” | 
             #visibility  ID ID “;” |  
             #ID ID “=” exp “;” | 
             #ID ID “;”    
def p_attribute(p):
  '''attribute : visibility ID ID ASSIGNMENT exp SEMICOLON'''
  
#method
def p_method(p):
 '''method : signature body'''

  
#signature
def p_signature(p):
  '''signature : ID ID LPAREN sigparams RPAREN
             | ID ID LPAREN RPAREN
  '''
    
#sigParams
def p_sigparams(p):
  '''sigparams : ID ID
               | ID ID COMMA sigparams
  '''

#body
def p_body(p):
  ''' body : LBRACE stms RBRACE
           | LBRACE RBRACE
  '''

def p_visibility(p):
  '''visibility : PUBLIC | PRIVATE | PROTECTED | PACKAGE'''

def p_stms(p):
  '''stms : stm | stm stms'''



def p_exp1_soma(p):
    '''exp1 : exp1 PLUS exp2
         | exp2'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = sa.SomaExp(p[1], p[3])

def p_exp2_vezes(p):
  '''exp2 : exp2 TIMES exp3
          | exp3'''
  if len(p) == 2:
    p[0] = p[1]
  else:
    p[0] = sa.MulExp(p[1] + p[3])

def p_exp4_call(p):
  '''exp4 : call
          | NUMBER
          | ID
          | TRUE
          | FALSE'''
  if isinstance(p[1], sa.Call):
        p[0] = sa.CallExp(p[1])
    elif isinstance(p[1], int):
        p[0] = sa.NumExp(p[1])
    elif (p[1] == 'true' or p[1] == 'false'):
        p[0] = sa.BooleanExp(p[1])
    else:
        p[0] = sa.IdExp(p[1])  


  
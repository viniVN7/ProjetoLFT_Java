import ply.yacc as yacc
from AnalisadorLexico import *
import SintaxeAbstrata as sa

def p_class(p):
    '''class : visibility CLASS ID LBRACE body_class RBRACE'''
    p[0] = sa.Class(p[1], p[3], p[5])
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
  '''constant : visibility STATIC FINAL type ID ASSIGNMENT exp SEMICOLON 
  | FINAL type ID ASSIGNMENT exp SEMICOLON 
  | visibility FINAL type ID ASSIGNMENT exp SEMICOLON
  | STATIC FINAL type ID ASSIGNMENT exp SEMICOLON'''
  
#method
def p_method(p):
 '''method : signature body'''

#signature
def p_signature(p):
  '''signature : visibility type ID LPAREN sigparams RPAREN
             | visibility type ID LPAREN RPAREN'''
    
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
  if (len(p) == 4):
      p[0] = sa.BodyConcrete(p[2])
  else:
      p[0] = sa.BodyConcrete(None)
    
def p_visibility(p):
  '''visibility : PUBLIC'''
  

def p_type(p):
  '''type : INT 
        | STRING
        | BOOLEAN
        | ID
        | VOID
  '''

def p_stms(p):
  '''stms : stm 
        | stm stms'''
  if(len(p) == 2):
      p[0] = sa.SingleStm(p[1])
  else:
    p[0] = sa.CompoundStm(p[1], p[2])
      
def p_stm(p):
  '''stm : stm1 
       | stm2'''

def p_stm1(p):
  '''stm1 : IF LBRACE exp RBRACE stm1 ELSE stm1 
        | IF LBRACE exp RBRACE body ELSE stm1 
        | IF LBRACE exp RBRACE stm1 ELSE body
        | IF LBRACE exp RBRACE body ELSE body
        | WHILE LBRACE exp RBRACE body 
        | WHILE LBRACE exp RBRACE stm1
        | FOR LBRACE opt_exp RBRACE body
        | FOR LBRACE opt_exp RBRACE stm1
        | RETURN exp SEMICOLON
        | exp SEMICOLON '''

# expressão opcional para o for 
def p_opt_exp(p):
  '''opt_exp : exp SEMICOLON exp SEMICOLON exp 
           | exp SEMICOLON SEMICOLON exp
           | exp SEMICOLON exp SEMICOLON 
           | exp SEMICOLON SEMICOLON 
           | SEMICOLON exp SEMICOLON exp 
           | SEMICOLON exp SEMICOLON 
           | SEMICOLON SEMICOLON exp
           | SEMICOLON SEMICOLON 
           '''
# SOBRE O FOR: CASO O PRIMEIRO COMANDO NÃO CONSTE, É NECESSÁRIO DECLARAR A VARIÁVEL ANTES 


def p_stm2(p):
  '''stm2 : IF LBRACE exp RBRACE stm 
        | IF LBRACE exp RBRACE stm1 ELSE stm2
        | IF LBRACE exp RBRACE body ELSE stm2 
        | IF LBRACE exp RBRACE body
        | WHILE LBRACE exp RBRACE stm2
        | FOR LBRACE opt_exp RBRACE stm2'''

def p_exp(p):
  '''exp : exp1 ASSIGNMENT exp
       | exp1 PLUS_ASSIGNMENT exp
       | exp1 MINUS_ASSIGNMENT exp
       | exp1 TIMES_ASSIGNMENT exp
       | exp1 DIVIDE_ASSIGNMENT exp
       | exp1 MODULE_ASSIGNMENT exp
       | exp1 AND_ASSIGNMENT exp
       | exp1 EXCLUSIVE_OR_ASSIGNMENT exp
       | exp1 INCLUSIVE_OR_ASSIGNMENT exp
       | exp1'''

def p_exp1(p):
  '''exp1 : exp1 LOGICAL_OR exp2
        | exp2'''

def p_exp2(p):
  '''exp2 : exp2 LOGICAL_AND exp3
        | exp3'''

def p_exp3(p):
  '''exp3 : exp3 INCLUSIVE_OR exp4
        | exp4'''

def p_exp4(p):
  '''exp4 : exp4 EXCLUSIVE_OR exp5
       | exp5'''

def p_exp5(p):
  '''exp5 : exp5 AND exp6 
       | exp6'''

def p_exp6(p):
  '''exp6 : exp6 EQUAL exp7 
       | exp6 DIFFERENT exp7
       | exp7'''

def p_exp7(p):
  '''exp7 : exp7 LESS_THAN exp8
        | exp7 GREATER_THAN exp8
        | exp7 LESS_OR_EQUAL exp8
        | exp7 GREATER_OR_EQUAL exp8
        | exp8'''

def p_exp8(p):
  '''exp8 : exp8 PLUS exp9
        | exp8 MINUS exp9
        | exp9'''

def p_exp9(p):
  '''exp9 : exp9 TIMES exp10 
       | exp9 DIVIDE exp10
       | exp9 MODULE exp10
       | exp10'''

def p_exp10(p):
  '''exp10 : PLUS_PLUS exp11 
         | MINUS_MINUS exp11
         | PLUS exp11
         | MINUS exp11
         | NEGATION exp11
         | BOOLEAN_NEGATION exp11
         | exp11'''

def p_exp11(p):
  '''exp11 : exp12 PLUS_PLUS 
       | exp12 MINUS_MINUS
       | exp12'''

def p_exp12(p):
  '''exp12 : call
         | NUMBER
         | ID
         | STRING 
         | LBRACE exp RBRACE'''
  
def p_call(p):
  '''call : ID LPAREN params RPAREN
        | ID LPAREN RPAREN'''

def p_params(p):
  '''params : exp COMMA params
            | exp '''

def p_error(p):
  print("Erro Sintático")
  
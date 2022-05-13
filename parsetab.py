
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AND_ASSIGNMENT ASSIGNMENT BOOLEAN BOOLEAN_NEGATION BREAK CLASS COMMA DIFFERENT DIVIDE DIVIDE_ASSIGNMENT ELSE EQUAL EXCLUSIVE_OR EXCLUSIVE_OR_ASSIGNMENT FALSE FOR GREATER_OR_EQUAL GREATER_THAN ID IF IMPORT INCLUSIVE_OR INCLUSIVE_OR_ASSIGNMENT INSTANCEOF INT LBRACE LESS_OR_EQUAL LESS_THAN LOGICAL_AND LOGICAL_OR LPAREN MINUS MINUS_ASSIGNMENT MINUS_MINUS MODULE MODULE_ASSIGNMENT NEGATION NEW NULL NUMBER PACKAGE PLUS PLUS_ASSIGNMENT PLUS_PLUS PUBLIC RBRACE RETURN RPAREN SEMICOLON STATIC STRING THIS TIMES TIMES_ASSIGNMENT TRUE VOID WHILEclass : visibility CLASS ID LBRACE body_class RBRACEbody_class : attribute \n              | method\n              | attribute body_class \n              | method body_class \n  attribute : visibility type ID ASSIGNMENT exp SEMICOLON \n            | visibility type ID SEMICOLON \n            | type ID ASSIGNMENT exp SEMICOLON \n            | type ID SEMICOLON\n  type : INT \n        | ID \n        | STRING\n  method : signature bodysignature : ID ID LPAREN sigparams RPAREN\n             | ID ID LPAREN RPARENsigparams : ID ID \n             | ID ID COMMA sigparams\n   body : LBRACE stms RBRACE\n           | LBRACE RBRACE\n  visibility : PUBLICstms : stm \n        | stm stmsstm : IDexp : call : ID LPAREN params RPAREN\n        | ID LPAREN RPARENparams : exp COMMA params\n            | exp '
    
_lr_action_items = {'PUBLIC':([0,6,10,11,23,28,30,34,39,44,45,],[3,3,3,3,-13,-9,-19,-7,-18,-8,-6,]),'$end':([1,19,],[0,-1,]),'CLASS':([2,3,],[4,-20,]),'INT':([3,6,7,10,11,23,28,30,34,39,44,45,],[-20,14,14,14,14,-13,-9,-19,-7,-18,-8,-6,]),'ID':([3,4,6,7,8,10,11,12,14,15,16,17,23,24,26,28,30,31,32,34,35,39,44,45,46,],[-20,5,8,17,18,8,8,22,-10,-12,25,-11,-13,32,35,-9,-19,32,-23,-7,42,-18,-8,-6,35,]),'STRING':([3,6,7,10,11,23,28,30,34,39,44,45,],[-20,15,15,15,15,-13,-9,-19,-7,-18,-8,-6,]),'LBRACE':([5,13,37,43,],[6,24,-15,-14,]),'RBRACE':([9,10,11,20,21,23,24,28,29,30,31,32,34,39,40,44,45,],[19,-2,-3,-4,-5,-13,30,-9,39,-19,-21,-23,-7,-18,-22,-8,-6,]),'LPAREN':([18,],[26,]),'ASSIGNMENT':([22,25,],[27,33,]),'SEMICOLON':([22,25,27,33,38,41,],[28,34,-24,-24,44,45,]),'RPAREN':([26,36,42,47,],[37,43,-16,-17,]),'COMMA':([42,],[46,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'class':([0,],[1,]),'visibility':([0,6,10,11,],[2,7,7,7,]),'body_class':([6,10,11,],[9,20,21,]),'attribute':([6,10,11,],[10,10,10,]),'method':([6,10,11,],[11,11,11,]),'type':([6,7,10,11,],[12,16,12,12,]),'signature':([6,10,11,],[13,13,13,]),'body':([13,],[23,]),'stms':([24,31,],[29,40,]),'stm':([24,31,],[31,31,]),'sigparams':([26,46,],[36,47,]),'exp':([27,33,],[38,41,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> class","S'",1,None,None,None),
  ('class -> visibility CLASS ID LBRACE body_class RBRACE','class',6,'p_class','analisadorSintatico.py',6),
  ('body_class -> attribute','body_class',1,'p_body_class','analisadorSintatico.py',10),
  ('body_class -> method','body_class',1,'p_body_class','analisadorSintatico.py',11),
  ('body_class -> attribute body_class','body_class',2,'p_body_class','analisadorSintatico.py',12),
  ('body_class -> method body_class','body_class',2,'p_body_class','analisadorSintatico.py',13),
  ('attribute -> visibility type ID ASSIGNMENT exp SEMICOLON','attribute',6,'p_attribute','analisadorSintatico.py',18),
  ('attribute -> visibility type ID SEMICOLON','attribute',4,'p_attribute','analisadorSintatico.py',19),
  ('attribute -> type ID ASSIGNMENT exp SEMICOLON','attribute',5,'p_attribute','analisadorSintatico.py',20),
  ('attribute -> type ID SEMICOLON','attribute',3,'p_attribute','analisadorSintatico.py',21),
  ('type -> INT','type',1,'p_type','analisadorSintatico.py',24),
  ('type -> ID','type',1,'p_type','analisadorSintatico.py',25),
  ('type -> STRING','type',1,'p_type','analisadorSintatico.py',26),
  ('method -> signature body','method',2,'p_method','analisadorSintatico.py',30),
  ('signature -> ID ID LPAREN sigparams RPAREN','signature',5,'p_signature','analisadorSintatico.py',34),
  ('signature -> ID ID LPAREN RPAREN','signature',4,'p_signature','analisadorSintatico.py',35),
  ('sigparams -> ID ID','sigparams',2,'p_sigparams','analisadorSintatico.py',39),
  ('sigparams -> ID ID COMMA sigparams','sigparams',4,'p_sigparams','analisadorSintatico.py',40),
  ('body -> LBRACE stms RBRACE','body',3,'p_body','analisadorSintatico.py',45),
  ('body -> LBRACE RBRACE','body',2,'p_body','analisadorSintatico.py',46),
  ('visibility -> PUBLIC','visibility',1,'p_visibility','analisadorSintatico.py',50),
  ('stms -> stm','stms',1,'p_stms','analisadorSintatico.py',53),
  ('stms -> stm stms','stms',2,'p_stms','analisadorSintatico.py',54),
  ('stm -> ID','stm',1,'p_stm','analisadorSintatico.py',57),
  ('exp -> <empty>','exp',0,'p_exp','analisadorSintatico.py',60),
  ('call -> ID LPAREN params RPAREN','call',4,'p_call','analisadorSintatico.py',69),
  ('call -> ID LPAREN RPAREN','call',3,'p_call','analisadorSintatico.py',70),
  ('params -> exp COMMA params','params',3,'p_params','analisadorSintatico.py',73),
  ('params -> exp','params',1,'p_params','analisadorSintatico.py',74),
]

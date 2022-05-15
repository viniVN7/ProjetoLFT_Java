import ply.lex as lex # importando a biblioteca ply para o léxico

#Definindo palavras reservadas
reserved = {
  'if' : 'IF',
  'else' : 'ELSE',
  'while' : 'WHILE',
  'for' : 'FOR',
  'break' : 'BREAK',
  'class' : 'CLASS',
  'return' : 'RETURN',
  'int' : 'INT',
  'boolean' : 'BOOLEAN',
  'String' : 'STRING',
  'new' : 'NEW',
  'this' : 'THIS',
  'void' : 'VOID',
  'import' : 'IMPORT',
  'instanceof' : 'INSTANCEOF',
  'package' : 'PACKAGE',
  'public' : 'PUBLIC',
  'static' : 'STATIC',
  'final' : 'FINAL',
  'null' : 'NULL',
  'false' : 'FALSE',
  'true' : 'TRUE',
}

#Definindo Tokens e seus padroes
tokens = ["PLUS_PLUS","MINUS_MINUS", "PLUS_ASSIGNMENT", "MINUS_ASSIGNMENT", "TIMES_ASSIGNMENT", "DIVIDE_ASSIGNMENT", "MODULE_ASSIGNMENT", "AND_ASSIGNMENT", "EXCLUSIVE_OR_ASSIGNMENT", "INCLUSIVE_OR_ASSIGNMENT", "PLUS","MINUS","TIMES","DIVIDE", "MODULE", "LPAREN", "RPAREN", "ID", "NUMBER", "EQUAL", "ASSIGNMENT", "EXCLUSIVE_OR", "INCLUSIVE_OR", "LOGICAL_AND", "LOGICAL_OR", "AND", "NEGATION", "BOOLEAN_NEGATION", "LESS_OR_EQUAL", "DIFFERENT","GREATER_OR_EQUAL", "LESS_THAN", "GREATER_THAN", "LBRACE", "RBRACE", "COMMA", "SEMICOLON"]  + list(reserved.values()) 

#adicionar operadores e (palavras reservadas _já_ok)
t_PLUS_PLUS = r'\++' 
t_MINUS_MINUS = r'--' 
t_PLUS_ASSIGNMENT = r'\+=' 
t_MINUS_ASSIGNMENT = r'-=' 
t_TIMES_ASSIGNMENT = r'\*='
t_DIVIDE_ASSIGNMENT = r'/='
t_MODULE_ASSIGNMENT = r'%='
t_AND_ASSIGNMENT = r'&='
t_EXCLUSIVE_OR_ASSIGNMENT = r'\^='
t_INCLUSIVE_OR_ASSIGNMENT = r'\|='

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*' 
t_DIVIDE = r'/'
t_MODULE = r'%'

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_EQUAL = r'=='
t_ASSIGNMENT = r'='

t_LOGICAL_AND = r'&&'
t_LOGICAL_OR = r'\|\|'
t_AND = r'&'
t_EXCLUSIVE_OR = r'\^' 
t_INCLUSIVE_OR = r'\|'

t_NEGATION = r'~'
t_BOOLEAN_NEGATION = r'!'

t_LESS_OR_EQUAL = r'<='
t_GREATER_OR_EQUAL = r'>='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_DIFFERENT = r'!='

t_LBRACE = r'\{'
t_RBRACE = r'\}'

t_COMMA = r','
t_SEMICOLON = r';'
#t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'

#Definindo funções
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,"ID")
    return t


def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t


def t_newline(t): # reconhece quebra de linha, tabulação e espaçõ em branco 
  r'\n+'
  t.lexer.lineno += len(t.value)
t_ignore = t_ignore = ' \t'  

def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)

#lexer = lex.lex()

def t_STRING(t):
   r'\"([^\\\n]|(\\.))*?\"'
   return t

def t_ccode_comment(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass
  
#Criando analisador Lexico e realizando analise lexica
#lexer = lex.lex()
#lexer.input("\"\\n\"") #new
#lexer.input("&& || > <  >= <= != == = % , ; ^ | ++")
#lexer.input("& && &= -- += -= %= /= *= ^= |= | || ~ !")
#lexer.input("+-*-/ 5 } {=^++\t+\n+() num4 \"teste \\n teste\"  ") 
#for tok in lexer:
 # print(tok.type, tok.value, tok.lineno, tok.lexpos) 

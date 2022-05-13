from analisadorLexico import *
from analisadorSintatico import *

lexer = lex.lex();

cl = '''public class Java {
        
        int a = 3;
        }
     '''

lexer.input(cl)
parser = yacc.yacc()
result = parser.parse(debug=True)
#Visitor = vis.Visitor()
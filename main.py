from analisadorLexico import *
from analisadorSintatico import *

lexer = lex.lex();

teste = '''public class Java {
            int a = 3;
            public int b;
        }
        '''

lexer.input(teste)
parser = yacc.yacc()
result = parser.parse(debug=True)
#Visitor = vis.Visitor()
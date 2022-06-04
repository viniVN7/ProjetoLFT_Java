from AnalisadorLexico import *
from AnalisadorSintatico import *


lexer = lex.lex();

teste = '''
public class Java {
  int a = 3;
  public int b;
  public int metodo(int a) {
    return a*2;
  }
  public void metodo2(){
      if(a=3)
      b=1;
  }
            
        }
        '''

lexer.input(teste)
parser = yacc.yacc()
result = parser.parse(debug=True)
#Visitor = vis.Visitor()
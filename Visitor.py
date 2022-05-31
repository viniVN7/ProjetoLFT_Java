from AbstractVisitor import AbstractVisitor

tab = 0

def blank():
  p = ''
  for x in range(tab):
    p = p + ' '
  return p

class Visitor(AbstractVisitor):

  def visitClassConcrete(self, classConcrete):
    #classConcrete.visibility.accept(self)
    classConcrete.visibility.accept(self)
    print(blank(), 'class ', end = '', sep = '')
    print(classConcrete.id, ' ', end = '', sep = '')
    print('{ ', end = '', sep = '')
    classConcrete.body_class.accept(self)
    print(' }')
   
  #visibility CLASS ID LBRACE body_class RBRACE
  def visitBodyClassAttrRec(self, bodyClassAttrRec):
    bodyClassAttrRec.attribute.accpet(self)
    if(bodyClassAttrRec.bodyClass != None):
      bodyClassAttrRec.bodyClass.accept(self)

  def visitBodyClassMethRec(self,bodyClassMethRec):
    bodyClassMethRec.method.accept(self)
    if(bodyClassMethRec.bodyClass != None):
      bodyClassMethRec.bodyClass.accept(self)
  
  def visitMethodConcrete(self, methodConcrete):
    methodConcrete.signature.accept(self)
    methodConcrete.body.accept(self)

  def visitSignatureConcrete(self, signatureConcrete):
    signatureConcrete.visibility.accept(self)
    print(blank(), signatureConcrete.type, ' ', end = '', sep = '')
    print(signatureConcrete.id, '(', end = '', sep = '')
    if(signatureConcrete.sigparams != None):
      signatureConcrete.sigparams.accept(self)
    print(')', end = '')

  def visitSingleParam(self, singleParam):
    singleParam.exp.accept(self)

  def visitCompoundParams(self, compoundParams):
    compoundParams.exp.accept(self)
    print(',', end='')
    compoundParams.accept(self)

  def visitVisibility(self, visibilityConcrete):
    print('public ', end='')

  def visitBodyConcrete(self, bodyConcrete):
    global tab
    print('{ ')
    tab = tab + 3
    if(bodyConcrete.stms != None):
      bodyConcrete.stms.accept(self)
    tab = tab - 3
    print(blank(), '} ', sep = '')
  
  def visitSingleStm(self, singleStm):
    singleStm.stm.accept(self)

  def visitCompoundStm(self, compoundStm):
    compoundStm.stm.accept(self)
    compoundStm.stms.accept(self)

  def visitStmExp(self, stmExp):
    print(blank(),sep='',end='')
    stmExp.exp.accept(self)
    print('')

  def visitStmWhile(self, stmWhile):
    print (blank(), 'while (', end='', sep='')
    stmWhile.exp.accept(self)
    print (')', end='', sep='')
    stmWhile.block.accept(self)

  def visitStmReturn(self, stmReturn):
    print (blank(), 'return ', end='', sep='')
    stmReturn.exp.accept(self)
    print (';')
    
  def visitAssignExp(self, assignExp):
    assignExp.exp1.accept(self)
    print(' = ', end='')
    assignExp.exp2.accept(self)

  def visitSomaExp(self, somaExp):
    somaExp.exp1.accept(self)
    print(' + ', end='')
    somaExp.exp2.accept(self)

  def visitMulExp(self, mulExp):
    mulExp.exp1.accept(self)
    print(' * ', end='')
    mulExp.exp2.accept(self)

  #def visitDivExp(self, divExp):
    #divExp.

  def visitCallExp(self, callExp):
    callExp.call.accept(self)

  def visitNumExp(self, numExp):
    print(numExp.num, end='')

  def visitIdExp(self, idExp):
    print(idExp.id, end='')

  def visitBooleanExp(self, booleanExp):
    print(booleanExp.boolValue, end='')

  def visitModuleExp(self, moduleExp):
    moduleExp.exp1.accept(self)
    print(' % ', end='')
    moduleExp.exp2.accept(self)

  def visitParamsCall(self, paramsCall):
    print(paramsCall.id, '(', end='', sep='')
    paramsCall.paramscall.params.accept(self)
    print(')', end='')

  def visitNoParamsCall(self, simpleCall):
    print(blank(), simpleCall.id, '()', end='', sep='')




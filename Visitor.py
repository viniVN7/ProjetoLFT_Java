from AbstractVisitor import AbstractVisitor
import SintaxeAbstrata as sa

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
    compoundParams.params.accept(self)

  def visitVisibilityConcrete(self, visibilityConcrete):
    print('public ', end='')

  def visitAttributeWhitVisibility(self, attributeWhitVisibility):
    attributeWhitVisibility.visibility.accept(self)
    attributeWhitVisibility.type.accept(self)
    attributeWhitVisibility.id.accept(self)
    if (attributeWhitVisibility.exp != None):
      print(' = ')
      attributeWhitVisibility.exp.accept(self)
    print(";")

  def visitAttributeWithoutVisibility(self, attributeWithoutVisibility):
    attributeWithoutVisibility.type.accept(self)
    attributeWithoutVisibility.id.accept(self)
    if (attributeWithoutVisibility.exp != None):
      print(' = ')
      attributeWithoutVisibility.exp.accept(self)
    print(";")

  def visitTypeInt(self, typeInt):
    print('int ', end = '')
  
  def visitTypeString(self, typeString):
    print('String ', end = '')

  def visitTypeBoolean(self, typeBoolean):
    print('boolean ', end = '')

  def visitTypeVoid(self, typeVoid):
    print('void ', end = '')

  def visitTypeID(self, typeID):
    typeID.id.accept(self)
  
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
    assignExp.exp.accept(self)
  
  def visitPlusAssignExp(self, plusAssignExp):
    plusAssignExp.exp1.accept(self)
    print(' += ', end='')
    plusAssignExp.exp.accept(self)

  def visitMinusAssignExp(self, minusAssignExp):
    minusAssignExp.exp1.accept(self)
    print(' -= ', end='')
    minusAssignExp.exp.accept(self)

  def visitTimesAssignExp(self, timesAssignExp):
    timesAssignExp.exp1.accept(self)
    print(' *= ', end='')
    timesAssignExp.exp.accept(self)

  def visitDivideAssignExp(self, divideAssignExp):
    divideAssignExp.exp1.accept(self)
    print(' /= ', end='')
    divideAssignExp.exp.accept(self)

  def visitModuleAssignExp(self, moduleAssignExp):
    moduleAssignExp.exp1.accept(self)
    print(' %= ', end='')
    moduleAssignExp.exp.accept(self)

  def visitAndAssignExp(self, andAssignExp):
    andAssignExp.exp1.accept(self)
    print(' &= ', end='')
    andAssignExp.exp.accept(self)

  def visitExclusiveOrAssignExp(self, exclusiveOrAssign):
    exclusiveOrAssign.exp1.accept(self)
    print(' ^= ', end='')
    exclusiveOrAssign.exp.accept(self)

  def visitInclusiveOrAssignExp(self, inclusiveOrAssign):
    inclusiveOrAssign.exp1.accept(self)
    print(' |= ', end='')
    inclusiveOrAssign.exp.accept(self)

  def visitLogicalOrExp(self, logicalOrExp):
    logicalOrExp.exp1.accept(self)
    print(' || ', end='')
    logicalOrExp.exp2.accept(self)

  def visitLogicalAndExp(self, logicalAndExp):
    logicalAndExp.exp2.accept(self)
    print(' && ', end='')
    logicalAndExp.exp3.accept(self)
  
  def visitInclusiveOrExp(self, inclusiveOrExp):
    inclusiveOrExp.exp3.accept(self)
    print(' | ', end='')
    inclusiveOrExp.exp4.accept(self)

  def visitExclusiveOrExp(self, exclusiveOrExp):
    exclusiveOrExp.exp4.accept(self)
    print(' ^ ', end='')
    exclusiveOrExp.exp5.accept(self)

  def visitAndExp(self, andExp):
    andExp.exp5.accept(self)
    print(' ^ ', end='')
    andExp.exp6.accept(self)

  def visitEqualExp(self, equalExp):
      equalExp.exp6.accept(self)
      print(' == ', end='')
      equalExp.exp7.accept(self) 
 
  def visitDifferentExp(self, differentExp):
      differentExp.exp6.accept(self)
      print(' != ', end='')
      differentExp.exp7.accept(self)  

  def visitLessOrEqualExp(self, lessOrEqualExp):
      lessOrEqualExp.exp7.accept(self)
      print(' <= ', end='')
      lessOrEqualExp.exp8.accept(self)  
  
  def visitGreaterOrEqualExp(self, greaterOrEqualExp):
      greaterOrEqualExp.exp7.accept(self)
      print(' >= ', end='')
      greaterOrEqualExp.exp8.accept(self)  
  
  def visitLessThanExp(self, lessThanExp):
      lessThanExp.exp7.accept(self)
      print(' < ', end='')
      lessThanExp.exp8.accept(self)  
  
  def visitGreaterThanExp(self, greaterThanExp):
      greaterThanExp.exp7.accept(self)
      print(' > ', end='')
      greaterThanExp.exp8.accept(self) 

  def visitSomaExp(self, somaExp):
    somaExp.exp8.accept(self)
    print(' + ', end='')
    somaExp.exp9.accept(self)

  def visitMulExp(self, mulExp):
    mulExp.exp9.accept(self)
    print(' * ', end='')
    mulExp.exp10.accept(self)

  def visitDivExp(self, divExp):
    divExp.exp9.accept(self)
    print(' / ', end='')
    divExp.exp10.accept(self)

  def visitModuleExp(self, moduleExp):
    moduleExp.exp9.accept(self)
    print(' % ', end='')
    moduleExp.exp10.accept(self)

  def visitPlusPlusPrefixExp(self, plusPlusPrefixPostExp):
      plusPlusPrefixPostExp.exp11.accept(self)
      print(' ++')

  def visitMinusMinusPrefixExp(self, minusMinusPrefixPostExp):
    minusMinusPrefixPostExp.exp11.accept(self)
    print(' --')

  def visitPlusPrefixExp(self, PlusPrefixExp):
    PlusPrefixExp.exp11.accept(self)
    print(' +')

  def visitMinusPrefixExp(self, minusPrefixPostExp):
    minusPrefixPostExp.exp11.accept(self)
    print(' -')

  def visitNegationExp(self, negationExp):
    negationExp.exp11.accept(self)
    print(' !')

  def visitNegationBoolExp(self, negationBoolExp):
    negationBoolExp.exp11.accept(self)
    print(' ~')
  
  def visitMinusMinusSuffixExp(self, minusMinusSuffix):
      minusMinusSuffix.exp12.accept(self)
      print('--')  

  def visitPlusPlusSuffixExp(self, plusPlusSuffixExp):
      plusPlusSuffixExp.exp12.accept(self)
      print('++')
    
  def visitCallExp(self, callExp):
    callExp.call.accept(self)

  def visitNumExp(self, numExp):
    print(numExp.num, end='')

  def visitIdExp(self, idExp):
    print(idExp.id, end='')

  def visitBooleanExp(self, booleanExp):
    print(booleanExp.boolValue, end='')

  def visitParamsCall(self, paramsCall):
    print(paramsCall.id, '(', end='', sep='')
    paramsCall.paramscall.params.accept(self)
    print(')', end='')

  def visitNoParamsCall(self, simpleCall):
    print(blank(), simpleCall.id, '()', end='', sep='')




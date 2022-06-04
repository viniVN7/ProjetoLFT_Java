from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor


class Class (metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class ClassConrete(metaclass = ABCMeta):
  def __init__ (self, visibility, Class, id, body_class):
    self.visibility = visibility
    self.Class = Class
    self.id = id 
    self.body_class = body_class
  def accept(self, Visitor):
    return Visitor.visitClassConrete
  
'''Method'''     
class Method (metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
      pass

class MethodConcrete(Method):
  def __init__ (self, signature, body):
    self.signature = signature
    self.body = body 
  def accept(self, Visitor):
    return Visitor.visitMethodConcrete(self)

'''Signature'''
class Signature (metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class SignatureConcrete(Signature):
  def __init__(self, visibility, type, id, sigparams):
      self.visibility = visibility
      self.type = type 
      self.id = id 
      self.sigparams = sigparams
  def accept(self, Visitor):
    return Visitor.visitSignatureConcrete(self)

'''BodyClass'''
class BodyClass (metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
      pass

class BodyClassAttrRec(BodyClass):
  def __init__(self, attribute, body_class):
    self.attribute = attribute
    self.body_class = body_class
  def accept(self, Visitor):
    return Visitor.visitBodyClassAttrRec(self)

class BodyClassMethRec(BodyClass):
  def __init__(self, method, body_class):
    self.method = method
    self.body_class = body_class
  def accept(self, visitor):
    return Visitor.visitBodyClassMethRec(self)

'''Attribute'''
class Attribute (metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
      pass

class AttributehitVisibilityConcrete(Attribute):
  def __init__(self, visibility, type, id, exp):
    self.visibility = visibility
    self.type = type
    self.id = id 
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitAttributehitVisibilityConcrete(self)

class AttributeWithoutVisibilityConcrete(Attribute):
  def __init__(self, type, id, exp):
    self.type = type
    self.id = id 
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitAttributeWithoutVisibility(self)
    

class Constant (metaclass = ABCMeta):
  @abstractmethod
  def accept():
      pass

class ConstantConcrete (Constant):
  def __init__(self, visibility, static, final, type, id, exp):
    Constant.visibility =  visibility
    Constant.static = static
    Constant.final = final
    Constant.type = type
    Constant.id = id
    Constant.exp = exp
  def accept(self, visitor):
    return visitor.visitConstConcrete(self)
    
  '''SigParams'''
class SigParams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleSigParam(SigParams):
    def __init__(self, ID):
        self.nameParameter = ID
    def accept(self, visitor):
        return visitor.visitSingleParam(self)

class CompoundSigParam(SigParams):
    def __init__(self, ID, SigParameters):
        self.nameParameter = ID
        self.parameters = SigParameters
    def accept(self, visitor):
        return visitor.visitCompoundParams(self)

'''stms'''
class Stms(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleStm(Stms):
    def __init__(self, stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitSingleStm(self)

class CompoundStm(Stms):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitCompoundStm(self)


'''stm'''
class Stm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class StmExp(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmExp(self)

class StmWhile(Stm):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block
    def accept(self, visitor):
        return visitor.visitStmWhile(self)

class StmReturn(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmReturn(self)

'''Exp'''

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class AssignExp(Exp):
    def __init__(self, exp1, exp):
        self.exp1 = exp1
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitAssignExp(self)

class PlusAssignExp(Exp):
    def __init__(self, exp1, exp):
        self.exp1 = exp1
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitPlusAssignExp(self)

class MinusAssignExp(Exp):
    def __init__(self, exp1, exp):
        self.exp1 = exp1
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitMinusAssignExp(self)

class TimesAssignExp(Exp):
    def __init__(self, exp1, exp):
        self.exp1 = exp1
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitTimesAssignExp(self)

class DivideAssignExp(Exp):
    def __init__(self, exp1, exp):
        self.exp1 = exp1
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitDivideAssignExp(self)

class ModuleAssignExp(Exp):
    def __init__(self, exp1, exp):
        self.exp1 = exp1
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitModuleAssignExp(self)

class AndAssignExp(Exp):
    def __init__(self, exp1, exp):
        self.exp1 = exp1
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitAndAssignExp(self)

class ExclusiveOrAssignExp(Exp):
    def __init__(self, exp1, exp):
        self.exp1 = exp1
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitExclusiveOrAssignExp(self)

class InclusiveOrAssignExp(Exp):
    def __init__(self, exp1, exp):
        self.exp1 = exp1
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitInclusiveOrAssignExp(self)

class LogicalOrExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitLogicalOrExp(self)

class LogicalAndExp(Exp):
    def __init__(self, exp2, exp3):
        self.exp2 = exp2
        self.exp3 = exp3
    def accept(self, visitor):
        return visitor.visitLogicalAndExp(self)

class InclusiveOrExp(Exp):
    def __init__(self, exp3, exp4):
        self.exp3 = exp3
        self.exp4 = exp4
    def accept(self, visitor):
        return visitor.visitInclusiveOrExp(self)

class ExclusiveOrExp(Exp):
    def __init__(self, exp4, exp5):
        self.exp4 = exp4
        self.exp5 = exp5
    def accept(self, visitor):
        return visitor.visitExclusiveOrExp(self)

class AndExp(Exp):
    def __init__(self, exp5, exp6):
        self.exp5 = exp5
        self.exp6 = exp6
    def accept(self, visitor):
        return visitor.visitAndExp(self)

class EqualExp(Exp):
    def __init__(self, exp6, exp7):
        self.exp6 = exp6
        self.exp7 = exp7
    def accept(self, visitor):
        return visitor.visitEqualExp(self)

class DifferentExp(Exp):
    def __init__(self, exp6, exp7):
        self.exp6 = exp6
        self.exp7 = exp7
    def accept(self, visitor):
        return visitor.visitDifferentExp(self)

class LessOrEqualExp(Exp):
    def __init__(self, exp7, exp8):
        self.exp7 = exp7
        self.exp8 = exp8
    def accept(self, visitor):
        return visitor.visitLessOrEqualExp(self)

class GreaterOrEqualExp(Exp):
    def __init__(self, exp7, exp8):
        self.exp7 = exp7
        self.exp8 = exp8
    def accept(self, visitor):
        return visitor.visitGreaterOrEqualExp(self)

class LessThanExp(Exp):
    def __init__(self, exp7, exp8):
        self.exp7 = exp7
        self.exp8 = exp8
    def accept(self, visitor):
        return visitor.visitLessThanExp(self)

class GreaterThanExp(Exp):
    def __init__(self, exp7, exp8):
        self.exp7 = exp7
        self.exp8 = exp8
    def accept(self, visitor):
        return visitor.visitGreaterThanExp(self)

class SomaExp(Exp):
    def __init__(self, exp8, exp9):
        self.exp8 = exp8
        self.exp9 = exp9
    def accept(self, visitor):
        return visitor.visitSomaExp(self)

class SubExp(Exp):
    def __init__(self, exp8, exp9):
        self.exp8 = exp8
        self.exp9 = exp9
    def accept(self, visitor):
        return visitor.visitSubExp(self)

class MulExp(Exp):
    def __init__(self, exp9, exp10):
        self.exp9 = exp9
        self.exp10 = exp10
    def accept(self, visitor):
        return visitor.visitMulExp(self)

class DivExp(Exp):
    def __init__(self, exp9, exp10):
        self.exp9 = exp9
        self.exp10 = exp10
    def accept(self, visitor):
        return visitor.visitDivExp(self)

class ModuleExp(Exp):
    def __init__(self, exp9, exp10):
        self.exp9 = exp9
        self.exp10 = exp10
    def accept(self, visitor):
        return visitor.visitModuleExp(self)

class PlusPlusPrefixExp(Exp):
    def __init__(self, exp11):
        self.exp11 = exp11
    def accept(self, visitor):
        return visitor.visitPlusPlusPrefixExp(self)

class MinusMinusPrefixExp(Exp):
    def __init__(self, exp11):
        self.exp11 = exp11
    def accept(self, visitor):
        return visitor.visitMinusMinusPrefixExp(self)

class PlusPrefixExp(Exp):
    def __init__(self, exp11):
        self.exp11 = exp11
    def accept(self, visitor):
        return visitor.visitPlusPrefixExp(self)

class MinusPrefixExp(Exp):
    def __init__(self, exp11):
        self.exp11 = exp11
    def accept(self, visitor):
        return visitor.visitMinusPrefixExp(self)

class NegationExp(Exp):
    def __init__(self, exp11):
        self.exp11 = exp11
    def accept(self, visitor):
        return visitor.visitNegationExp(self)

class NegationBoolExp(Exp):
    def __init__(self, exp11):
        self.exp11 = exp11
    def accept(self, visitor):
        return visitor.visitNegationBollExp(self)

class MinusMinusSuffixExp(Exp):
  def __init__(self, exp12):
    self.exp12 = exp12
  def accept(self, visitor):
    return visitor.visitMinusMinusSuffixExp(self)

class PlusPlusSuffixExp(Exp):
  def __init__(self, exp12):
    self.exp12 = exp12
  def accept(self, visitor):
    return visitor.visitPlusPlusSuffixExp(self)
    
class CallExp(Exp, Stm):
    def __init__(self, call):
        self.call = call
    def accept(self, visitor):
        return visitor.visitCallExp(self)

class NumExp(Exp):
    def __init__(self, num):
        self.num = num
    def accept(self, visitor):
        return visitor.visitNumExp(self)


class IdExp(Exp):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitIdExp(self)

class BooleanExp(Exp):
    def __init__(self, boolValue):
        self.boolValue = boolValue
    def accept(self, visitor):
        return visitor.visitBooleanExp(self)   
      
'''call'''

class Call(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ParamsCall(Call):
  def __init__ (self, id, params):
    self.id = id
    self.params = params
  def accept(self, visitor):
    return visitor.visitParamsCall(self)

class NoParamsCall(Call):
    def __init__(self, id):
      self.id = id
    def accept(self, visitor):
      return visitor.visitNoParamsCall(self)
      
'''chamada'''
class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CompoundParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params
    def accept(self, visitor):
        return visitor.visitCompoundParams(self)

class SingleParam(Params):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitSingleParam(self)      

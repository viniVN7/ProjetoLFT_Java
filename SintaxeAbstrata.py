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
  def accept(self, Visitor):
    return Visitor.visitBodyClassMethRec(self)

'''Attribute'''
class Attribute (metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
      pass

class attributeConcrete(Attribute):
  

class Constant (metaclass = ABCMeta):
  @abstractmethod
  def accept():
      pass
    
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
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitAssignExp(self)

class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitSomaExp(self)


class MulExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitMulExp(self)


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

class ModuleExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitModuleExp(self)
'''AND, OR, ++ '''

class AndExp(Exp): #DEFINIR NO VISITOR s  
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitAndExp(self)
      
class IqualExp(Exp): #DEFINIR NO VISITOR S
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitIqualExp(self)

class LESS_OR_EQUALExp(Exp): #DEFINIR NO VISITORs
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitLESS_OR_EQUALExp(self)

class GREATER_OR_EQUALExp(Exp): #DEFINIR NO VISITOR s
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitGREATER_OR_EQUALExp(self)

class LESS_THANExp(Exp): #DEFINIR NO VISITOR s
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitLESS_THANExp(self)
      
class GREATER_THANExp(Exp): #DEFINIR NO VISITOR s
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitGREATER_THANExp(self)      
      

class DIFFERENTExp(Exp): #DEFINIR NO VISITOR s
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitDIFFERENTExp(self) 
      
'''parte de operadores

'''      
class plus_plusExp(Exp): #s -----
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitplus_plusExp(self)

class minus_minusExp(Exp): #
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitminus_minusExp(self)
      
class plus_assigmetExp(Exp):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitplus_assigmetExp(self) 
      
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

# Generated from logic_grammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,23,8,0,1,1,1,1,1,1,1,1,1,2,
        1,2,5,2,31,8,2,10,2,12,2,34,9,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,5,5,47,8,5,10,5,12,5,50,9,5,1,5,1,5,3,5,54,8,5,1,6,1,
        6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,8,9,57,0,22,1,0,0,0,2,24,1,0,
        0,0,4,28,1,0,0,0,6,35,1,0,0,0,8,38,1,0,0,0,10,41,1,0,0,0,12,55,1,
        0,0,0,14,23,3,2,1,0,15,23,3,4,2,0,16,23,3,8,4,0,17,23,3,10,5,0,18,
        19,5,1,0,0,19,20,3,0,0,0,20,21,5,2,0,0,21,23,1,0,0,0,22,14,1,0,0,
        0,22,15,1,0,0,0,22,16,1,0,0,0,22,17,1,0,0,0,22,18,1,0,0,0,23,1,1,
        0,0,0,24,25,5,4,0,0,25,26,5,8,0,0,26,27,3,0,0,0,27,3,1,0,0,0,28,
        32,3,10,5,0,29,31,3,6,3,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,
        0,0,32,33,1,0,0,0,33,5,1,0,0,0,34,32,1,0,0,0,35,36,5,5,0,0,36,37,
        3,0,0,0,37,7,1,0,0,0,38,39,5,6,0,0,39,40,3,0,0,0,40,9,1,0,0,0,41,
        53,5,7,0,0,42,43,5,1,0,0,43,48,3,12,6,0,44,45,5,3,0,0,45,47,3,12,
        6,0,46,44,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,
        1,0,0,0,50,48,1,0,0,0,51,52,5,2,0,0,52,54,1,0,0,0,53,42,1,0,0,0,
        53,54,1,0,0,0,54,11,1,0,0,0,55,56,7,0,0,0,56,13,1,0,0,0,4,22,32,
        48,53
    ]

class logic_grammarParser ( Parser ):

    grammarFileName = "logic_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "<INVALID>", "<INVALID>", 
                     "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "QUANTIFIER", "BINARY_OP", "NOT", "PREDICATE", "VARIABLE", 
                      "CONSTANT", "WS" ]

    RULE_formula = 0
    RULE_quantifiedFormula = 1
    RULE_binaryFormula = 2
    RULE_binaryOpRest = 3
    RULE_unaryFormula = 4
    RULE_atom = 5
    RULE_term = 6

    ruleNames =  [ "formula", "quantifiedFormula", "binaryFormula", "binaryOpRest", 
                   "unaryFormula", "atom", "term" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    QUANTIFIER=4
    BINARY_OP=5
    NOT=6
    PREDICATE=7
    VARIABLE=8
    CONSTANT=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quantifiedFormula(self):
            return self.getTypedRuleContext(logic_grammarParser.QuantifiedFormulaContext,0)


        def binaryFormula(self):
            return self.getTypedRuleContext(logic_grammarParser.BinaryFormulaContext,0)


        def unaryFormula(self):
            return self.getTypedRuleContext(logic_grammarParser.UnaryFormulaContext,0)


        def atom(self):
            return self.getTypedRuleContext(logic_grammarParser.AtomContext,0)


        def formula(self):
            return self.getTypedRuleContext(logic_grammarParser.FormulaContext,0)


        def getRuleIndex(self):
            return logic_grammarParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)




    def formula(self):

        localctx = logic_grammarParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formula)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.quantifiedFormula()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.binaryFormula()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.unaryFormula()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 17
                self.atom()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 18
                self.match(logic_grammarParser.T__0)
                self.state = 19
                self.formula()
                self.state = 20
                self.match(logic_grammarParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantifiedFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUANTIFIER(self):
            return self.getToken(logic_grammarParser.QUANTIFIER, 0)

        def VARIABLE(self):
            return self.getToken(logic_grammarParser.VARIABLE, 0)

        def formula(self):
            return self.getTypedRuleContext(logic_grammarParser.FormulaContext,0)


        def getRuleIndex(self):
            return logic_grammarParser.RULE_quantifiedFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantifiedFormula" ):
                listener.enterQuantifiedFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantifiedFormula" ):
                listener.exitQuantifiedFormula(self)




    def quantifiedFormula(self):

        localctx = logic_grammarParser.QuantifiedFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_quantifiedFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(logic_grammarParser.QUANTIFIER)
            self.state = 25
            self.match(logic_grammarParser.VARIABLE)
            self.state = 26
            self.formula()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(logic_grammarParser.AtomContext,0)


        def binaryOpRest(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(logic_grammarParser.BinaryOpRestContext)
            else:
                return self.getTypedRuleContext(logic_grammarParser.BinaryOpRestContext,i)


        def getRuleIndex(self):
            return logic_grammarParser.RULE_binaryFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryFormula" ):
                listener.enterBinaryFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryFormula" ):
                listener.exitBinaryFormula(self)




    def binaryFormula(self):

        localctx = logic_grammarParser.BinaryFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_binaryFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.atom()
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 29
                    self.binaryOpRest() 
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryOpRestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BINARY_OP(self):
            return self.getToken(logic_grammarParser.BINARY_OP, 0)

        def formula(self):
            return self.getTypedRuleContext(logic_grammarParser.FormulaContext,0)


        def getRuleIndex(self):
            return logic_grammarParser.RULE_binaryOpRest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOpRest" ):
                listener.enterBinaryOpRest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOpRest" ):
                listener.exitBinaryOpRest(self)




    def binaryOpRest(self):

        localctx = logic_grammarParser.BinaryOpRestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_binaryOpRest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(logic_grammarParser.BINARY_OP)
            self.state = 36
            self.formula()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(logic_grammarParser.NOT, 0)

        def formula(self):
            return self.getTypedRuleContext(logic_grammarParser.FormulaContext,0)


        def getRuleIndex(self):
            return logic_grammarParser.RULE_unaryFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryFormula" ):
                listener.enterUnaryFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryFormula" ):
                listener.exitUnaryFormula(self)




    def unaryFormula(self):

        localctx = logic_grammarParser.UnaryFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_unaryFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(logic_grammarParser.NOT)
            self.state = 39
            self.formula()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREDICATE(self):
            return self.getToken(logic_grammarParser.PREDICATE, 0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(logic_grammarParser.TermContext)
            else:
                return self.getTypedRuleContext(logic_grammarParser.TermContext,i)


        def getRuleIndex(self):
            return logic_grammarParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = logic_grammarParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(logic_grammarParser.PREDICATE)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 42
                self.match(logic_grammarParser.T__0)
                self.state = 43
                self.term()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 44
                    self.match(logic_grammarParser.T__2)
                    self.state = 45
                    self.term()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 51
                self.match(logic_grammarParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(logic_grammarParser.VARIABLE, 0)

        def CONSTANT(self):
            return self.getToken(logic_grammarParser.CONSTANT, 0)

        def getRuleIndex(self):
            return logic_grammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = logic_grammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






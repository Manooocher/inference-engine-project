# Generated from logic_grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .logic_grammarParser import logic_grammarParser
else:
    from logic_grammarParser import logic_grammarParser

# This class defines a complete listener for a parse tree produced by logic_grammarParser.
class logic_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by logic_grammarParser#formula.
    def enterFormula(self, ctx:logic_grammarParser.FormulaContext):
        pass

    # Exit a parse tree produced by logic_grammarParser#formula.
    def exitFormula(self, ctx:logic_grammarParser.FormulaContext):
        pass


    # Enter a parse tree produced by logic_grammarParser#quantifiedFormula.
    def enterQuantifiedFormula(self, ctx:logic_grammarParser.QuantifiedFormulaContext):
        pass

    # Exit a parse tree produced by logic_grammarParser#quantifiedFormula.
    def exitQuantifiedFormula(self, ctx:logic_grammarParser.QuantifiedFormulaContext):
        pass


    # Enter a parse tree produced by logic_grammarParser#binaryFormula.
    def enterBinaryFormula(self, ctx:logic_grammarParser.BinaryFormulaContext):
        pass

    # Exit a parse tree produced by logic_grammarParser#binaryFormula.
    def exitBinaryFormula(self, ctx:logic_grammarParser.BinaryFormulaContext):
        pass


    # Enter a parse tree produced by logic_grammarParser#binaryOpRest.
    def enterBinaryOpRest(self, ctx:logic_grammarParser.BinaryOpRestContext):
        pass

    # Exit a parse tree produced by logic_grammarParser#binaryOpRest.
    def exitBinaryOpRest(self, ctx:logic_grammarParser.BinaryOpRestContext):
        pass


    # Enter a parse tree produced by logic_grammarParser#unaryFormula.
    def enterUnaryFormula(self, ctx:logic_grammarParser.UnaryFormulaContext):
        pass

    # Exit a parse tree produced by logic_grammarParser#unaryFormula.
    def exitUnaryFormula(self, ctx:logic_grammarParser.UnaryFormulaContext):
        pass


    # Enter a parse tree produced by logic_grammarParser#atom.
    def enterAtom(self, ctx:logic_grammarParser.AtomContext):
        pass

    # Exit a parse tree produced by logic_grammarParser#atom.
    def exitAtom(self, ctx:logic_grammarParser.AtomContext):
        pass


    # Enter a parse tree produced by logic_grammarParser#term.
    def enterTerm(self, ctx:logic_grammarParser.TermContext):
        pass

    # Exit a parse tree produced by logic_grammarParser#term.
    def exitTerm(self, ctx:logic_grammarParser.TermContext):
        pass



del logic_grammarParser
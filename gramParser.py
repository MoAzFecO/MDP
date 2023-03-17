# Generated from gram.g4 by ANTLR 4.12.0
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
        4,1,13,133,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,28,8,1,
        10,1,12,1,31,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,42,8,1,
        10,1,12,1,45,9,1,1,1,3,1,48,8,1,1,2,1,2,1,2,1,2,5,2,54,8,2,10,2,
        12,2,57,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,69,8,3,10,
        3,12,3,72,9,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,80,8,4,10,4,12,4,83,9,
        4,1,4,1,4,1,5,1,5,5,5,89,8,5,10,5,12,5,92,9,5,1,6,1,6,3,6,96,8,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,110,8,7,10,7,
        12,7,113,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,126,
        8,8,10,8,12,8,129,9,8,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,
        0,133,0,18,1,0,0,0,2,47,1,0,0,0,4,49,1,0,0,0,6,60,1,0,0,0,8,75,1,
        0,0,0,10,86,1,0,0,0,12,95,1,0,0,0,14,97,1,0,0,0,16,116,1,0,0,0,18,
        19,3,2,1,0,19,20,3,8,4,0,20,21,3,10,5,0,21,22,5,0,0,1,22,1,1,0,0,
        0,23,24,5,1,0,0,24,29,5,12,0,0,25,26,5,7,0,0,26,28,5,12,0,0,27,25,
        1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,
        31,29,1,0,0,0,32,48,5,6,0,0,33,34,5,1,0,0,34,35,5,12,0,0,35,36,5,
        4,0,0,36,43,5,11,0,0,37,38,5,7,0,0,38,39,5,12,0,0,39,40,5,4,0,0,
        40,42,5,11,0,0,41,37,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,
        0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,48,5,6,0,0,47,23,1,0,0,0,47,
        33,1,0,0,0,48,3,1,0,0,0,49,50,5,1,0,0,50,55,5,12,0,0,51,52,5,7,0,
        0,52,54,5,12,0,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,
        1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,5,6,0,0,59,5,1,0,0,0,60,
        61,5,1,0,0,61,62,5,12,0,0,62,63,5,4,0,0,63,70,5,11,0,0,64,65,5,7,
        0,0,65,66,5,12,0,0,66,67,5,4,0,0,67,69,5,11,0,0,68,64,1,0,0,0,69,
        72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,70,1,0,0,
        0,73,74,5,6,0,0,74,7,1,0,0,0,75,76,5,2,0,0,76,81,5,12,0,0,77,78,
        5,7,0,0,78,80,5,12,0,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,
        81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,6,0,0,85,9,1,0,
        0,0,86,90,3,12,6,0,87,89,3,12,6,0,88,87,1,0,0,0,89,92,1,0,0,0,90,
        88,1,0,0,0,90,91,1,0,0,0,91,11,1,0,0,0,92,90,1,0,0,0,93,96,3,14,
        7,0,94,96,3,16,8,0,95,93,1,0,0,0,95,94,1,0,0,0,96,13,1,0,0,0,97,
        98,5,12,0,0,98,99,5,9,0,0,99,100,5,12,0,0,100,101,5,10,0,0,101,102,
        5,5,0,0,102,103,5,11,0,0,103,104,5,4,0,0,104,111,5,12,0,0,105,106,
        5,8,0,0,106,107,5,11,0,0,107,108,5,4,0,0,108,110,5,12,0,0,109,105,
        1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,114,
        1,0,0,0,113,111,1,0,0,0,114,115,5,6,0,0,115,15,1,0,0,0,116,117,5,
        12,0,0,117,118,5,5,0,0,118,119,5,11,0,0,119,120,5,4,0,0,120,127,
        5,12,0,0,121,122,5,8,0,0,122,123,5,11,0,0,123,124,5,4,0,0,124,126,
        5,12,0,0,125,121,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,
        1,0,0,0,128,130,1,0,0,0,129,127,1,0,0,0,130,131,5,6,0,0,131,17,1,
        0,0,0,10,29,43,47,55,70,81,90,95,111,127
    ]

class gramParser ( Parser ):

    grammarFileName = "gram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'States'", "'Actions'", "'transition'", 
                     "':'", "'->'", "';'", "','", "'+'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "STATES", "ACTIONS", "TRANSITION", "DPOINT", 
                      "FLECHE", "SEMI", "VIRG", "PLUS", "LCROCH", "RCROCH", 
                      "INT", "ID", "WS" ]

    RULE_program = 0
    RULE_defstates = 1
    RULE_statenoreward = 2
    RULE_statereward = 3
    RULE_defactions = 4
    RULE_transitions = 5
    RULE_trans = 6
    RULE_transact = 7
    RULE_transnoact = 8

    ruleNames =  [ "program", "defstates", "statenoreward", "statereward", 
                   "defactions", "transitions", "trans", "transact", "transnoact" ]

    EOF = Token.EOF
    STATES=1
    ACTIONS=2
    TRANSITION=3
    DPOINT=4
    FLECHE=5
    SEMI=6
    VIRG=7
    PLUS=8
    LCROCH=9
    RCROCH=10
    INT=11
    ID=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defstates(self):
            return self.getTypedRuleContext(gramParser.DefstatesContext,0)


        def defactions(self):
            return self.getTypedRuleContext(gramParser.DefactionsContext,0)


        def transitions(self):
            return self.getTypedRuleContext(gramParser.TransitionsContext,0)


        def EOF(self):
            return self.getToken(gramParser.EOF, 0)

        def getRuleIndex(self):
            return gramParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = gramParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.defstates()
            self.state = 19
            self.defactions()
            self.state = 20
            self.transitions()
            self.state = 21
            self.match(gramParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefstatesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATES(self):
            return self.getToken(gramParser.STATES, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.VIRG)
            else:
                return self.getToken(gramParser.VIRG, i)

        def DPOINT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.DPOINT)
            else:
                return self.getToken(gramParser.DPOINT, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.INT)
            else:
                return self.getToken(gramParser.INT, i)

        def getRuleIndex(self):
            return gramParser.RULE_defstates

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefstates" ):
                listener.enterDefstates(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefstates" ):
                listener.exitDefstates(self)




    def defstates(self):

        localctx = gramParser.DefstatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_defstates)
        self._la = 0 # Token type
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(gramParser.STATES)
                self.state = 24
                self.match(gramParser.ID)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 25
                    self.match(gramParser.VIRG)
                    self.state = 26
                    self.match(gramParser.ID)
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 32
                self.match(gramParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(gramParser.STATES)
                self.state = 34
                self.match(gramParser.ID)
                self.state = 35
                self.match(gramParser.DPOINT)
                self.state = 36
                self.match(gramParser.INT)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 37
                    self.match(gramParser.VIRG)
                    self.state = 38
                    self.match(gramParser.ID)
                    self.state = 39
                    self.match(gramParser.DPOINT)
                    self.state = 40
                    self.match(gramParser.INT)
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 46
                self.match(gramParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatenorewardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATES(self):
            return self.getToken(gramParser.STATES, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.VIRG)
            else:
                return self.getToken(gramParser.VIRG, i)

        def getRuleIndex(self):
            return gramParser.RULE_statenoreward

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatenoreward" ):
                listener.enterStatenoreward(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatenoreward" ):
                listener.exitStatenoreward(self)




    def statenoreward(self):

        localctx = gramParser.StatenorewardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statenoreward)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(gramParser.STATES)
            self.state = 50
            self.match(gramParser.ID)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 51
                self.match(gramParser.VIRG)
                self.state = 52
                self.match(gramParser.ID)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaterewardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATES(self):
            return self.getToken(gramParser.STATES, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def DPOINT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.DPOINT)
            else:
                return self.getToken(gramParser.DPOINT, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.INT)
            else:
                return self.getToken(gramParser.INT, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.VIRG)
            else:
                return self.getToken(gramParser.VIRG, i)

        def getRuleIndex(self):
            return gramParser.RULE_statereward

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatereward" ):
                listener.enterStatereward(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatereward" ):
                listener.exitStatereward(self)




    def statereward(self):

        localctx = gramParser.StaterewardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statereward)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(gramParser.STATES)
            self.state = 61
            self.match(gramParser.ID)
            self.state = 62
            self.match(gramParser.DPOINT)
            self.state = 63
            self.match(gramParser.INT)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 64
                self.match(gramParser.VIRG)
                self.state = 65
                self.match(gramParser.ID)
                self.state = 66
                self.match(gramParser.DPOINT)
                self.state = 67
                self.match(gramParser.INT)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefactionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTIONS(self):
            return self.getToken(gramParser.ACTIONS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.VIRG)
            else:
                return self.getToken(gramParser.VIRG, i)

        def getRuleIndex(self):
            return gramParser.RULE_defactions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefactions" ):
                listener.enterDefactions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefactions" ):
                listener.exitDefactions(self)




    def defactions(self):

        localctx = gramParser.DefactionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_defactions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(gramParser.ACTIONS)
            self.state = 76
            self.match(gramParser.ID)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 77
                self.match(gramParser.VIRG)
                self.state = 78
                self.match(gramParser.ID)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransitionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trans(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramParser.TransContext)
            else:
                return self.getTypedRuleContext(gramParser.TransContext,i)


        def getRuleIndex(self):
            return gramParser.RULE_transitions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransitions" ):
                listener.enterTransitions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransitions" ):
                listener.exitTransitions(self)




    def transitions(self):

        localctx = gramParser.TransitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_transitions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.trans()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 87
                self.trans()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def transact(self):
            return self.getTypedRuleContext(gramParser.TransactContext,0)


        def transnoact(self):
            return self.getTypedRuleContext(gramParser.TransnoactContext,0)


        def getRuleIndex(self):
            return gramParser.RULE_trans

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrans" ):
                listener.enterTrans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrans" ):
                listener.exitTrans(self)




    def trans(self):

        localctx = gramParser.TransContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_trans)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.transact()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.transnoact()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def LCROCH(self):
            return self.getToken(gramParser.LCROCH, 0)

        def RCROCH(self):
            return self.getToken(gramParser.RCROCH, 0)

        def FLECHE(self):
            return self.getToken(gramParser.FLECHE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.INT)
            else:
                return self.getToken(gramParser.INT, i)

        def DPOINT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.DPOINT)
            else:
                return self.getToken(gramParser.DPOINT, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.PLUS)
            else:
                return self.getToken(gramParser.PLUS, i)

        def getRuleIndex(self):
            return gramParser.RULE_transact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransact" ):
                listener.enterTransact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransact" ):
                listener.exitTransact(self)




    def transact(self):

        localctx = gramParser.TransactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_transact)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(gramParser.ID)
            self.state = 98
            self.match(gramParser.LCROCH)
            self.state = 99
            self.match(gramParser.ID)
            self.state = 100
            self.match(gramParser.RCROCH)
            self.state = 101
            self.match(gramParser.FLECHE)
            self.state = 102
            self.match(gramParser.INT)
            self.state = 103
            self.match(gramParser.DPOINT)
            self.state = 104
            self.match(gramParser.ID)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 105
                self.match(gramParser.PLUS)
                self.state = 106
                self.match(gramParser.INT)
                self.state = 107
                self.match(gramParser.DPOINT)
                self.state = 108
                self.match(gramParser.ID)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransnoactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def FLECHE(self):
            return self.getToken(gramParser.FLECHE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.INT)
            else:
                return self.getToken(gramParser.INT, i)

        def DPOINT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.DPOINT)
            else:
                return self.getToken(gramParser.DPOINT, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.PLUS)
            else:
                return self.getToken(gramParser.PLUS, i)

        def getRuleIndex(self):
            return gramParser.RULE_transnoact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransnoact" ):
                listener.enterTransnoact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransnoact" ):
                listener.exitTransnoact(self)




    def transnoact(self):

        localctx = gramParser.TransnoactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_transnoact)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(gramParser.ID)
            self.state = 117
            self.match(gramParser.FLECHE)
            self.state = 118
            self.match(gramParser.INT)
            self.state = 119
            self.match(gramParser.DPOINT)
            self.state = 120
            self.match(gramParser.ID)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 121
                self.match(gramParser.PLUS)
                self.state = 122
                self.match(gramParser.INT)
                self.state = 123
                self.match(gramParser.DPOINT)
                self.state = 124
                self.match(gramParser.ID)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






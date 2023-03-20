from antlr4 import *
from gramLexer import gramLexer
from gramListener import gramListener
from gramParser import gramParser

from class_mdp import MDP

        
class gramPrintListener(gramListener):

    def __init__(self, mdp):
        self.mdp = mdp
        
    def enterDefstates(self, ctx):
        r = ctx.INT()
        if r == []:
            print("States: %s" % str([str(x) for x in ctx.ID()]))
            for x in ctx.ID():
                state = str(x)
                if self.mdp.init is None:
                    self.mdp.init = state
                self.mdp.add_state(state)
        else :
            liste = zip(ctx.ID(),ctx.INT())
            for x, reward in liste:
                state = str(x)
                if self.mdp.init is None:
                    self.mdp.init = state
                print(f"States {state} with reward {reward}")
                self.mdp.add_state_reward(state, reward)
                

    def enterDefactions(self, ctx):
        print("Actions: %s" % str([str(x) for x in ctx.ID()]))
        for x in ctx.ID():
            action = str(x)
            self.mdp.add_action(action)

    def enterTransact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        act = ids.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]
        print("Transition from " + dep + " with action "+ act + " and targets " + str(ids) + " with weights " + str(weights))
        self.mdp.add_transAct(dep, act, ids, weights)
        
    def enterTransnoact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]
        print("Transition from " + dep + " with no action and targets " + str(ids) + " with weights " + str(weights))
        self.mdp.add_transNoAct(dep, ids, weights)

            

def main():
    fichier = input("Nom du fichier : ")
    lexer = gramLexer(FileStream(fichier))
    stream = CommonTokenStream(lexer)
    parser = gramParser(stream)
    tree = parser.program()
    printer = gramPrintListener(MDP())
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    printer.mdp.Graph(printer.mdp.init, 'mdp')
    printer.mdp.mode()
    

   

if __name__ == '__main__':
    main()

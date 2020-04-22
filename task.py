from TokenClass import *
from OperatorNode import *


from LexerClass import LexerClass

from ParserClass import ParserClass








#############################

class ASTNodeVisitorClass(object):
    def func_visit(self, node):
        method_name = 'func_visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.func_generic_visit)
        return visitor(node)

    def func_generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class InterpreterClass(ASTNodeVisitorClass):
    def __init__(self, parser):
        self.GLOBAL_TABLE = {}
        self.parser = parser

    def func_visit_MathOperatorNode(self, node):
        if node.op.type == PLUS:
            return self.func_visit(node.left) + self.func_visit(node.right)
        elif node.op.type == MINUS:
            return self.func_visit(node.left) - self.func_visit(node.right)
        elif node.op.type == MULESSTHANIPLY:
            return self.func_visit(node.left) * self.func_visit(node.right)
        elif node.op.type == DEVIDE:
            return self.func_visit(node.left) / self.func_visit(node.right)

    def func_visit_NumberNode(self, node):
        return node.value

    def func_visit_AssignNode(self, node):
        var_name = node.left.value
        self.GLOBAL_TABLE[var_name] = self.func_visit(node.right)

    def func_visit_BooleanNode(self, node):
        # print('visit_Boolean')
        if node.op.type == EQUAL:
            return self.func_visit(node.left) == self.func_visit(node.right)
        elif node.op.type == LESSTHAN:

            return self.func_visit(node.left) < self.func_visit(node.right)
        elif node.op.type == GREATERTHAN:
            return self.func_visit(node.left) > self.func_visit(node.right)
        elif node.op.type == AND:
            if self.func_visit(node.left) == False:
                return False
            else:
                return self.func_visit(node.left) and self.func_visit(node.right)
        elif node.op.type == OR:
            if self.func_visit(node.left) == True:
                return True
            else:
                return self.func_visit(node.left) or self.func_visit(node.right)
        elif node.op.type == NOT:
            return not self.func_visit(node.right)

    def func_visit_WhileNode(self, node):
        truth_val = self.func_visit(node.left)

        loopCounter = 0
        while (truth_val is True) and (loopCounter <= 10000):
            self.func_visit(node.right)
            truth_val = self.func_visit(node.left)
            loopCounter += 1

    def func_visit_IfNode(self, node):
        truth_val = self.func_visit(node.left)

        if truth_val is True:
            self.func_visit(node.right)
        else:
            self.func_visit(node.wrong)

    def func_visit_VarNode(self, node):
        var_name = node.value
        val = self.GLOBAL_TABLE.get(var_name)
        if val is None:
            return 0
        else:
            return val

    def func_visit_NoOpNode(self, node):
        pass

    def func_visit_CompoundNode(self, node):
        for child in node.children:
            self.func_visit(child)

    def func_interpret(self):
        tree = self.parser.parse()
        self.func_visit(tree)
        str = "{"
        for key, value in sorted(self.GLOBAL_TABLE.items()):
            str = str + '{} → {}, '.format(key, value)
        if len(self.GLOBAL_TABLE) >= 1:
            str = str.rstrip()[:-1] + "}"
        else:
            str = str.rstrip() + "}"
        return str

    def func_print_table(self):
        print(self.GLOBAL_TABLE)


def main():
    while True:
        try:
            try:
                text = raw_input('')
            except NameError:  
                text = input('')
        except EOFError:
            break
        if not text:
            continue

        lexer = LexerClass(text)
        parser = ParserClass(lexer)
        interpreter = InterpreterClass(parser)
        resuLESSTHAN = interpreter.func_interpret()
        print(resuLESSTHAN)


if __name__ == '__main__':
    main()

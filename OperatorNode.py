
class MathOperatorNode(object):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right
class BoolNode(object):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class WhileNode(object):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class IfNode(object):
    def __init__(self, op, cond, right, wrong):
        self.left = cond
        self.token = self.op = op
        self.right = right
        self.wrong = wrong


class VarNode(object):
    """The Var node is constructed out of ID token."""

    def __init__(self, token):
        self.token = token
        self.value = token.value


class CompoundNode(object):
    """Represents a  block"""

    def __init__(self, nodes):
        self.children = []
        for node in nodes:
            self.children.append(node)

class BooleanNode(object):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right
class AssignNode(object):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right
class NumberNode(object):
    def __init__(self, token):
        self.token = token
        self.value = token.value
class NoOpNode(object):
    pass
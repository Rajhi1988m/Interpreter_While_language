WHILE, DO, IF, THEN, ELSE, SKIP, ID, INTEGER, TRUE, FALSE, NOT, PLUS, MINUS, MULESSTHANIPLY, DEVIDE, AND, OR, LPAREN, RPAREN, ASSIGN, EQUAL, GREATERTHAN, LESSTHAN, LBRACE, RBRACE, SEMI,  EOF = (
    'WHILE', 'DO', 'IF', 'THEN', 'ELSE', 'SKIP', 'ID', 'INTEGER', 'TRUE', 'FALSE', 'NOT', 'PLUS', 'MINUS', 'MULESSTHANIPLY', 'DEVIDE', '∧', '∨', '(', ')', ':=', '=', '>', '<', '{', '}', 'SEMI',  'EOF'
)
class TokenClass(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

from TokenClass import *
WHILE, DO, IF, THEN, ELSE, SKIP, ID, INTEGER, TRUE, FALSE, NOT, PLUS, MINUS, MULESSTHANIPLY, DEVIDE, AND, OR, LPAREN, RPAREN, ASSIGN, EQUAL, GREATERTHAN, LESSTHAN, LBRACE, RBRACE, SEMI,  EOF = (
    'WHILE', 'DO', 'IF', 'THEN', 'ELSE', 'SKIP', 'ID', 'INTEGER', 'TRUE', 'FALSE', 'NOT', 'PLUS', 'MINUS', 'MULESSTHANIPLY', 'DEVIDE', '∧', '∨', '(', ')', ':=', '=', '>', '<', '{', '}', 'SEMI',  'EOF'
)
class LexerClass(object):
    def __init__(self, text):
        self.tokens = text.split(' ')
        self.location = 0
        self.token = self.tokens[self.location]

    def error_func(self):
        raise Exception('Invalid character')

    def move_next(self):
        self.location += 1
        if self.location > len(self.tokens) - 1:
            self.token = None  # Indicates end of input
        else:
            self.token = self.tokens[self.location]

    def check_token_is_integer(self, token):
        try:
            r = int(token)
            return True
        except:
            return False

    def read_next_token(self):

        while self.token is not None:
            if self.token == '':
                self.location += 1
                continue

            if self.token == 'while':
                self.move_next()
                return TokenClass(WHILE, 'while')
            if self.token == 'do':
                self.move_next()
                return TokenClass(DO, 'do')

            if self.token == 'if':
                self.move_next()
                return TokenClass(IF, 'if')
            if self.token == 'then':
                self.move_next()
                return TokenClass(THEN, 'then')
            if self.token == 'else':
                self.move_next()
                return TokenClass(ELSE, 'else')

            if self.token == 'skip':
                self.move_next()
                return TokenClass(SKIP, 'skip')

            if self.check_token_is_integer(self.token):
                the_token = TokenClass(INTEGER, int(self.token))
                self.move_next()
                return the_token

            if self.token == '+':
                self.move_next()
                return TokenClass(PLUS, '+')

            if self.token == '-':
                self.move_next()
                return TokenClass(MINUS, '-')

            if self.token == '*':
                self.move_next()
                return TokenClass(MULESSTHANIPLY, '*')

            if self.token == '/':
                self.move_next()
                return TokenClass(DEVIDE, '/')

            if self.token == '∧':
                self.move_next()
                return TokenClass(AND, '∧')

            if self.token == '∨':
                self.move_next()
                return TokenClass(OR, '∨')

            if self.token == '(':
                self.move_next()
                return TokenClass(LPAREN, '(')

            if self.token == ')':
                self.move_next()
                return TokenClass(RPAREN, ')')

            if self.token == '{':
                self.move_next()
                return TokenClass(LBRACE, '{')

            if self.token == '}':
                self.move_next()
                return TokenClass(RBRACE, '}')

            if self.token == ';':
                self.move_next()
                return TokenClass(SEMI, ';')

            if self.token == ':=':
                self.move_next()
                return TokenClass(ASSIGN, ':=')

            if self.token == '=':
                self.move_next()
                return TokenClass(EQUAL, '=')

            if self.token == '>':
                self.move_next()
                return TokenClass(GREATERTHAN, '>')

            if self.token == '<':
                self.move_next()
                return TokenClass(LESSTHAN, '<')

            if self.token == 'true':
                self.move_next()
                return TokenClass(TRUE, 'true')

            if self.token == 'false':
                self.move_next()
                return TokenClass(FALSE, 'false')
            if self.token == '¬':
                self.move_next()
                return TokenClass(NOT, '¬')

            if self.token.isidentifier():
                tk = TokenClass(ID, self.token)
                self.move_next()
                return tk

            self.error_func()

        return TokenClass(EOF, None)
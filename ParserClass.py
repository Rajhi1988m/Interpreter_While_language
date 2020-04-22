from TokenClass import *
from OperatorNode import *

class ParserClass(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.token = self.lexer.read_next_token()

    def func_error(self):
        raise Exception('Invalid syntax')

    def match_token(self, token_type):
        if self.token.type == token_type:
            self.token = self.lexer.read_next_token()
        else:
            self.func_error()

    def func_factor(self):
        """factor : INTEGER """
        token = self.token
        if token.type == INTEGER:
            self.match_token(INTEGER)
            return NumberNode(token)
        elif token.type == ID:
            self.match_token(ID)
            # print('get VAR')
            return VarNode(token)
        elif token.type == LPAREN:
            self.match_token(LPAREN)
            node = self.func_expression()
            self.match_token(RPAREN)
            return node

    def func_term(self):
        """term : factor ((MULESSTHANIPLY | DEVIDE) factor)*"""
        node = self.func_factor()

        while self.token.type in (MULESSTHANIPLY, DEVIDE):
            token = self.token
            if token.type == MULESSTHANIPLY:
                self.match_token(MULESSTHANIPLY)
            elif token.type == DEVIDE:
                self.match_token(DEVIDE)

            node = MathOperatorNode(left=node, op=token, right=self.func_factor())

        return node

    def func_variable(self):
        """
        variable : ID
        """
        var_node = VarNode(self.token)
        self.match_token(ID)
        return var_node

    def func_skip(self):
        """An skip production"""
        self.match_token(SKIP)
        return NoOpNode()

    def func_expression(self):
        
        node = self.func_term()

        while self.token.type in (PLUS, MINUS):
            token = self.token
            if token.type == PLUS:
                self.match_token(PLUS)
            elif token.type == MINUS:
                self.match_token(MINUS)

            node = MathOperatorNode(left=node, op=token, right=self.func_term())

        return node

    def func_assignment_statement(self):
        """
        assignment_statement : variable ASSIGN expr
        """
        left = self.func_variable()
        token = self.token
        self.match_token(ASSIGN)
        right = self.func_expression()
        node = AssignNode(left, token, right)
        return node

    def func_bool_expression(self):
        """
        assignment_statement : variable := expr
        """
        node = self.func_bool_term()

        while self.token.type in (OR):
            token = self.token
            if token.type == OR:
                self.match_token(OR)
            node = BooleanNode(left=node, op=token, right=self.func_bool_term())

        return node
        

    def func_bool_term(self):
        """
        assignment_statement : variable := expr
        """
        node = self.func_bool_factor()

        while self.token.type in (AND):
            token = self.token
            if token.type == AND:
                self.match_token(AND)

            node = BooleanNode(left=node, op=token, right=self.func_bool_factor())

        return node

    def func_bool_factor(self):
        token = self.token
        if self.token.type == TRUE:
            left = NumberNode(TokenClass(INTEGER, 1))
            right = NumberNode(TokenClass(INTEGER, 1))
            node = BooleanNode(left, TokenClass(EQUAL, '='), right)
            return node
        elif self.token.type == FALSE:
            left = NumberNode(TokenClass(INTEGER, 1))
            right = NumberNode(TokenClass(INTEGER, 2))
            node = BooleanNode(left, TokenClass(EQUAL, '='), right)
            return node
        elif token.type == NOT:
            self.match_token(NOT)
            right = self.func_bool_factor()
            node = BooleanNode(None, token, right)
            return node
        elif token.type == LPAREN:
            self.match_token(LPAREN)
            node = self.func_bool_expression()
            self.match_token(RPAREN)
            return node
        else:
            left = self.func_expression()
            token = self.token
            if token.type == EQUAL:
                self.match_token(EQUAL)
            elif token.type == LESSTHAN:
                self.match_token(LESSTHAN)
            elif token.type == GREATERTHAN:
                self.match_token(GREATERTHAN)
            right = self.func_expression()
            node = BooleanNode(left, token, right)
            return node

    def func_if_statement(self):
        self.match_token(IF)
        left = self.func_bool_expression()
        token = self.token
        if self.token.type == TRUE:
            self.match_token(TRUE)
        elif self.token.type == FALSE:
            self.match_token(FALSE)
        # print(self.token)
        self.match_token(THEN)
        right = self.func_statement()
        self.match_token(ELSE)
        wrong = self.func_statement()
        node = IfNode(token, left, right, wrong)
        return node

    def func_while_statement(self):
        self.match_token(WHILE)
        left = self.func_bool_expression()

        token = self.token
        if self.token.type == TRUE:
            self.match_token(TRUE)
        elif self.token.type == FALSE:
            self.match_token(FALSE)
        self.match_token(DO)
        if self.token.type == LBRACE:
            self.match_token(LBRACE)
            right = self.func_statement_list()
            self.match_token(RBRACE)
        else:
            right = self.func_statement()
        node = WhileNode(left, token, right)
        return node

    def func_program(self):
        """program : compound_statement """
        nodes = self.func_statement_list()
        return nodes

    def func_statement_list(self):
        """
        statement_list : statement
                       | statement ; statement_list
        """
        node = self.func_statement()

        result = [node]

        while self.token.type == SEMI:
            self.match_token(SEMI)
            result.append(self.func_statement())

        if self.token.type == ID:
            self.func_error()
        node = CompoundNode(result)
        return node

    def func_statement(self):
        """
        statement : compound_statement
                  | assignment_statement
                  | skip
        """
        if self.token.type == ID:
            node = self.func_assignment_statement()
        elif self.token.type == WHILE:
            node = self.func_while_statement()
        elif self.token.type == IF:
            node = self.func_if_statement()
        elif self.token.type == SKIP:
            node = self.func_skip()
        else:
            node = self.func_expression()
        return node

    def parse(self):
        return self.func_statement_list()
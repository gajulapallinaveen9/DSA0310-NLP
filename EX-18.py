import re

class FOPCParser:
    def __init__(self, text):
        self.tokens = re.findall(r'->|[A-Za-z_]\w*|[()~&|.,]', text)
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, expected=None):
        tok = self.peek()
        if tok is None or (expected and tok != expected):
            raise SyntaxError(f'Expected {expected!r} but found {tok!r}')
        self.pos += 1
        return tok

    def parse(self):
        tree = self.formula()
        if self.peek() is not None:
            raise SyntaxError(f'Unexpected token {self.peek()!r}')
        return tree

    def formula(self):
        left = self.disjunction()
        if self.peek() == '->':
            self.eat('->')
            return ('->', left, self.formula())
        return left

    def disjunction(self):
        node = self.conjunction()
        while self.peek() == '|':
            self.eat('|')
            node = ('|', node, self.conjunction())
        return node

    def conjunction(self):
        node = self.unary()
        while self.peek() == '&':
            self.eat('&')
            node = ('&', node, self.unary())
        return node

    def unary(self):
        tok = self.peek()
        if tok == '~':
            self.eat()
            return ('~', self.unary())
        if tok in ('all', 'exists'):
            self.eat()
            var = self.eat()
            self.eat('.')
            return (tok, var, self.formula())
        if tok == '(':
            self.eat('(')
            node = self.formula()
            self.eat(')')
            return node
        return self.atom()

    def atom(self):
        pred = self.eat()
        self.eat('(')
        args = [self.eat()]
        while self.peek() == ',':
            self.eat(',')
            args.append(self.eat())
        self.eat(')')
        return (pred, tuple(args))

tests = ['all x. (Man(x) -> Mortal(x))',
         'exists y. Loves(John, y) & ~Sleeps(y)',
         'Man(x) & Mortal(x) -> Happy(x)',
         'Man(x']
for t in tests:
    print(t)
    try:
        print('  ', FOPCParser(t).parse())
    except SyntaxError as e:
        print('   SyntaxError:', e)

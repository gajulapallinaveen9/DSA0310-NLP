class FSA:
    def __init__(self):
        self.start = 'q0'
        self.accepting = {'q2'}
        self.delta = {
            ('q0', 'a'): 'q1', ('q0', 'b'): 'q0',
            ('q1', 'a'): 'q1', ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q1', ('q2', 'b'): 'q0',
        }

    def accepts(self, s):
        state = self.start
        for ch in s:
            if (state, ch) not in self.delta:
                return False
            state = self.delta[(state, ch)]
        return state in self.accepting

m = FSA()
for w in ['ab', 'aab', 'abab', 'abba', 'ba', 'bbb', '']:
    print(f'{w!r:8}', '->', 'Accepted' if m.accepts(w) else 'Rejected')

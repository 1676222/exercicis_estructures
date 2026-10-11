class MinStack:
    """
    problema min_stack
    exemple: 
    s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
s.getMin()   # retorna -3
s.pop()
s.top()      # retorna 0
s.getMin()   # retorna -2

Restriccions
Els valors són enters entre −2³¹ i 2³¹ − 1.
Els mètodes pop, top i getMin sempre es cridaran sobre una Stack no buida.
Es faran com a màxim 3·10⁴ crides als mètodes.
Cada objecte MinStack ha de ser independent dels altres. Dues Stacks diferents no poden compartir dades.
    """

    def __init__(self):
        self.stack = []#cada pila independent

    def push(self, val: int) -> None:
        if self.stack:
            min_actual = self.stack[-1][1]
            if val < min_actual:
                min_actual = val
        else:
            min_actual = val
        self.stack.append((val, min_actual))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

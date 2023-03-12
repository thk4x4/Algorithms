from operator import add, mul, sub, floordiv


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        raise IndexError('empty stack')


def main():
    seq = list(map(str, input().split()))
    OPERATOR = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': floordiv
    }
    calc = Stack()
    for i in seq:
        if i not in OPERATOR:
            calc.push(int(i))
        else:
            a = calc.pop()
            b = calc.pop()
            calc.push(OPERATOR[i](b, a))
    print(calc.pop())


if __name__ == "__main__":
    main()

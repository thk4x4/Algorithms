class Deque:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_front(self, x):
        if self.size != self.max_n:
            self.queue[self.head - 1] = x
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def push_back(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            raise ValueError

    def pop_front(self):
        if self.is_empty():
            raise ValueError
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            raise ValueError
        x = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x


def main():
    commands_count = int(input())
    s = int(input())
    q = Deque(s)
    for _ in range(commands_count):
        command, *args = input().split()
        try:
            getattr(q, command)(*args)
        except ValueError:
            print('error')


if __name__ == '__main__':
    main()

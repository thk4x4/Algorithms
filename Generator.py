import sys
n = int(sys.stdin.readline())


def bracket(count, s='', left=0, right=0):
    if left == count and right == count:
        print(s)
    else:
        if left < count:
            bracket(count, s + '(', left+1, right)
        if right < left:
            bracket(count, s + ')', left, right+1)
    bracket(n)




class Stack:

    def __init__(self):
        self.lst = []

    def isEmpty(self):
        if not self.lst:
            print('True')
        else:
            print('False')

    def push(self, digit):
        self.digit = digit
        self.lst.append(self.digit)


    def pop(self):
        return self.lst.pop()

    def peek(self):
        return self.lst[-1]

    def size(self):
        return len(self.lst)


def balanced(s):
    stack = Stack()
    bopen, bclose = "(", ")"
    for c in s:
        if c == bopen:
            stack.push(c)
        elif c == bclose:
            if stack.isEmpty():
                return False
            else:
                stackTop = stack.pop()
    return stack.isEmpty()


print(balanced(input()))


# lst = Stack()
# lst.isEmpty()
# lst.push(4)
# lst.push(4)
# lst.push(3)
# print(lst.pop())
# print(lst.peek())
# print(lst.size())
# lst.isEmpty()




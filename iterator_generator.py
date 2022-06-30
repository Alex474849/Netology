import self as self


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class Iter():
    """
    Iterator
    """

    def __init__(self, lst, n):
        self.lst = lst
        self.n = n

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        flat_lst = []
        for i in self.lst:
            for z in i:
                flat_lst.append(z)

            self.cursor += 1
            if self.cursor == self.n:
                raise StopIteration
        return flat_lst


iter = Iter(nested_list, 5)
for u in iter:
    print(u)


# def ge(*args, **kwargs):
#     for item in args:
#         for z in item:
#             for q in z:
#                 yield q
#
#
#
# for i in ge(nested_list):
#     print(i)




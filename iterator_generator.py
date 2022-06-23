nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class Iter():
    """
    Iterator
    """

    def __init__(self, n=1):
        self.n = n

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.n:
            raise StopIteration
        return nested_list


# iter = Iter(2)
# for i in iter:
#     for z in i:
#         for q in z:
            # print(q)


# gen

def ge(*args, **kwargs):
    for item in args:
        yield item



for i in ge(nested_list):
    for z in i:
        for q in z:
            print(q)




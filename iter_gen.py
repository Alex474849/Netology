nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
def lst0(lst):
    for i in nested_list:
        for z in i:
           print(z)


def lst1(lst):

    result = []
    for i in lst:
        for z in i:
            result.append(z)
    return result

def gen(lst):
    pass



print(lst1(nested_list))
print(lst0(nested_list))
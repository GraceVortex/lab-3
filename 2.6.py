stri = input("enter string: ")

def str_maker(stri):
    reversed_iter = reversed(stri)
    reversed_str = ''.join(reversed_iter)
    return reversed_str

res = str_maker(stri)
print(res)
from itertools import permutations

stri = input("enter string: ")

perms = permutations(stri)
perms_list = list(perms)

print(perms_list)

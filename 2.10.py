my_lst = []
while True:
    usrcin = input("enter smth: ")
    if usrcin == "":
        break
    else:
        my_lst.append(usrcin)

        
def teks(my_lst):
    res_lst = []
    for i in range(len(my_lst)):
        rem_el = my_lst[i]
        new_lst = my_lst[:1]+my_lst[i+1:]
        if rem_el not in new_lst:
            res_lst.append(rem_el)
    return res_lst

res = teks(my_lst)
print(res)

        
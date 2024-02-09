stri = input("enter string, mf: ")
def teks_pal(stri):
    rev_str = stri[::-1]
    if rev_str == stri:
        return True
    else:
        return False
    
res = teks_pal(stri)
print(res)
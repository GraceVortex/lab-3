lst = []

while True:
    usrcin = input("Enter smth: ")
    if usrcin == '':
        break
    else:
        lst.append(int(usrcin))

def printer(lst):
    result = ""
    for x in lst:
        hist = ""
        for i in range(x):
            hist+="*"
        result += hist + "\n"
    return result

res = printer(lst)
print(res)
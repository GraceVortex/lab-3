mylst = []
while True:
    usrcin =  input("Enter smth: ")

    if usrcin == '':
        break
    else:
        mylst.append(int(usrcin))
def teks(mylst):
    x = 0
    for i in range(len(mylst)-2):
        if mylst[i] == 0 and mylst[i+1] == 0 and mylst[i+2] == 7 : 
            x += 1
    if x>0:
        return True
    else:
        return False
    
res = teks(mylst)
print(res)
    

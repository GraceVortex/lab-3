from math import pi
r = int(input("enter radius: "))

def vol(r):
    vol = 4/3*pi*(r**3)
    return vol

res = vol(r)
print(res)
heads = int(input("how many heads?: "))
legs = int(input("how many legs?: "))

def counter(heads, legs):
    r = legs/2 - heads
    c = heads - r
    return c, r

chicks , rabs = map(int, counter(heads, legs))
print(f"number of rabbits is {rabs} number of chickens is {chicks} ")

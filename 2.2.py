far = float(input("could you pls tell me temp in Farenheits: "))

def conv(far):
    c = (5 / 9) * (far - 32)
    return c

res = conv(far)
print(f"temp in celsium is {res} degrees")
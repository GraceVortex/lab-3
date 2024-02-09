grams = float(input("how many grams u want?"))
def conve(grams):
    ounces = 28.3495231 * grams
    return ounces

res = conve(grams)
print(f"unfort we sell  only in ounces , so you receive {res} ounces")
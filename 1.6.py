numbers = [1,2,3,4,5,6,7,8,9]

def is_Prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
prime_numbers = filter(lambda x: is_Prime(x), numbers)

result = list(prime_numbers)

print(result)
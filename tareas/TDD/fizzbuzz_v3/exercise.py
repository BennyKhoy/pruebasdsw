#Fizzbuzz
def fizzbuzz(a: int):
    if(a % 3 == 0): return "Fizz"
    elif(a % 5 == 0): return "Buzz"
    return str(a)
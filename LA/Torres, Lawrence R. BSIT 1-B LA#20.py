fibo = int(input("Fibonacci: "))
def fibonacci(fibo):
    return fibo if fibo <= 1 else fibonacci(fibo - 1) + fibonacci(fibo - 2)
print(fibonacci(fibo))  
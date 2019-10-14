def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return n

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def menu():
    steps = ("1. Fibonacci \n""2. Factorial\n""3. Exit\n")
    choice = input(steps)
    return int(choice)
while True:
    try:
        choice = menu()
        if choice == 1:
            n = int(input("Enter a number to do the fibonacci : "))
            fibonacci(n)
            print(fibonacci(n))
        elif choice == 2:
            n = int(input("Enter a number to search the factorial : "))
            factorial(n)
            print(factorial(n))
        elif choice == 3:
            break
    except ValueError:
        continue
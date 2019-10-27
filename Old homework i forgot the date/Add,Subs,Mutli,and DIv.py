print("Welcome to the never ending calculator ! ")

def addition():
    shouldTerminate = False
    total = 0
    while (shouldTerminate != True):
        num1 = input ("Enter your number : ")
        if(num1 != "stop"):
            total = total + int(num1)
        else:
            shouldTerminate = True
            break
        print(total)

def substraction():
    shouldTerminate = False
    total = 0
    while (shouldTerminate != True):
        num1 = input ("Enter your number : ")
        if(num1 != "end"):
            total = total - int(num1)
        else:
            shouldTerminate = True
            break
        print(total)

def multiplication():
    shouldTerminate = False
    total = 1
    while (shouldTerminate != True):
        num1 = input("Enter your number : ")
        if (num1 != "end"):
            total = total * int(num1)
        else:
            shouldTerminate = True
            break
        print(total)

def division():
    shouldTerminate = False
    total = 1
    while (shouldTerminate != True):
        num1 = input("Enter your number : ")
        if (num1 != "end"):
            total = total / int(num1)
        else:
            shouldTerminate = True
            break
        print(total)

def menu():
    steps = ("1. Add \n""2. Subtraction\n""3. Multipiclation\n""4. Division\n""5. Exit\n")
    choice = input(steps)
    return int(choice)
while True:
    try:
        choice = menu()
        if choice == 1:
            addition()
        elif choice == 2:
            substraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        elif choice == 5:
            break
    except ValueError:
        continue

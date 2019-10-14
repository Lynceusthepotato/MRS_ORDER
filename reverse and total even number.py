def reverse():
    a = input("Write here : ")[::-1]
    print(a)

def total_of_even_number():
    valuesearch = int(input("Enter the max value : "))
    total = 0

    for numb in range(1, valuesearch+1): # +1 so it stop at the number the user input
        if(numb % 2 == 0):
            print("{0}".format(numb))
            total = total + numb
    print("The total of even numbers from 1 to {0} = {1}".format(numb, total)) #number goes to {0} and total goes to {1} well format is useful

def menu():
    steps = ("1. Reverse/Palindrome \n""2. Total of even number\n""3. Exit\n")
    choice = input(steps)
    return int(choice)
while True:
    try:
        choice = menu()
        if choice == 1:
            reverse()
        elif choice == 2:
            total_of_even_number()
        elif choice == 3:
            break
    except ValueError:
        continue
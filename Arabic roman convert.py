def arb_to_roman(num):
    value = [(10, 'X'), (5, 'V'), (1, 'I')]
    result = []
    for (arabic, roman) in value:
        (factor, num) = divmod(num, arabic)
        result.append(roman * factor)
        if num == 0:
            break
    return "".join(result)


def roman_to_arb():
    val = {'I': 1, 'V': 5, 'X': 10}
    string = str(input('Enter a roman numeral: '))
    string = string.upper()
    total = 0
    while string:
        if len(string) == 1 or val[string[0]] >= val[string[1]]:
            total += val[string[0]]
            string = string[1:]
        else:
            total += val[string[1]] - val[string[0]]
            string = string[2:]
    print(total)

def menu():
    steps = ("1. Arabic to Roman \n""2. Roman to Arabic\n""3. Exit\n")
    choice = input(steps)
    return int(choice)
while True:
    try:
        choice = menu()
        if choice == 1:
            num = int(input("Enter any number between 1 and 20: "))
            arb_to_roman(num)
            print(arb_to_roman(num))
        elif choice == 2:
            roman_to_arb()
        elif choice == 3:
            break
    except ValueError:
        continue
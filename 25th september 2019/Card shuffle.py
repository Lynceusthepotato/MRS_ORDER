from random import shuffle
def card():
    shape = ["heart","spade","diamond","club"]
    number = ["1","2","3","4","5","6","7","8","9","10"]
    lst = []
    for shapes in shape:
        for numbers in number:
            lst.append(f'{numbers} of {shapes}')
    print(lst)
    print("I going to shuffle the card now")
    shuffle(lst)
    print(lst[:int(input("How many card do you want? : "))])

card()
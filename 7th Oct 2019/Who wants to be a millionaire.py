import random #IM only doing 5 numbers
player_name = input("Enter your name : ")
que = 1
lifeline5050 = 0
lifeline_audience = 0
money = ['$32000','$64000','$125000','$250000','$500000','$1000000']
QL = list(open('QNA.txt'))
while que <= 5:
    f = QL.pop(0)
    line = f.split('>')
    question = line[0]
    answer = line[1].strip('\n').split(',')
    l5050a = line[2].strip('\n').split(',')
    random_answer = random.choice(answer)
    print(que,".",question)

    a = random.choice(answer)
    answer.remove(a)
    b = random.choice(answer)
    answer.remove(b)
    c = random.choice(answer)
    answer.remove(c)
    d = random.choice(answer)
    print('A.',a,'\nB.',b,'\nC.',c,'\nD.',d)
    answerdict = {a:'A',b:'B',c:'C',d:'D'}
    print("If you want to access lifeline, [1] is for 50:50 [2] is for audience")
    select = input("Whats your answer? ")
    select = select.capitalize()
    #Start of number 1
    if que == 1:
            if select == "Pikachu":
                print("correct, you pass the ",money[que],"question")
            elif select == answerdict["Pikachu"]:
                print("correct, you pass the ", money[que], "question")
            elif select == "1":
                if lifeline5050 == 0:
                    print("You are left with the answer",l5050a[0],'and',l5050a[1])
                    l50 = input("Your answer ")
                    select = l50.capitalize()
                    if select == "Pikachu":
                        print("correct, you pass the ",money[que],"question")
                    lifeline5050 = 1
                elif lifeline5050 != 0:
                    print("You already use lifeline 50:50")
            elif select == "2": #Going to skip the audience first
                if lifeline_audience == 0:
                    print()
            else:
                print("ooof, better luck next time")
                break
    if que == 2:
            if select == "Bruce":
                print("correct, you pass the ",money[que],"question")
            elif select == answerdict["Bruce"]:
                print("correct, you pass the ",money[que],"question")
            elif select == "1":
                if lifeline5050 == 0:
                    print("You are left with the answer",l5050a[0],'and',l5050a[1])
                    l50 = input("Your answer ")
                    select = l50.capitalize()
                    if select == "Bruce":
                        print("correct, you pass the ",money[que],"question")
                    lifeline5050 = 1
                elif lifeline5050 != 0:
                    print("You already use lifeline 50:50")
            else:
                print("ooof, better luck next time")
                break
    if que == 3:
            if select == "Felix":
                print("correct, you pass the ",money[que],"question")
            elif select == answerdict["Felix"]:
                print("correct, you pass the ",money[que],"question")
            elif select == "1":
                if lifeline5050 == 0:
                    print("You are left with the answer",l5050a[0],'and',l5050a[1])
                    l50 = input("Your answer ")
                    select = l50.capitalize()
                    if select == "Felix":
                        print("correct, you pass the ",money[que],"question")
                    lifeline5050 = 1
                elif lifeline5050 != 0:
                    print("You already use lifeline 50:50")
            else:
                print("ooof, better luck next time")
                break
    if que == 4:
            if select == "Peter":
                print("correct, you pass the ",money[que],"question")
            elif select == answerdict["Peter"]:
                print("correct, you pass the ",money[que],"question")
            elif select == "1":
                if lifeline5050 == 0:
                    print("You are left with the answer",l5050a[0],'and',l5050a[1])
                    l50 = input("Your answer ")
                    select = l50.capitalize()
                    if select == "Peter":
                        print("correct, you pass the ",money[que],"question")
                    lifeline5050 = 1
                elif lifeline5050 != 0:
                    print("You already use lifeline 50:50")
            else:
                print("ooof, better luck next time")
                break
    if que == 5:
            if select == "Sean":
                print("correct, you Answer the ",money[que],"question")
            elif select == answerdict["Sean"]:
                print("correct, you Answer the ",money[que],"question")
            elif select == "1":
                if lifeline5050 == 0:
                    print("You are left with the answer",l5050a[0],'and',l5050a[1])
                    l50 = input("Your answer ")
                    select = l50.capitalize()
                    if select == "Sean":
                        print("correct, you pass the ",money[que],"question")
                    lifeline5050 = 1
                elif lifeline5050 != 0:
                    print("You already use lifeline 50:50")
            else:
                print("ooof, better luck next time")
                break
    que += 1
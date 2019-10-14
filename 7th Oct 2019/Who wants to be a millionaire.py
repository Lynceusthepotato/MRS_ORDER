import random #IM only doing 5 numbers
player_name = input("Enter your name : ")
que = 1
lifeline5050 = 0
lifeline_audience = 0
money = ['$32000','$64000','$125000','$250000','$500000','$1000000']
psg = ['20','10','30','40']
QL = list(open('QNA.txt'))
while que <= 5:
    f = QL.pop(0)
    line = f.split('>')
    question = line[0]
    answer = line[1].strip('\n').split(',')
    l5050a = line[2].strip('\n').split(',')
    random_answer = random.choice(answer)
    psg.sort()
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
                    print(answerdict["Pikachu"],"Pikachu",psg[3],"%")
                    psg.remove(psg[3])
                    print(answerdict["Regigigas"],"Regigigas",random.choice(psg),"%")
                    print(answerdict["Swiblu"],"Swiblu",random.choice(psg),"%")
                    print(answerdict["Swampert"],"Swampert",random.choice(psg),"%")
                    laud = input("answer")
                    select = laud.capitalize()
                    if select == answerdict["Pikachu"]:
                        print("correct, you pass the ",money[que],"question")
                    lifeline_audience = 1
                elif lifeline_audience != 0:
                    print("You already use lifeline audience")
                else:
                    print("ooof, better luck next time")
                    break

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
            elif select == "2": #Going to skip the audience first
                if lifeline_audience == 0:
                    print(answerdict["Bruce"],"Bruce",psg[3],"%")
                    psg.remove(psg[3])
                    print(answerdict["Damian"],"Damian",random.choice(psg),"%")
                    print(answerdict["Alfred"],"Alfred",random.choice(psg),"%")
                    print(answerdict["Peter"],"Peter",random.choice(psg),"%")
                    laud = input("answer")
                    select = laud.capitalize()
                    if select == answerdict["Bruce"]:
                        print("correct, you pass the ",money[que],"question")
                    lifeline_audience = 1
                elif lifeline_audience != 0:
                    print("You already use lifeline audience")
                else:
                    print("ooof, better luck next time")
                    break
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
            elif select == "2": #Going to skip the audience first
                if lifeline_audience == 0:
                    print(answerdict["Felix"],"Felix",psg[3],"%")
                    psg.remove(psg[3])
                    print(answerdict["Bob"],"Bob",random.choice(psg),"%")
                    print(answerdict["Mark"],"Mark",random.choice(psg),"%")
                    print(answerdict["Jack"],"Jack",random.choice(psg),"%")
                    laud = input("answer")
                    select = laud.capitalize()
                    if select == answerdict["Felix"]:
                        print("correct, you pass the ",money[que],"question")
                    lifeline_audience = 1
                elif lifeline_audience != 0:
                    print("You already use lifeline audience")
                else:
                    print("ooof, better luck next time")
                    break
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
            elif select == "2": #Going to skip the audience first
                if lifeline_audience == 0:
                    print(answerdict["Peter"],"Peter",psg[3],"%")
                    psg.remove(psg[3])
                    print(answerdict["John"],"John",random.choice(psg),"%")
                    print(answerdict["Simon"],"Simon",random.choice(psg),"%")
                    print(answerdict["Sean"],"Sean",random.choice(psg),"%")
                    laud = input("answer")
                    select = laud.capitalize()
                    if select == answerdict["Peter"]:
                        print("correct, you pass the ",money[que],"question")
                    lifeline_audience = 1
                elif lifeline_audience != 0:
                    print("You already use lifeline audience")
                else:
                    print("ooof, better luck next time")
                    break
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
            elif select == "2": #Going to skip the audience first
                if lifeline_audience == 0:
                    print(answerdict["Sean"],"Sean",psg[3],"%")
                    psg.remove(psg[3])
                    print(answerdict["blipblop"],"blipblop",random.choice(psg),"%")
                    print(answerdict["Mark"],"Mark",random.choice(psg),"%")
                    print(answerdict["Bob"],"Bob",random.choice(psg),"%")
                    laud = input("answer")
                    select = laud.capitalize()
                    if select == answerdict["Sean"]:
                        print("correct, you pass the ",money[que],"question")
                    lifeline_audience = 1
                elif lifeline_audience != 0:
                    print("You already use lifeline audience")
                else:
                    print("ooof, better luck next time")
                    break
            else:
                print("ooof, better luck next time")
                break
    que += 1
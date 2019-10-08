import json

filename = "tweet.json"
PC = []
with open(filename) as f:
    txt = json.load(f)
    PC = txt["statuses"]

def findid(chat):
    for i in PC:
        if i["id_str"] == chat:
            return i
        elif i not in PC:
            print("There is no id")

def savethread(thread):
    PC.append(thread)

def savefile():
    with open(filename,"w") as f:
        json.dump({"text": PC}, f)

id = input("Enter an id: ") # put in id_str
userchoice = findid(id)
if userchoice is not None:
    print(userchoice)
else:
    username = input("Enter a new username: ")
    opinion = input("Enter an opinion: ")
    newusername = {"name": username}
    newopinion = {"text": opinion}
    savethread(newusername)
    savethread(newopinion)
    print(PC)
    savefile()

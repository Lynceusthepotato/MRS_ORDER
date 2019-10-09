import json

filename = "tweet.json"
PC = []
with open(filename) as f:
    txt = json.load(f)
    PC = txt["statuses"]
def loadtweet(YN):
    if YN == "Y":
        for i in range(0,3):
            print(PC[i]["text"])

def findid(chat):
    for i in PC:
        if i["id_str"] == chat:
            return i
        elif i not in PC:
            print("There is no id")

'''def findtext(chat): #Doesnt work 
    for i in range(0,len(PC)):
        if PC[i]["text"] == chat:
            return i
        elif i not in PC:
            print("There is no thread")'''

def savethread(thread):
    PC.append(thread)

def savefile():
    with open(filename,"w") as f:
        json.dump({"text": PC}, f)


tweet = input("Do you want to load tweet [Y/N]: ")
loadtweet(tweet.capitalize())
id = input("Enter a id: ")# enter id_str
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

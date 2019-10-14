import matplotlib.pyplot as plt

with open("im closing my eyes.txt") as something:
    txt = something.read()
listz = txt.split()
result = dict()

for x in listz:
    if x in result:
        result[x] += 1
    else:
        result[x] = 1

count = result.values()
indentation = list(range(1, len(count) + 1))

b1 = plt.barh(indentation, sorted(count),edgecolor = "black",linewidth = 0.5,color = "turquoise")
plt.yticks(indentation,listz)
plt.xticks(range(0,25,5))
plt.title("Im closing my eyes lyric")
plt.ylabel("Words")
plt.xlabel("How many words on the song")
plt.show()

character = input("Put something in for the ascii thingy: ")
ll = []
bb = []
for c in character:
    ll.append(c)
    bb.append(ord(c))
print(ll)
print(bb)
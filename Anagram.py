def anagrams(som1,som2):
    list1 = list(som2)

    test1 = 0
    condition = True

    while test1 < len(som1) and condition:
        test2 = 0
        found = False
        while test2 < len(list1) and not found:
            if som1[test1] == list1[test2]:
                found = True
            else:
                test2 = test2 + 1

        if found:
            list1[test2] = None
        else:
            condition = False

        test1 = test2 + 1

    return condition

print(anagrams('pewdiepie','wepiedipe'))
def quickFindUF(n):
    idList = []
    for i in range(n):
        idList.append(i)
    return idList

def connected(p, q) -> "me kqyr a jon connected tek QuickFind":
    global idList
    return idList[p] == idList[q]

def union(u1,u2) -> "mi lidh tek QuickFind":
    global idList
    uid1 = idList[u1]
    uid2 = idList[u2]
    for i in range(len(idList)):
        if idList[i] == uid1:
            idList[i] = uid2

def unionQU(id1,id2) -> "unioni i QuickUnion":
    global idList
    i = root(id1)
    j = root(id2)
    idList[i] = j

def root(number) -> "me gjet rrenjen e Trees":
    global idList
    while number != idList[number]:
        number = idList[number]
        print(number, idList[number])
    return number

idList = quickFindUF(10000000)
union(2,3)
union(4,3)
union(1,9)
union(3,20)
print(connected(4,20))
union(9,0)
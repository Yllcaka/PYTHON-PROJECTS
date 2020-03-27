def quickFindUF(n):
    idList = []
    for i in range(n):
        idList.append(i)
    return idList
def connected(p, q) -> "me kqyr a jon connected tek QuickFind":
    global idList
    return root(p) == root(q)
def unionQU(id1,id2) -> "unioni i QuickUnion":
    global idList
    i = root(id1)
    j = root(id2)
    idList[i] = j

def root(number) -> "me gjet rrenjen e Trees":
    a = 0
    global idList
    while number != idList[number]:
        number = idList[number]
        print(number, idList[number],a)
        a+=1
    return number

idList = quickFindUF(10)
unionQU(2,1)
unionQU(4,2)
unionQU(7,2)
unionQU(9,3)
unionQU(5,8)
unionQU(6,8)
unionQU(0,5)
print(idList)
print(connected(1,7))
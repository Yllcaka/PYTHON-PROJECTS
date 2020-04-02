import copy as cp
def quickFindUF(n):
    return [i for i in range(n)]


def connected(p , q) -> "me kqyr a jon connected tek QuickFind":
    return root(p) == root(q)


def root(number) -> "me gjet rrenjen e Trees":
    a = 0
    global idList
    while number != idList[number]:
        print(a)
        # print(number , idList[number] , idList[idList[number]])
        idList[number] = idList[idList[number]]#Path comprehension
        number = idList[number]
        print(number , idList[number] )
        # print(number, idList[number],a)
        a+=1
    return number


def union(id1, id2) -> "unioni i QuickUnion":
    global idList,sz
    i = root(id1)
    j = root(id2)
    if i == j:
        return
    if sz[i] < sz[j]:
        idList[i] = j
        sz[j] += sz[i]
    else:
        idList[j] = i
        sz[i] += sz[j]


# print(quickFindUF(1000))
idList = quickFindUF(1000)
sz = cp.deepcopy(idList)
union(2,1)
union(4,2)
union(7,2)
union(9,3)
union(5,8)
union(6,8)
union(0,5)
union(3,100)
union(4,500)
print(connected(1,7))
union(99,23)
union(9,3)
union(3,83)
union(83,8)
union(8,5)
# print(idList,sz)
#kqyre qita edhe niher ma mir e ki
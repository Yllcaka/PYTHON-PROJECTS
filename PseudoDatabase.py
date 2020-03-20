import shutil
import shelve
database = open("hello.txt", mode="w+")
# print(database.read())
print(database.read())
for i in range(10):
    database.write(f"iteration number: {i}\n")
database.close()
count = 0
with open("add.txt","r") as add:
    for i in add:
        count +=1
    print(f"total number of counts is {count}")
database = open("add.txt","a+")
ranging = int(input("How many iterations do you wanna add??? "))
for i in range(ranging):
    database.write(f"Iteration number: {count + i}\n")
database.close()
shelf = shelve.open("ShelveData")
shelf["shokt"] = ["Dardi","Verona","Kastro","Dimi"]
print(shelf["shokt"])
shelf.close()
# shutil.copy("hello.txt","/home/ylli/Desktop/reincarnation.txt")
# shutil.copytree("../PYTHON","/home/ylli/Desktop/PythonCopy")
# shutil.move("add.txt","/home/ylli/Desktop/add.txt")
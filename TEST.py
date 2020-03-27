import time
def middle(list,target:'Number to be found') ->"Binary search using recursion" :
    mid = len(list)//2
    list.sort()
    if list == [] or (len(list)<2 and list[0] !=target):
        return f"{target} is not in the list"
    if list[mid] == target:
        return f"{target} is in the list"
    elif list[mid] < target:
        return middle(list[mid:],target)
    elif list[mid] > target:
        return middle(list[:mid],target)
try:
    list = input("Enter list seperate elements by ',': ")
    number = int(input("Enter a number"))
    list = list.split(",")
    list = [int(''.join(element.split(" "))) for element in list]
    starttime = time.time()
    print(middle(list , number))
    endtime = time.time()
    print(f"The time is {endtime-starttime}")
except Exception as e:
    print("The program couldn't execute because of:",e)
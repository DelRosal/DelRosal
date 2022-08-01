import time

###THE LIST MUST BE SORTED###

def binary_search(num,key):

    start=time.perf_counter()
    left=0
    right=len(num)-1

    while left<= right:
        middle=(left+right)//2

        if num[middle]==key:
            finish=time.perf_counter()
            total=finish-start
            return print("{} is in position {} and it took {:0.10f} seconds".format(key,middle,total))
        
        elif num[middle]>key:
            right=middle-1

        elif num[middle]<=key:
            left=middle+1
    return print("{} is not on the list".format(key))



def linear_search(num,key):

    start=time.perf_counter()

    for i, item in enumerate (num):
        
        if key==item:
            finish=time.perf_counter()
            total=finish-start
            return print("{} is in position {} and it took {:0.10f} seconds".format(key,i,total)) 
    
    return print("{} is not on the list".format(key))


#Main code 
num=[*range(0,80000,2)]
key=int(input("Numero:"))


print("-Linear Search-")
linear_search(num,key)
print('\n-BinarySearch-')
binary_search(num,key)


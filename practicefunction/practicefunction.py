#let's practice using a function:
#Q1: write to print the length of a list (list is the parameter):
num=[1,2,3,45,54,57,34,89]
cities=["islamabad","karachi","lahore","hyderabad","multan","sawat"]
def cal_list(list):
    print("length of list:",len(list))
cal_list(num)
cal_list(cities)

#Q2: write to the print the element of list in a singal line. (list is the parameter)
cities=["islamabad","karachi","lahore","hyderabad","multan","sawat"]
def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(cities)

#Q3: write to find the factorial of n.( n is the parameter)

def find_factorial(n):
     fact=1
     for i in range(1,n+1):
        fact=fact*i
     print("\nfactorial is:",fact)
find_factorial(6)

#Q4: write to convert USD to PAKR:

def converter(USD):
    pakr=USD*279.79
    print(USD,"USD=",pakr,"PAKR")

converter(2)

#Q5: write to find EVEN and ODD. (n parameter):

def find_out(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")

find_out(178)

#Fibonacci Series with Recursion

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fibonacci(i), end=", " )


#Matrix

m=[]
r=int(input("Enter Number of Rows: "))
c=int(input("Enter Number of Columns: "))
for i in range(0,r):
    a=[]
    for j in range(0,c):
        a.append((input()))
    m.append(a)
print("Matrix: ")
for i in range(0,r):
    for j in range(0,c):
        print(m[i][j],end=" ")
    print()


#Transpose Matrix

m=[]
r=int(input("Enter Number of Rows: "))
c=int(input("Enter Number of Columns: "))
for i in range(0,r):
    a=[]
    for j in range(0,c):
        a.append((input()))
    m.append(a)
print("Matrix: ")
for i in range(0,r):
    for j in range(0,c):
        print(m[i][j],end=" ")
    print()
print("Transpose Matrix: ")
for i in range(0,r):
    for j in range(0,c):
        print(m[j][i],end=" ")
    print()


# To print positive index place value from string
a=input()
for i in range(0,len(a)):
    if i%2==0:
        print(a[i],end="")

#Take a string  from user and  write a function to return even index characters in form of another string.
def even_ind(str1):
    s=list()
    for i in range(0,len(str1)):
        if i%2==0:
            s.append(str1[i])
    
    for x in s:
        print(x,end="")
    return ""

str2=input()
print(even_ind(str2))

#Take a list of integers from user and print the list of sqaures the integers
def squares(x):
    list2=list()
    for x in list1:
        list2.append(x**2)
    print(list2)
list1=list(map(int,input().split(",")))
squares(list1)

#Take a list and print double for max 2 elements in it
arr=list(map(int,input().split()))
arr.sort()
print(arr)
print((arr[-1]*arr[-2])**2)
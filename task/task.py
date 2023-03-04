for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            if (j%2==0):
              print("0",end=" ")
            else:
              print("1",end=" ")
        else:
            print(" ",end=" ")
    print()
print("-------------------------------------------")
a = int(input("Enter number: "))

for i in range(a, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    
    print(" ")
print("---------------------------------------------")

a = int(input("Enter number: "))

for k in range(a, 1, -1):
    for space in range(0, a-k):
        print("  ", end=" ")
    for l in range(i, 2*k-1):
        print("* ", end="")
    for l in range(1, k-1):
        print("* ", end=" ")
    print("")
print("---------------------------------------------")
a = int(input("Enter number: "))  
k = 2 * a - 2  
for i in range(0, a):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 1  
    for j in range(0, i + 1):  
        print("* ", end="")  
    print(" ")   
k = a - 2  
for i in range(a, -1, -1):  
    for j in range(k, 0, -1):  
        print(end=" ")  
    k = k + 1  
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")  
print("---------------------------------------------")
a = int(input("Enter number: "))  
for i in range(0, a):  
    for j in range(0, i + 1):  
        print("*", end=' ')  
    print(" ")  
for i in range(a + 1, 0, -1):  
    for j in range(0, i - 1):  
      print("*", end=" ")  
    print(" ")
print("---------------------------------------------")    
a = int(input("Enter number: "))
n = 1
for i in range(1, a+1):
    for j in range(1, i+1):
        print(n, end=" ")
        n += 1
    print()
print("---------------------------------------------")
n = int(input("Enter number:"))
for i in range(n):
    for j in range(i+1):
        print(chr(j + 65), end=" ")
    print(" ")
print("---------------------------------------------")
n = int(input("Enter number:"))
k=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()

rows = int(input())
for i in range(1,rows+1):
    print(" " * ((rows-i)), end = " ")
    print("*" * i )
for j in range(i,rows+i):
    print(" " * ((rows-i)-1), end = " ")
    print("*" * i)

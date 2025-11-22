# Nhập số n (number)
n = int( input("Mời nhập số n: ") )

#In dãy số [1, 2, 3,...n]
# i (index)
for i in range(1,n+1):
    if i%2==0:
        print(i, end=" ")
print("")
for i in range(2,n+1,2):
    print(i, end=" ")
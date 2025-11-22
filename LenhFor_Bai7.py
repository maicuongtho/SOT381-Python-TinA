# Nhập số n (number)
n = int( input("Mời nhập số n: ") )

#
print(f"Các số từ 1 đến {n} chia hết cho 3 và 5 là")
for i in range(1,n+1):
    if (i%3==0) and (i%5==0):
        print(i,end=" ")
        

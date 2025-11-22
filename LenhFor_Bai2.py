# Nhập số n (number)
n = int( input("Mời nhập số n: ") )

#In dãy số [1, 2, 3,...n]
# i (index)
#for i in range(1,n+1):
#    print(i, end=" ")
    
#Tính tổng
tong=0

for i in range(1,n+1):
     tong=tong+i
# In kết quả tính được

print(f"\nTổng các số từ 1 đến {n} là {tong}")

 



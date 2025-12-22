# nhập số lượng phần tử của ds: n
n =  int(   input("Nhập số lượng phần tử: ")  )
# nhập danh sách các phần tử từ bàn phím
a=[]   # khai báo 1 danh sách rỗng
for i in range(n):
    tam =  int( input(f"a[{i}]=")  )
    a.append(tam)
    
print("Danh sách vừa nhập là:")
print(a)

# Đếm số lượng Chẵn, Lẻ
sl_chan=0
sl_le=0

for so in a:
    if so%2==0:
        sl_chan +=1
    else:
        sl_le +=1
#print(f"Số lượng số chẵn là {sl_chan}")
print("Số lượng số chẵn là: ")
print(sl_chan)

print(f"Số lượng số lẻ là {sl_le}")

 




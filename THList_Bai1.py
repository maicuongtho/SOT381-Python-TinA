# Nhập danh sách n số nguyên từ bàn phím
# - In lại danh sách vừa nhập
# - Tính tổng các phần tử

# nhập số lượng phần tử của ds: n
n =  int(   input("Nhập số lượng phần tử: ")  )
# nhập danh sách các phần tử từ bàn phím
a=[]   # khai báo 1 danh sách rỗng

for i in range(n):
    tam =  int( input(f"a[{i}]=")  )
    a.append(tam)
    
print("Danh sách vừa nhập là:")
print(a)


#--- Tính tổng all phần tử trong ds
tong_all = sum(a)
print(f"Tổng các pt trong ds a là {tong_all}")





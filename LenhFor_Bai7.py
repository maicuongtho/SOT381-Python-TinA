# Nhập số n (number)
n = int( input("Mời nhập số n: ") )

# Đếm
sl_chan=0
sl_le=0
for i in range(1,n+1):
    if i%2==0:
        sl_chan = sl_chan + 1
        
    if i%2!=0:
        sl_le = sl_le + 1
# Xuất kết quả

print(f"Số lượng số chẵn là {sl_chan}")
print(f"Số lượng số lẻ là {sl_le}")

# Tính tổng các số chẵn từ 1 đén n
tong_chan=0
for i in range(1,n+1):
    if i%2==0:
        tong_chan = tong_chan + i
        # tong_chan +=i

# Tính tổng các số lẻ từ 1 đén n
tong_le=0
for i in range(1,n+1):
    if i%2!=0:
        tong_le+=i
print(f"Tổng các số chẵn = {tong_chan}")        
print(f"Tổng các số lẻ = {tong_le}")



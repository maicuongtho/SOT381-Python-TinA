n = int( input("Nhập một số nguyên dương ") )
# Số chẵn là số chia hết cho 2, nghĩa là chia 2 , có dư =0

#Tính phần dư
du = n % 2


# Kiểm tra
if du==0:
    print(f"Số {n} là số chẵn")
else:
    print(f"Số {n} là số lẻ")

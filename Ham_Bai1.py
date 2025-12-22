def giaithua(n):
    #Tính giai thừa ở đây
    # kết quả,cất tạm vào biến kq
    kq=1
    for i in range(1,n+1):
        kq=kq*i
    return kq
print(giaithua(6))
    
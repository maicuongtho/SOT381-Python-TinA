# Dem so phan tu nguyen to trong 1 day so
def laNguyenTo(n):
    kq=True
    if (n==1) or (n==2):
        kq=True	# n là số NT
    else:
        for i in range(2,n):
            if n%i==0:
                kq=False
                break
    return kq
#---------------
ds = [ 1, 5, 22, 10, 7, 2, 9, 91]

#dem so luong so nguyen to
dem=0
for i in ds:
    if laNguyenTo(i):
        dem=dem+1
print(f"So luon so nguyen to la: {dem}")    
        
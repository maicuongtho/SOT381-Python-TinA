# Chương trình nhập vào 1 số nguyên từ bàn phím
# cho biết số đó là số âm, dương, hay số 0
so = int( input("Nhập một số nguyên ") )   
if so>0:
    print("Số dương")
elif so<0:
    print("Số âm")
else:
    print("Số không");
    

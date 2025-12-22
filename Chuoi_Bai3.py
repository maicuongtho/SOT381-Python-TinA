s = "Mai Cường Thọ"
sl_Hoa = 0

print("Debug từng bước:")
for i in range(len(s)):
    if s[i].isupper():  
        sl_Hoa +=1    
print(f"\nKết quả sai: {sl_Hoa}")
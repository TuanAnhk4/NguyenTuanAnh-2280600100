# tim cac so chia het cho 7 va ko la boi cua 5 nam trong khoang (2000-3200). in ra 1 dong ngan cach dau phay

j=[]

for i in range(2000, 3201):
    if(i%7==0) and (i%5 !=0):
        j.append(str(i))
print(','.join(j))

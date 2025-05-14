def ktra_songuyento(n):
    if n<= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input('nhap so can ktra: '))
if ktra_songuyento(number):
    print(number, 'la so nguyento')
else:
    print(number, "ko la snt")
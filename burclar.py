a = int(input("Kaçıncı ayda doğduğunuzu giriniz : "))
b = int(input("Doğduğunuz günü giriniz : "))
if a == 12 and b >= 22 :
    print('Burcunuz oğlak ')
elif a == 1 and b <= 19 :
    print('Burcunuz oğlak ')
elif a == 1 and b>=20 :
    print('Burcunuz kova ')
elif a == 2 and b <= 18 :
    print('Burcunuz kova ')
elif a == 2 and b >=19 :
    print('Burcunuz balık ')
elif a == 3 and b <=20 :
    print('Burcunuz balık ')
elif a == 3 and b >=21 :
    print('Burcunuz koç ')
elif a == 4 and b <= 19 :
    print('Burcunuz koç ')
elif a == 4 and b >= 20 :
    print('Burcunuz boğa ')
elif a == 5 and b <=20 :
    print('Burcunuz boğa ')
elif a == 5 and b >=21 :
    print('Burcunuz ikizler ')
elif a == 6 and b <=20 :
    print('Burcunuz ikizler ')
elif a == 6 and b >= 21 :
    print('Burcunuz yengeç ')
elif a == 7 and b <=22 :
    print('Burcunuz yengeç ')
if a == 7 and b >=23 :
    print('Burcunuz aslan ')
elif a == 8 and b <=22 :
    print('Burcunuz aslan ')
if a == 8 and b >=23 :
    print('Burcunuz başak ')
elif a == 9 and b <= 22 :
    print('Burcunuz başak ')
elif a == 9 and b >= 23 :
    print('Burcunuz terazi ')
elif a == 10 and b <= 22 :
    print('Burcunuz terazi')
elif a == 10 and b >=23 :
    print('Burcunuz akrep ')
elif a == 11 and b <= 21 :
    print('Burcunuz akrep ')
elif a == 11 and b >= 22 :
    print('Burcunuz yay')
elif a == 12 and b <= 21 :
    print('Burcunuz yay')
else:
    print('Eğer burcunuz çıkmıyorsa hatalı bir tarih girdiniz.Lütfen kontrol ediniz')

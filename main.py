import random
from plyer import notification
import time
a = random.randint(0,20)
b = random.randint(0,20)
result= 0
x = random.randint(0,4)


#1 toplama 2 çıkarma 3 çarpma 4 bölme işemi olucak

if x == 1 :
    result= a+b
    print(f"{a}+{b} :")
elif x == 2 :
    result = a-b
    print(f"{a}-{b}:")
elif x == 3 :
    result = a * b
    print(f"{a}*{b}:")
elif x == 4 :
    result = a/b
    print(f"{a}/{b}:")

userinput=int(input("İşlemnin sonucunu giriniz:"))

if userinput == result:
    notification.notify(title="Doğru!", message="Tebrikler doğru bildiniz!", app_icon=None, timeout=10)
else :
    notification.notify(title="Hatalı!", message="Yanlış işlem yaptınız lütfen tekrar deneyin!", app_icon=None, timeout=10)











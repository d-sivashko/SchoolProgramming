a = int(input("Введите двузначное число: "))
if a%10 > a/10:
    print("Число едениц больше чем число десятков на", a%10-a//10)
else:
    print("Число десятков больше чем число едениц на", a//10-a%10)

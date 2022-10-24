def toBase(num,base):
    num = int(num)
    base = int(base)
    ans = ""
    while num>0:
        ans += str(num%base)
        num //= base
    return ans[::-1]
cond = True
while cond is True:
    number = (input('Введите число '))
    if number.isnumeric():
        cond = False
    else:
        print('Такое нельзя!')
while cond is False:
    base = input('В какую систему счисления переводим? ')
    if base.isnumeric():
        cond = True
    else:
        print('В такую нельзя!')
print(toBase(number,base))
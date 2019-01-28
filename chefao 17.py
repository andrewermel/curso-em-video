import math
co=float(input('diga o comprimento do cateto oposto:'))
ca=float(input('diga o comprimento do cateto adjacente:'))
hi=math.hypot(co,ca)
print('o valor da hipotenusa é {:.2f}'.format(hi))

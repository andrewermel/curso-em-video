import math
an=float(input('digite o angulo que voce deseja'))
s=math.sin(math.radians(an))
print('o angulo {} tem como seno {:.2f}'.format(an,s))
c=math.cos(math.radians(an))
print('o angulo {} tem como coseno {:.2f}'.format(an,c))
t=math.tan(math.radians(an))
print('o angulo {} tem como tangente {:.2f}'.format(an,t))

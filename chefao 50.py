# desenvolva um programa que leia seis
# numeros inteiros e mostre a soma
# apenas daqueles que forem pares.
# se o valor digitado for impar,
# desconsidere.

# exercicio
soma = 0
cont = 0
for c in range(1,7):
    n=int(input('diga um numero:'))
    if n % 2==0:
       soma +=n
       cont +=1

print('voce informou {} e a soma dos PARES numeros é {}'.format(cont,soma))




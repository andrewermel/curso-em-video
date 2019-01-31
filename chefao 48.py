# Faça um programa que calcule a soma
# entre todos os numeros impares que são multiplos de tres e que se encontram
# no intervalo de 1 até 500

# exercicio

soma = 0
cont = 0

for c in range(1,501,2):
    if c % 3 == 0:
        cont = cont +1
        soma += c

print('a soma de todos os {} valores solicitados é {}'.format(cont,soma))

# faça um programa que leia o sexo de uma pessoa , mas so aceite o valor M ou F
# caso esteja errado , peça a digitação novamente até ter um valor correto

# exercicio

sexo = str(input('informe seu sexo : [M/F]')).strip().upper()[0]
while sexo not in 'M F' :
    sexo = str(input('dados incorretos. por favor digite novamente:')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))





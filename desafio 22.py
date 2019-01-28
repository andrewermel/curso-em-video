nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome ...')
print('Seu nome em letras maiusculas é {}'.format(nome.upper()))
print('Seu nome em letras minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa= nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0],len(separa[0])))









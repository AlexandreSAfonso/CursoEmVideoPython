print('======= Desafio 04 =========')
n = input('Digite Algo: ')
print('O tipo primitivo é {}'.format(type(n)))
print('Só tem espaço  {}'.format(n.isspace()))
print('O valor é numérico  {}'.format(n.isnumeric()))
print('O valor é alfanumérico  {}'.format(n.isalnum()))
print('O valor é maiúsculo  {}'.format(n.isupper()))
print('O valor é minúsculo  {}'.format(n.islower()))
print('O valor é capitalizado  {}'.format(n.istitle()))
print('O valor é decimal {}'.format(n.isdecimal()))

if n.isalnum() == True:
    print(n.upper())
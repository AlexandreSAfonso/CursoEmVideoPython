print('======= Desafio 03 =========')
num1 = input('Digite um numero ')
num2 = input('Digite outro para soma ')
soma = float(num1) + float(num2)
print('A soma entre {} e {}, é {}'.format(num1, num2, soma))

print('======= Desafio 04 =========')
n = input('Digite Algo: ')
print(type(n))
if n.isalnum() == True:
    print(n.upper())
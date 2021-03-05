#Tipos Primitivos
    #var (cadeia de caractéres)
    #bool (True or False)
    #int (-1,0,1,1985)
    #float (4.5, 0.0076, 1.0)


print('======= Desafio 03 =========')
num1 = input('Digite um numero ')
num2 = input('Digite outro para soma ')
soma = float(num1) + float(num2)
print('o tipo da variavel num1 é',type(num1))
print('o tipo da variavel soma é',type(soma))
print('A soma dos dois números é: ', soma)
print('A soma entre', num1, 'vale', num2 ,'é: ', soma)

#modo correto de inserir variáveis no Python 3
print('A soma entre {} e {}, é {}'.format(num1, num2, soma))
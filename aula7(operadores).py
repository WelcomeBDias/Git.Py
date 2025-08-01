#Introdução aos operadores matematicos

adicao = 1 + 1
print('Adição' , adicao)

subtracao = 10-5
print('Subtração', subtracao)

multiplicacao = 2*2
print('Multiplicação', multiplicacao)

divisao = 10/3 #sempre retorna como dado float, mesmo sendo numeros inteiros
print('Divisão', divisao)

divisao_inteira = 10//3 #retorna os dados como inteiro, mas depende de qual
print('Divisão Inteira', divisao_inteira)

exponenciacao = 2**10 #numero elevado, nesse caso 2 elevado a 10
print('Exponenciação', exponenciacao)

modulo = 25 % 5 #resto da divisão
print('Modulo', modulo)


lolo = 16 % 8 #serve para saber se número é divisivel por outro

if lolo == 0:
    print('divisivel')
else:
    print('não é divisivel')

#ou

print(16 % 8 == 0)

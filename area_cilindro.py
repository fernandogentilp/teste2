import math
#Primeiro, irei pegar as variaveis da fórmula do cilindro, pedindo ao usuário para inserir-las
r = float(input('Insira neste campo o valor do raio: '))
h = float(input('Insira neste campo o valor da altura: '))
#Segundo, irei fazer o processamento dos dados já adquiridos, fazendo com que a fórmula do cilindro rode e produza o resultado esperado
a_lateral = 2 * r * h
a_bases = 2 * r ** 2
a_total = math.ceil((a_lateral + a_bases) * math.pi)
#Terceiro, irei fazer o comando de saída para mostrar o resultado no terminal
print(f'O valor da área total é: {a_total} centimetros ao quadrado!')


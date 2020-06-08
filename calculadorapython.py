##calculadora com python
import math
print("************CALCULADORA PYTHON************")
print("Digite o numero da operação desejada!")
print("1 - Soma")
print("2 - Subtrção")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potencia")
print("6 - Raiz quadrada")

operacao = float(input('Número da operação: '))

a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
resultado = 0

if operacao == 1:
	resultado = a + b
	print("o resultado da soma é: ",resultado)

elif operacao == 2:
	resultado = a - b
	print("o resultado da subtração é: ",resultado)

elif operacao == 3:
	resultado = a * b
	print("o resultado da multiplicação é: ",resultado)

elif operacao == 4:
	resultado = a / b
	print("o resultado da divisão é: ",resultado)

elif operacao == 5:
	resultado = a ** b
	print("o resultado da potencia é: ",resultado)

elif operacao == 6:
	resultado = math.sqrt(a)
	print("o resultado da potencia é: ",resultado)



else:
	print("Confira a operação desejada!")

def entrada():
	print ("Escolha a operação: ")
	return int(input ("1 - Soma \n2 - Subtração \n3 - Divisão \n4 - Multiplicação \n0 - Sair \n\n:"))

ops = ["Sair", "Soma", "Subtração", "Divisão", "Multiplicação"]

print ("Bem vindo a calculador mais simples do mundo.")
op = entrada()

while (op >= 1 and op <=4):
	print ("Opção escolhida: ", ops[op])
	
	if op == 1:	
		print("Expressão: valor 1 + valor 2")
		v1 = int(input("valo 1: "))
		v2 = int(input("valo 2: "))
		print("Resultadp: ", v1+v2, "\n\n")

	elif op == 2:
		print("Expressão: valor 1 - valor 2")
		v1 = int(input("valo 1: "))
		v2 = int(input("valo 2: "))
		print("Resultadp: ", v1-v2, "\n\n")

	elif op == 3:
		print("Expressão: valor 1 / valor 2")
		v1 = int(input("valo 1: "))
		v2 = int(input("valo 2: "))
		print("Resultadp: ", v1/v2, "\n\n")

	elif op == 4:
		print("Expressão: valor 1 x valor 2")
		v1 = int(input("valo 1: "))
		v2 = int(input("valo 2: "))
		print("Resultadp: ", v1*v2, "\n\n")

	op = entrada()	

else:
	print("já vai tarde")
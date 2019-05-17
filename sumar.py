def main():
	print(sumar(input("Escriba una lista de numeros: ").split(",")))

def sumar(numero):
	if numero!=[]:
		return int(numero[0]) + sumar(numero[1:])
	else:
		return 0

main()

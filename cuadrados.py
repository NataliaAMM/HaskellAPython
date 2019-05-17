def main():
	print(cuadrados(input("Escriba una lista de numeros separados por comas: ").split(",")))

def cuadrados(lista):
	if lista==[]:
		return []
	else:
		return [int(lista[0])*int(lista[0])]+cuadrados(lista[1:])

main()
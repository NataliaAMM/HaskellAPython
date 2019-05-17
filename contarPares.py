def main():
	print(contarPares(input("Escriba una lista de numeros separados por comas: ").split(",")))

def contarPares(lista):
	if lista!=[]:
		if int(lista[0])%2==0:
			return 1 + contarPares(lista[1:])
		else:
			return contarPares(lista[1:])
	else:
		return 0

main()
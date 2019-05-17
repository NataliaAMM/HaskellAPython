def main():
	print(invertir(input("Escriba una lista separada por comas: ").split(",")))

def invertir(lista):
	return lista[::-1]

main()
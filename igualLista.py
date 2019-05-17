def main():
	print(igualLista(input("Escriba una lista separada por comas: ").split(","), input("Escriba una lista separada por comas: ").split(",")))

def igualLista(uno, dos):
	if uno == dos:
		return True
	else:
		return False

main()
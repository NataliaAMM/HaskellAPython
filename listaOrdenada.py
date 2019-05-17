def main():
	print(listaOrdenada(input("Escriba una lista separados por comas: ").split(",")))

def listaOrdenada(lista):
	if lista==[]:
		return True
	elif len(lista)==1:
		return True
	elif lista[0]<=lista[1] and listaOrdenada(lista[1:]):
		return True
	else:
		return False

main()
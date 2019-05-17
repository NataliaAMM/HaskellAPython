def main():
	print(mostrarUbicacion(input("Escriba una lista separada por comas: ").split(","), int(input("Escriba la posicion: "))))

def mostrarUbicacion(lista, posicion):
	if(posicion<len(lista) and posicion>=0):
		return lista[posicion]
	else:
		return "La posicion no existe"

main()
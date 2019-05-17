def main():
	print(primos(int(input("Escriba el numero tope: "))))

def primos(tope):
	if tope>0:
		if esPrimo(tope):
			return primos(tope-1) + [tope]
		else:
			return primos(tope-1)
	else:
		return []

def esPrimo(dato):
	if len(divisibles(dato,dato))<=2:
		return True
	else:
		return False

def divisibles(dato,cuenta):
	if cuenta>0:
		if divisible(dato,cuenta):
			return divisibles(dato,cuenta-1) + [cuenta]
		else:
			return divisibles(dato,cuenta-1)
	else:
		return []

def divisible(dividendo, divisor):
	if dividendo%divisor==0:
		return True
	else:
		return False

main()
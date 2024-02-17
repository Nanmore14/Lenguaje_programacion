
def factorial(n):
    if n== 0:
        return 1
    else:
        return n * factorial(n - 1)
    
numero = int(input()) 5
resultado = factorial (numero)
print(f"el factorial de {numero} es: {resultado}")

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-2)
    
numero_terminos =10
print("serie de fibonacci:")
for i in range(numero_terminos):
    print(fibonacci(i))

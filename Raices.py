
#A continuación desarrollamos un programa que pida el ingreso de a, b y c de una función cuadrática (ax^2 + bx + c) 
# y cacule sus raíces reales.

import cmath # Importa la biblioteca cmath para manejar números complejos

# Definimos una función para calcular las raíces de la ecuación cuadrática
# utilizando la fórmula general: x = (-b ± √(b² - 4ac)) / (2a)

def calcular_raices(a, b, c): # Parametros: a, b, c son los coeficientes de la ecuación cuadrática

    discriminante = b**2 - 4*a*c # Calcula el discriminante (b^2 - 4ac)

    if discriminante < 0: # Si el discriminante es menor que 0, las raíces son complejas, la respuesta será un número complejo.
        print("Las raíces son complejas.")
    raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a) # Calcula la primera raíz
    raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a) # Calcula la segunda raíz   
    # Se utiliza cmath.sqrt para manejar números complejos si es necesario

    # Las raíces se calculan utilizando la biblioteca cmath
    # para manejar números complejos, lo que permite que el programa funcione incluso si las raíces son complejas.
    return raiz1, raiz2 # Devuelve las dos raíces calculadas

# Definimos la función principal que solicita al usuario los coeficientes y muestra las raíces
# Esta función se ejecuta cuando el script se corre directamente
def main():
    print("Ingrese los coeficientes de la función cuadrática (ax^2 + bx + c):")
    a = float(input("Ingrese coeficiente a: ")) # Solicita el coeficiente 'a'
    b = float(input("Ingrese coeficiente b: ")) # Solicita el coeficiente 'b'
    c = float(input("Ingrese coeficiente c: ")) # Solicita el coeficiente 'c'

    if a == 0: # Verifica si 'a' es cero, lo cual no es válido para una función cuadrática

        # Si 'a' es cero, imprime un mensaje de error y termina la ejecución
        print("El valor de 'a' no puede ser cero en una función cuadrática.")
        return

    raiz1, raiz2 = calcular_raices(a, b, c)    # Llama a la función para calcular las raíces y almacena los resultados en raiz1 y raiz2

    # Imprime las raíces calculadas
    print(f"Las raíces de la función cuadrática son: {raiz1} y {raiz2}")     

# Verifica si el script se está ejecutando directamente
# Si es así, llama a la función principal para iniciar el programa
if __name__ == "__main__":
    main()  
# El resultado se muestra en la consola.

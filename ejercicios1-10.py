# 2.1.	Crea un código que imprima en pantalla la expresión “Mi Primer Código En Python
print("Mi primer codigo en python")
# 2.2.	Crea un código que imprima en pantalla la siguiente expresión. A B C D E F G H I
letters = ["A", "B", "C", "D", "E","F","G","H","I"]
for i in range(0, len(letters), 3):
    print(" ".join(letters[i : i + 3]))
# 2.3.	Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta
careerAnswer = input("Que estas estudiando? :")
print(careerAnswer)
# 2.4.	Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta
countryAnswer = input("En que pais vives? :")
print(countryAnswer)
# 2.5.	Declara dos variables, llamadas nombre y edad.
nombre = "David Bowman"
pedad = 51
# 2.6.	Crea tres variables:
nombre = "Julia"
apellido = "Roberts"
nombrecompleto = nombre+" "+apellido
print(nombrecompleto)
# 2.7.	Declara la variable materia, asígnale el valor "Ingeniería del conocimiento", y muestra en pantalla la frase:
materia = "Ingenieria del conocimiento"
print("Estas estudiando "+ materia)
# 2.8.	Convierte el valor de num1 (num1=35) en un int e imprime el tipo de dato que resulta
num1= 35
print(type(num1))
# 2.9.	Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase
nombre_asociado = "Ambar"
numero_asociado = 116220
print(f"Estiado/a {nombre_asociado}, su numero de asociado es: {numero_asociado}")
# 2.10.	Muestra en pantalla el cociente (división al piso) de los siguientes dos números: 874 dividido entre 27.
print(874 // 27)
import uuid
#2.11.	Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.
print(round(10.676767))
# 2.12 Escribe una función que reciba una lista de productos (tuplas) y devuelva el producto más caro.
productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]
def obtener_producto_mas_caro(productos):
  producto_mas_caro = productos[0]

  for producto in productos:
    if producto[1] > producto_mas_caro[1]:
      producto_mas_caro = producto

  return producto_mas_caro[0]
print(obtener_producto_mas_caro(productos))
# 2.13.	Registro de estudiantes con diccionarios
estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

def obtener_promedio(matricula):
    if matricula not in estudiantes:
        print(f"No se encontró al estudiante con matrícula {matricula}.")
        return

    calificaciones_tomadas = estudiantes[matricula]["calificaciones"]
    total = 0
    cantidadMaterias = 0
    for nota in calificaciones_tomadas.values():
       total += nota
       cantidadMaterias += 1
    promedio = total/cantidadMaterias

    return print(f"El promedio del alumno {matricula} es de {promedio}")

matricula = int(input("Ingrese el numero de matricula: "))
obtener_promedio(matricula)

# 2.14.	Análisis de datos meteorológicos con arrays:
temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def devolver_datos (temperaturas):
    minimo = 100
    maximo = 0
    suma = 0
    cantidad = 0
    for valor in temperaturas:
      if(valor < minimo):
        minimo = valor

      if (valor > maximo):
        maximo = valor

      suma += valor
      cantidad += 1
      promedio = suma/cantidad

    print(f"El valor minimo es: {minimo}, el maximo es: {maximo}, y la media es de {promedio}")
 
devolver_datos(temperaturas)

#2.15.	Manejo de parámetros variables con *args:
def calcular_promedio(*args):
   suma= 0
   cantidad = 0
   for arg in args:
        suma += arg
        cantidad += 1

   print(f"El promedio del alumno es de {suma/cantidad}")
   
calcular_promedio(85, 90, 78, 92)
#2.16.	Creación de un perfil de usuario con **kwargs:

def crear_perfil(nombre, edad, email, **kwargs):
  perfil = {
      "id": str(uuid.uuid4())[:3], 
      "nombre": nombre,
      "edad": edad,
      "email": email,
      **kwargs,  
  }
  print(perfil)

crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza")
#2.17.	Administración de empleados con tuplas y diccionarios:
empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}
def salario_mas_alto (empleados):
 i=0
 mayor_salario = 0

 for i in empleados:
   if empleados[i][2]> mayor_salario:
      mayor_salario = empleados[i][2]
 print(f"El empleado con mayor salario es {empleados[i][0]}, con un salario de {mayor_salario}")

salario_mas_alto (empleados)
#2.18.	Procesamiento de ventas con arrays:
ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

def administrador_ventas(ventas):
    total = 0
    cantidad = 0
    for venta in ventas: 
        total += venta
        cantidad +=1
    print(f"El total de ventas es de ${total},y el promedio es de ${total/cantidad}")

administrador_ventas(ventas_diarias)

#2.19.	Análisis de resultados deportivos con diccionarios:
resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def calcular_goles(resultados):
    total_anotados = 0
    total_recibidos = 0
    for anotados, recibidos in resultados.values():
        total_anotados += anotados
        total_recibidos += recibidos
    print(f"El total es de {total_anotados} goles anotados , y {total_recibidos} goles recibidos")

calcular_goles(resultados)

#2.20.	Configuración de una aplicación con **kwargs:
def configurar_app(**kwargs):
  return kwargs

configuracion = configurar_app(
    modo_oscuro=True, idioma="es", notificaciones=False
)
print(configuracion)
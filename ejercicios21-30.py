# 2.21.	Ordenamiento de datos con tuplas:
puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

def ordenar_puntuaciones(lista):
    # Usamos una función lambda simple para indicar que se ordene por el segundo elemento (índice 1)
    # reverse=True es para que sea de mayor a menor
    lista.sort(key=lambda tupla: tupla[1], reverse=True)
    return lista

print(ordenar_puntuaciones(puntuaciones)) 
#2.22 Planificación de viajes con tuplas y diccionarios
paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

def calcular_paquetes(lista_paquetes):
    diccionario_destinos = {}
    for destino, precio, duracion in lista_paquetes:
        precio_total = precio * duracion
        diccionario_destinos[destino] = precio_total
    return diccionario_destinos

print(calcular_paquetes(paquetes))
#2.23 Gestión de inventario con arrays
inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

def actualizar_inventario(inv, vent):
    inventario_nuevo = []
    # Usamos len() para recorrer ambos arrays usando su posición (índice)
    for i in range(len(inv)):
        cantidad_restante = inv[i] - vent[i]
        inventario_nuevo.append(cantidad_restante)
    return inventario_nuevo

print(actualizar_inventario(inventario, ventas))

#2.24 Organización de eventos con *args
def organizar_eventos(*args):
    contador = 1
    for evento in args:
        print(f"{contador}. {evento}")
        contador += 1

organizar_eventos("Concierto", "Exposición de arte", "Conferencia")

#2.25 Análisis financiero con **kwargs
def analizar_finanzas(**kwargs):
    balance_total = 0
    for valor in kwargs.values():
        balance_total += valor
    return balance_total

balance = analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
print(f"El balance final es: {balance}")

#2.26 Registro de empleados con tuplas y **kwargs
def registro_empleado(nombre, edad, salario, **kwargs):
    empleado = {
        "nombre": nombre,
        "edad": edad,
        "salario": salario
    }
    for clave, valor in kwargs.items():
        empleado[clave] = valor
        
    return empleado

empleado_info = registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789")
print(empleado_info)

#2.27 Estadísticas de ventas con arrays
ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def estadisticas_ventas(ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    
    venta_maxima = 0
    mes_maximo = 0
    for i in range(len(ventas)):
        if ventas[i] > venta_maxima:
            venta_maxima = ventas[i]
            mes_maximo = i + 1 
            
    return {
        "total_ventas": total,
        "promedio_mensual": promedio,
        "mes_mayores_ventas": mes_maximo
    }

print(estadisticas_ventas(ventas_mensuales))

#2.28 Organización de una biblioteca con diccionarios
biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

def libros_despues_del_2000(biblio):
    libros_filtrados = []
    for titulo, detalles in biblio.items():
        if detalles["año"] > 2000:
            libros_filtrados.append(titulo)
    return libros_filtrados

print(libros_despues_del_2000(biblioteca))

#2.29 Registro de notas con tuplas y arrays
notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

def calcular_promedio_estudiantes(lista_notas):
    diccionario_promedios = {}
    for nombre, notas in lista_notas:
        promedio = sum(notas) / len(notas)
        diccionario_promedios[nombre] = promedio
    return diccionario_promedios

print(calcular_promedio_estudiantes(notas_estudiantes))

#2.30 Configuración de perfiles de usuario con **kwargs y arrays
usuarios = ["Ana", "Luis", "María"]

def configurar_perfiles(lista_usuarios, **kwargs):
    # Convertimos los argumentos empaquetados en una lista de tuplas para que sea un "array"
    configuraciones_array = list(kwargs.items())
    
    perfiles = {}
    for usuario in lista_usuarios:
        perfiles[usuario] = configuraciones_array
        
    return perfiles

print(configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False))
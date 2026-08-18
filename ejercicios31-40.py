# 2.31 Gestión de una red social con **kwargs y arrays
def publicar(usuario, texto, etiquetas=None, **kwargs):
    if etiquetas is None:
        etiquetas = []
        
    publicacion = {
        "usuario": usuario,
        "texto": texto,
        "etiquetas": etiquetas
    }
    
    for clave, valor in kwargs.items():
        publicacion[clave] = valor
        
    return publicacion

resultado_post = publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100)
print(resultado_post)


# 2.32 Simulación de ventas con tuplas, arrays, y *args
def simular_ventas(*args):
    ingresos_totales = 0
    for venta in args:
        cantidad = venta[1]
        precio = venta[2]
        ingresos_totales += cantidad * precio
    return ingresos_totales

total = simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0))
print(f"Total de ingresos: {total}")

# 2.33 Sistema de reservas con tuplas y diccionarios
reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

def hacer_reserva(fecha, huesped, habitacion, precio):
    if fecha not in reservas:
        reservas[fecha] = []
        
    for reserva_existente in reservas[fecha]:
        habitacion_ocupada = reserva_existente[1]
        if habitacion_ocupada == habitacion:
            return f"Error: La habitación {habitacion} ya está ocupada el {fecha}."
            
    nueva_tupla = (huesped, habitacion, precio)
    reservas[fecha].append(nueva_tupla)
    return f"Reserva exitosa para {huesped}."

print(hacer_reserva("2024-08-15", "Carlos", 101, 150)) # Dará error
print(hacer_reserva("2024-08-15", "Carlos", 103, 140)) # Será exitoso
print(reservas)

# 2.34 Análisis de resultados de encuestas con diccionarios y arrays
encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

def analizar_encuestas(diccionario_encuestas):
    resultados = {}
    for pregunta, respuestas in diccionario_encuestas.items():
        frecuencias = {}
        for respuesta in respuestas:
            if respuesta in frecuencias:
                frecuencias[respuesta] += 1
            else:
                frecuencias[respuesta] = 1
        resultados[pregunta] = frecuencias
    return resultados

print(analizar_encuestas(encuestas))

# 2.35. Optimización de rutas con arrays y tuplas
rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

def optimizar_rutas(lista_rutas, limites):
    rutas_validas = []
    for i in range(len(lista_rutas)):
        tupla_ruta = lista_rutas[i]
        distancia_real = tupla_ruta[2]
        limite_permitido = limites[i]
        
        if distancia_real <= limite_permitido:
            rutas_validas.append(tupla_ruta)
            
    return rutas_validas

print(optimizar_rutas(rutas, distancias_max))


# 2.26 Gestión de inventarios en múltiples tiendas con diccionarios y **kwargs
inventario_tiendas = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

def actualizar_inventario(tienda, **kwargs):
    if tienda in inventario_tiendas:
        for producto, cantidad_cambio in kwargs.items():
            if producto in inventario_tiendas[tienda]:
                inventario_tiendas[tienda][producto] += cantidad_cambio
            else:
                inventario_tiendas[tienda][producto] = cantidad_cambio
    else:
        print("La tienda no existe.")
        
    return inventario_tiendas

print(actualizar_inventario(tienda="Tienda A", producto_1=10, producto_2=-5))

# 2.37. Análisis de tendencias en redes sociales con arrays y tuplas
hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"] 
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

def filtrar_tendencias(lista_tendencias, minimo_menciones):
    hashtags_populares = []
    for hashtag, menciones in lista_tendencias:
        if menciones > minimo_menciones:
            hashtags_populares.append(hashtag)
    return hashtags_populares

print(filtrar_tendencias(tendencias, 100))


# 2.38 Administración de suscripciones con diccionarios, arrays, y **kwargs
suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

def actualizar_suscripcion(usuario, suscripcion, **kwargs):
    if usuario in suscripciones:
        suscripciones[usuario].append(suscripcion)
    else:
        suscripciones[usuario] = [suscripcion]
        
    return suscripciones

print(actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True))

# 2.39. Simulación de mercado bursátil con arrays y tuplas
precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

def simular_mercado(precios, lista_operaciones):
    balance = 0
    acciones_compradas = 0
    
    for tipo_operacion, dia in lista_operaciones:
        precio_del_dia = precios[dia]
        
        if tipo_operacion == "compra":
            balance -= precio_del_dia  
            acciones_compradas += 1
        elif tipo_operacion == "venta" and acciones_compradas > 0:
            balance += precio_del_dia 
            acciones_compradas -= 1
            
    return balance

print(f"Beneficio/Pérdida total: {simular_mercado(precios_diarios, operaciones)}")

# 2.40. Análisis de rendimiento académico con diccionarios y arrays
estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

def ranking_estudiantes(diccionario_estudiantes):
    promedios_generales = []
    
    for id_estudiante, materias in diccionario_estudiantes.items():
        suma_total_notas = 0
        cantidad_total_notas = 0
        
        for notas in materias.values():
            for nota in notas:
                suma_total_notas += nota
                cantidad_total_notas += 1
                
        promedio_general = suma_total_notas / cantidad_total_notas
        promedios_generales.append((promedio_general, id_estudiante))
        
    promedios_generales.sort(reverse=True)
    
    ranking = []
    for promedio, id_estudiante in promedios_generales:
        ranking.append(id_estudiante)
        
    return ranking

print(ranking_estudiantes(estudiantes))

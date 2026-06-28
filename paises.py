"""
TPI - Programacion 1
Gestion de Datos de Paises en Python
"""
directorio = "D:/UTN Tecnologica Nacional/Integrador/paises.csv"

import csv
def cargar_csv(directorio):
    paises = []
    try:
        with open(directorio, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except ValueError:
                    print(f"Error en fila: {fila}. Se omite.")
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo {directorio}.")
    return paises
def agregar_pais(paises):
    """Agrega un nuevo pais a la lista."""
    print("\n--- Agregar Pais ---")
    nombre = input("Nombre del pais: ").strip()
    if nombre == "":
        print("Error: el nombre no puede estar vacio.")
        return

    # Verificar duplicado
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print("Error: ese pais ya existe.")
            return

    try:
        poblacion = int(input("Poblacion: "))
        if poblacion < 0:
            print("Error: la poblacion no puede ser negativa.")
            return
    except ValueError:
        print("Error: ingrese un numero valido.")
        return

    try:
        superficie = int(input("Superficie en km2: "))
        if superficie < 0:
            print("Error: la superficie no puede ser negativa.")
            return
    except ValueError:
        print("Error: ingrese un numero valido.")
        return

    continente = input("Continente: ").strip()
    if continente == "":
        print("Error: el continente no puede estar vacio.")
        return

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    print(f"Pais '{nombre}' agregado correctamente.")


def actualizar_pais(paises):
    """Actualiza poblacion y superficie de un pais existente."""
    print("\n--- Actualizar Pais ---")
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    nombre = input("Nombre del pais a actualizar: ").strip().lower()
    encontrado = None
    for p in paises:
        if p["nombre"].lower() == nombre:
            encontrado = p
            break

    if encontrado is None:
        print("Error: pais no encontrado.")
        return

    print(f"Pais encontrado: {encontrado['nombre']} | Poblacion: {encontrado['poblacion']} | Superficie: {encontrado['superficie']}")

    try:
        nueva_poblacion = int(input("Nueva poblacion: "))
        if nueva_poblacion < 0:
            print("Error: la poblacion no puede ser negativa.")
            return
    except ValueError:
        print("Error: ingrese un numero valido.")
        return

    try:
        nueva_superficie = int(input("Nueva superficie en km2: "))
        if nueva_superficie < 0:
            print("Error: la superficie no puede ser negativa.")
            return
    except ValueError:
        print("Error: ingrese un numero valido.")
        return

    encontrado["poblacion"] = nueva_poblacion
    encontrado["superficie"] = nueva_superficie
    print("Pais actualizado correctamente.")


def buscar_pais(paises):
    """Busca un pais por nombre (coincidencia parcial o exacta)."""
    print("\n--- Buscar Pais ---")
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    buscar = input("Ingrese el nombre o parte del nombre: ").strip().lower()
    resultados = []
    for p in paises:
        if buscar in p["nombre"].lower():
            resultados.append(p)

    if len(resultados) == 0:
        print("No se encontraron paises.")
        return

    print(f"\nSe encontraron {len(resultados)} resultado(s):")
    for p in resultados:
        print(f"  {p['nombre']} | Poblacion: {p['poblacion']:,} | Superficie: {p['superficie']:,} km2 | Continente: {p['continente']}")


def filtrar_paises(paises):
    """Filtra paises por continente, rango de poblacion o superficie."""
    print("\n--- Filtrar Paises ---")
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    print("1. Por continente")
    print("2. Por rango de poblacion")
    print("3. Por rango de superficie")

    try:
        opcion = int(input("Seleccione filtro: "))
    except ValueError:
        print("Error: ingrese un numero valido.")
        return

    resultados = []

    if opcion == 1:
        continente = input("Continente: ").strip().lower()
        for p in paises:
            if p["continente"].lower() == continente:
                resultados.append(p)

    elif opcion == 2:
        try:
            minimo = int(input("Poblacion minima: "))
            maximo = int(input("Poblacion maxima: "))
        except ValueError:
            print("Error: ingrese numeros validos.")
            return
        for p in paises:
            if minimo <= p["poblacion"] <= maximo:
                resultados.append(p)

    elif opcion == 3:
        try:
            minimo = int(input("Superficie minima en km2: "))
            maximo = int(input("Superficie maxima en km2: "))
        except ValueError:
            print("Error: ingrese numeros validos.")
            return
        for p in paises:
            if minimo <= p["superficie"] <= maximo:
                resultados.append(p)

    else:
        print("Opcion no valida.")
        return

    if len(resultados) == 0:
        print("No se encontraron paises con ese criterio.")
        return

    print(f"\nResultados ({len(resultados)} paises):")
    for p in resultados:
        print(f"  {p['nombre']} | Poblacion: {p['poblacion']:,} | Superficie: {p['superficie']:,} km2 | Continente: {p['continente']}")


def ordenar_paises(paises):
    """Ordena los paises por nombre, poblacion o superficie."""
    print("\n--- Ordenar Paises ---")
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    print("1. Por nombre")
    print("2. Por poblacion")
    print("3. Por superficie")

    try:
        criterio = int(input("Seleccione criterio: "))
    except ValueError:
        print("Error: ingrese un numero valido.")
        return

    if criterio not in [1, 2, 3]:
        print("Opcion no valida.")
        return

    orden = input("Orden: 'A' ascendente o 'D' descendente: ").strip().upper()
    if orden not in ["A", "D"]:
        print("Opcion no valida.")
        return

    descendente = orden == "D"

    if criterio == 1:
        # Ordenamiento por nombre (burbuja)
        lista = paises[:]
        n = len(lista)
        for i in range(n - 1):
            for j in range(n - i - 1):
                comparar = lista[j]["nombre"].lower() > lista[j+1]["nombre"].lower()
                if (comparar and not descendente) or (not comparar and descendente):
                    lista[j], lista[j+1] = lista[j+1], lista[j]
    elif criterio == 2:
        lista = paises[:]
        n = len(lista)
        for i in range(n - 1):
            for j in range(n - i - 1):
                comparar = lista[j]["poblacion"] > lista[j+1]["poblacion"]
                if (comparar and not descendente) or (not comparar and descendente):
                    lista[j], lista[j+1] = lista[j+1], lista[j]
    else:
        lista = paises[:]
        n = len(lista)
        for i in range(n - 1):
            for j in range(n - i - 1):
                comparar = lista[j]["superficie"] > lista[j+1]["superficie"]
                if (comparar and not descendente) or (not comparar and descendente):
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    print(f"\nPaises ordenados:")
    for p in lista:
        print(f"  {p['nombre']} | Poblacion: {p['poblacion']:,} | Superficie: {p['superficie']:,} km2 | Continente: {p['continente']}")


def mostrar_estadisticas(paises):
    """Muestra estadisticas generales del dataset."""
    print("\n--- Estadisticas ---")
    if len(paises) == 0:
        print("No hay paises cargados.")
        return

    # Pais con mayor y menor poblacion
    mayor_pob = paises[0]
    menor_pob = paises[0]
    total_pob = 0
    total_sup = 0

    for p in paises:
        if p["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = p
        if p["poblacion"] < menor_pob["poblacion"]:
            menor_pob = p
        total_pob += p["poblacion"]
        total_sup += p["superficie"]

    promedio_pob = total_pob // len(paises)
    promedio_sup = total_sup // len(paises)

    # Cantidad de paises por continente
    continentes = {}
    for p in paises:
        c = p["continente"]
        if c in continentes:
            continentes[c] += 1
        else:
            continentes[c] = 1

    print(f"Total de paises: {len(paises)}")
    print(f"Pais con mayor poblacion: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,})")
    print(f"Pais con menor poblacion: {menor_pob['nombre']} ({menor_pob['poblacion']:,})")
    print(f"Promedio de poblacion: {promedio_pob:,}")
    print(f"Promedio de superficie: {promedio_sup:,} km2")
    print("\nPaises por continente:")
    for continente, cantidad in continentes.items():
        print(f"  {continente}: {cantidad} paises")

def mostrar_menu():
    """Muestra el menu principal."""
    print("\n========== GESTION DE PAISES ==========")
    print("1. Agregar un pais")
    print("2. Actualizar poblacion y superficie")
    print("3. Buscar pais por nombre")
    print("4. Filtrar paises")
    print("5. Ordenar paises")
    print("6. Mostrar estadisticas")
    print("7. Salir")
    print("========================================")

# ---------------- Bloque principal ----------------
paises = cargar_csv("paises.csv")
opcion = 0

while opcion != 7:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Error: ingrese un numero valido.")
        continue

    if opcion == 1:
        agregar_pais(paises)
    elif opcion == 2:
        actualizar_pais(paises)
    elif opcion == 3:
        buscar_pais(paises)
    elif opcion == 4:
        filtrar_paises(paises)
    elif opcion == 5:
        ordenar_paises(paises)
    elif opcion == 6:
        mostrar_estadisticas(paises)
    elif opcion == 7:
        print("Saliendo...")
    else:
        print("Error: opcion entre 1 y 7.")
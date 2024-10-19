def Leer_archivos(archivos):
    contenido = []
    for archivo in archivos:
        try:
            with open(archivo, "r") as f:
                contenido.append(f.read())  # Leer el contenido sin convertir a minúsculas
        except FileNotFoundError:
            print(f"Error: El archivo {archivo} no se encontró.")
    return contenido

def Contar_palabras(contenido):
    conteo = {}
    for texto in contenido:
        palabras = texto.split()    # Separamos el texto en palabras
        for palabra in palabras:
            
            # Normaliza la palabra eliminando caracteres no alfanuméricos
            palabra_normalizada = ""
            for letra in palabra:
                if ('a' <= letra <= 'z') or ('A' <= letra <= 'Z') or ('0' <= letra <= '9'):
                    palabra_normalizada += letra    # Agregar letra si es alfanumérica
            if palabra_normalizada:     # Asegurarse de que no esté vacía
                if palabra_normalizada in conteo:
                    conteo[palabra_normalizada] += 1    # Incrementamos el conteo
                else:
                    conteo[palabra_normalizada] = 1     # Inicializamos el conteo
    return conteo

def Archivo_salida(conteo, archivo_salida):
    # Creamos una lista de pares (palabra, frecuencia) y la ordenamos
    lista_ordenada = []
    for palabra in conteo:  # Recorre las claves del diccionario
        lista_ordenada.append((palabra, conteo[palabra]))  # Agregamos una tupla (palabra, frecuencia)

    # Ordenamos la lista por frecuencia
    for i in range(len(lista_ordenada)):
        for j in range(i + 1, len(lista_ordenada)):
            if lista_ordenada[i][1] < lista_ordenada[j][1]:  # Ordena por frecuencia
                lista_ordenada[i], lista_ordenada[j] = lista_ordenada[j], lista_ordenada[i]

    # Escribimos en el archivo de salida
    with open(archivo_salida, 'w') as f:
        for palabra, frecuencia in lista_ordenada:
            f.write(f'{palabra}: {frecuencia}\n')

# Programa Principal
archivos = ['Archivo_1.txt', 'Archivo_2.txt', 'Archivo_3.txt']
contenido = Leer_archivos(archivos)
cont = Contar_palabras(contenido)
Archivo_salida(cont, 'salida.txt')
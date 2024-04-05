def dividir_texto(texto, longitud_maxima):
    bloques = []
    inicio = 0
    while inicio < len(texto):
        bloque = texto[inicio:inicio + longitud_maxima]
        bloques.append(bloque)
        inicio += longitud_maxima
    return bloques

# Ruta al archivo JavaScript
ruta_archivo = "archivo.txt"  # Asegúrate de proporcionar la ruta correcta

# Definir la longitud máxima de cada bloque
longitud_maxima = 4000

# Leer el texto desde el archivo JavaScript
with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    texto_js = archivo.read()

# Dividir el texto en bloques de longitud máxima
bloques_de_texto = dividir_texto(texto_js, longitud_maxima)

# Escribir cada bloque en un archivo separado
for i, bloque in enumerate(bloques_de_texto):
    nombre_archivo = f"bloque_{i+1}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo_bloque:
        archivo_bloque.write(bloque)

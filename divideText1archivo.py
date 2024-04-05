def dividir_texto(texto, longitud_maxima):
    bloques = []
    inicio = 0
    while inicio < len(texto):
        bloque = texto[inicio:inicio + longitud_maxima]
        bloques.append(bloque)
        inicio += longitud_maxima
    return bloques

# Ruta al archivo JavaScript
ruta_archivo = "page-script.js"  # Asegúrate de proporcionar la ruta correcta

# Definir la longitud máxima de cada bloque
longitud_maxima = 4000

# Leer el texto desde el archivo JavaScript
with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    texto_js = archivo.read()

# Dividir el texto en bloques de longitud máxima
bloques_de_texto = dividir_texto(texto_js, longitud_maxima)

# Unir todos los bloques con dos líneas de asteriscos
texto_completo = "\n\n***********************************************************************\n\n".join(bloques_de_texto)

# Guardar el texto completo en un archivo
with open("texto_dividido.txt", "w", encoding="utf-8") as archivo_salida:
    archivo_salida.write(texto_completo)

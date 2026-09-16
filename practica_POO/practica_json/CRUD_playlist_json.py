import json
import os

class Musica:
    def __init__(self, nombre, genero, duracion):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion

    # JSON necesita diccionarios nativos, no objetos de clases personalizadas.
    # Este método traduce el objeto a un formato que JSON entiende.
    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "genero": self.genero,
            "duracion": self.duracion
        }

# Definimos el nombre del archivo en una constante para no escribirlo mal después
ARCHIVO = "playlist.json"

def cargar_desde_archivo():
    # Verificamos si el archivo físico ya existe en la compu
    if os.path.exists(ARCHIVO):
        try:
            # Abrimos el archivo en modo lectura ("r")
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo) # Transforma el texto JSON a una lista de diccionarios
                
                # Reconstruimos los objetos 'Musica' leyendo cada diccionario
                playlist_recuperada = []
                for item in datos:
                    cancion = Musica(item["nombre"], item["genero"], item["duracion"])
                    playlist_recuperada.append(cancion)
                return playlist_recuperada
        except json.JSONDecodeError:
            return [] # Si el archivo está vacío o roto, devolvemos una lista vacía
            
    return [] # Si el archivo no existe, también devolvemos lista vacía

def guardar_en_archivo(playlist):
    # Abrimos el archivo en modo escritura ("w")
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        # Convertimos cada objeto Musica en un diccionario
        datos = []
        for cancion in playlist:
            datos.append(cancion.a_diccionario())
            
        # Volcamos esa lista de diccionarios al archivo JSON
        # indent=4 le da los saltos de línea y espacios para que sea legible
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

        # 1. Carga inicial: Recuperamos datos antes de arrancar el menú
playlist = cargar_desde_archivo()

while True:
    print("\n--- MENÚ DE PLAYLIST ---")
    print("1. Agregar canción")
    print("2. Ver playlist")
    print("3. Salir")
    
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        genero = input("Género: ")
        duracion = float(input("Duración: "))
        
        # Creamos el objeto y lo guardamos en la memoria RAM
        nueva_cancion = Musica(nombre, genero, duracion)
        playlist.append(nueva_cancion)
        
        # ¡LA MAGIA!: Inmediatamente después, guardamos la lista entera en el disco
        guardar_en_archivo(playlist)
        print("¡Canción guardada con éxito en el archivo!")

    elif opcion == "2":
        for i, cancion in enumerate(playlist):
            print(f"{i + 1}. {cancion.nombre} - {cancion.genero} ({cancion.duracion} min)")

    elif opcion == "3":
        print("Saliendo...")
        break
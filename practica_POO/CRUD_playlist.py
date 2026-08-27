class Musica:
    def __init__(self, nombre, genero, duracion):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion

playlist = []

def agregar_cancion():

    print("\n--- AGREGAR NUEVA CANCIÓN ---")
    try:
        # Validación de nombre (permite letras y espacios)
        nombre = input("Ingresá el nombre de la canción: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if not all(caracter.isalnum() or caracter.isspace() for caracter in nombre):
            raise ValueError("El nombre solo debe contener letras, números y espacios.")
        
        # Validación de género (solo letras, sin espacios ni números)
        genero = input("Ingresá el género de la canción: ").strip()
        if not genero:
            raise ValueError("El género no puede estar vacío.")
        if not genero.isalpha():
            raise ValueError("El género solo debe contener letras, sin números ni espacios.")
        
        # Validación de duración (esperamos un número decimal o entero)
        duracion_str = input("Ingresá la duración en minutos (ej: 3.5): ").strip()
        duracion = float(duracion_str)
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor a 0.")

        # Creamos la instancia y la guardamos
        nueva_cancion = Musica(nombre, genero, duracion)
        playlist.append(nueva_cancion)
        print("¡Canción agregada con éxito a la playlist! 🎵")

    except ValueError as e:
        print(f"❌ Error al cargar los datos: {e}")

def mostrar_playlist():
    if not playlist:
        print("\nla playlist esta vacia...")
        return
    print("\n----Lista de canciones----")
    for indice, cancion in enumerate(playlist, start=1):
        print(f"{indice}. {cancion.nombre} | Género: {cancion.genero} | Duración: {cancion.duracion}")

def actualizar_playlist():
    mostrar_playlist()
    if not playlist:
        print("la playlist esta vacia...")
        return
    try:
        indice = int(input("Ingrese el indice de la cancion a modificar: "))
        indice_real = indice - 1

        if 0 <= indice_real < len(playlist):
            cancion_a_modificar = playlist[indice_real]
            print(f"modificando a {cancion_a_modificar.nombre}")

            nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
            if not all(caracter.isalnum() or caracter.isspace() for caracter in nuevo_nombre):
                raise ValueError("Error, valor ingresado no apropiado")

            nuevo_genero = input("Ingrese el nuevo genero: ").strip()
            if not nuevo_genero.isalpha():
                raise ValueError("Error, el genero solo puede contener letras, sin espacios ni numeros")

            nueva_duracion = float(input("Ingrese la nueva duracion"))

            cancion_a_modificar.nombre = nuevo_nombre
            cancion_a_modificar.genero = nuevo_genero 
            cancion_a_modificar.duracion = nueva_duracion

        else:
            print("Error, el indice ingresado no corresponde a la playlist!!!")

    except ValueError as e:
        print(f"Entrada invalida {e}!!!")

def Borrar_cancion():
    mostrar_playlist()
    if not playlist:
        print("la playlist esta vacia...")
        return
    try:
        indice = int(input("Ingrese el indice de la cancion a borrar: "))
        indice_real = indice - 1

        if 0 <= indice_real < len(playlist):
            cancion_eliminada = playlist.pop(indice_real)
            print(f"🗑️ Canción: '{cancion_eliminada.nombre}' eliminada correctamente.")
        else:
            print(f"Error! numero {indice_real} fuera de rango")

    except ValueError:
        print("❌ Por favor, ingresá un número válido.")

def menu():
    while True:
        print("\n---PLAYLIST---")
        print("\n1. Agregar una cancion")
        print("\n2. Modificar una cancion")
        print("\n3. Borrar una cancion")
        print("\n4. Mostrar playlist")
        print("\n5. Salir")

        try:
            opcion = int(input("Ingrese la opcion a realizar: "))

            if 1 <= opcion <= 5:
                if opcion == 1:
                    agregar_cancion()
                elif opcion == 2:
                    actualizar_playlist()
                elif opcion == 3:
                    Borrar_cancion()
                elif opcion == 4:
                    mostrar_playlist()
                elif opcion == 5:
                    print("Saliendo del programa...")
                    break
            else:
                print(f"Error! numero {opcion} fuera de rango")
        except ValueError:
            print("❌ Por favor, ingresá un número válido.")

if __name__ == "__main__":
    menu()



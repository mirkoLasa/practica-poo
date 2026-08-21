class Multimedia:
    def __init__(self, titulo, medida):
        self.titulo = titulo
        self.medida = medida

class Libro(Multimedia):
    def __init__(self, titulo, medida, autor):
        super().__init__(titulo, medida)
        self.autor = autor

class Pelicula(Multimedia):
    def __init__(self, titulo, medida, director):
        super().__init__(titulo, medida)
        self.director = director

# Nuestra base de datos temporal en memoria (mas adelante lo voy a guardar en un archivo de texto)
lista_multimedia = []

# --- 1. CREATE (Crear) ---
def agregar_elemento():
    print("\n--- [C]REAR ---")
    tipo = input("¿Qué querés agregar? (1: Libro, 2: Película): ")
    titulo = input("Título: ")
    
    try:
        medida = int(input("Medida (Páginas para libro / Minutos para película): "))
    except ValueError:
        print("❌ Error: Debe ser un número entero.")
        return

    if tipo == "1":
        autor = input("Autor: ")
        nuevo = Libro(titulo, medida, autor)
        lista_multimedia.append(nuevo)
        print(f"✅ ¡Libro '{titulo}' agregado!")
    elif tipo == "2":
        director = input("Director: ")
        nuevo = Pelicula(titulo, medida, director)
        lista_multimedia.append(nuevo)
        print(f"✅ ¡Película '{titulo}' agregada!")
    else:
        print("❌ Opción inválida. No se creó nada.")

# --- 2. READ (Leer / Mostrar) ---
def mostrar_elementos():
    print("\n--- [R]EAD (LISTA) ---")
    if not lista_multimedia:
        print("📭 La lista está vacía.")
        return
    
    for i, item in enumerate(lista_multimedia):
        # Usamos isinstance() para saber si es un Libro o una Película y mostrar los datos correctos
        if isinstance(item, Libro):
            print(f"{i}. [Libro] Título: {item.titulo} | Páginas: {item.medida} | Autor: {item.autor}")
        elif isinstance(item, Pelicula):
            print(f"{i}. [Película] Título: {item.titulo} | Duración: {item.medida} mins | Director: {item.director}")

# --- 3. UPDATE (Actualizar) ---
def actualizar_elemento():
    print("\n--- [U]PDATE (ACTUALIZAR) ---")
    mostrar_elementos()
    if not lista_multimedia:
        return
    
    try:
        indice = int(input("\nIngresá el número del elemento que querés actualizar: "))
        if 0 <= indice < len(lista_multimedia):
            item = lista_multimedia[indice]
            print(f"Modificando a: {item.titulo}")
            
            nuevo_titulo = input(f"Nuevo título (dejalo vacío para mantener '{item.titulo}'): ")
            if nuevo_titulo:
                item.titulo = nuevo_titulo
                
            print("✅ ¡Elemento actualizado con éxito!")
        else:
            print("❌ Número de índice fuera de rango.")
    except ValueError:
        print("❌ Por favor, ingresá un número válido.")

# --- 4. DELETE (Borrar) ---
def eliminar_elemento():
    print("\n--- [D]ELETE (BORRAR) ---")
    mostrar_elementos()
    if not lista_multimedia:
        return
    
    try:
        indice = int(input("\nIngresá el número del elemento que querés eliminar: "))
        if 0 <= indice < len(lista_multimedia):
            eliminado = lista_multimedia.pop(indice)
            print(f"🗑️ Elemento '{eliminado.titulo}' eliminado correctamente.")
        else:
            print("❌ Número de índice fuera de rango.")
    except ValueError:
        print("❌ Por favor, ingresá un número válido.")

# --- Menú principal ---
def menu():
    while True:
        print("\n--- MENÚ GESTIÓN MULTIMEDIA (CRUD) ---")
        print("1. Agregar elemento (Create)")
        print("2. Ver elementos (Read)")
        print("3. Actualizar elemento (Update)")
        print("4. Eliminar elemento (Delete)")
        print("5. Salir")
        
        opcion = input("Elegí una opción: ")
        
        if opcion == "1":
            agregar_elemento()
        elif opcion == "2":
            mostrar_elementos()
        elif opcion == "3":
            actualizar_elemento()
        elif opcion == "4":
            eliminar_elemento()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()
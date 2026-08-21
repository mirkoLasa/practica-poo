# 1. Crear clases: Usar una clase base Multimedia (con titulo y duracion o paginas) y 
# una clase hija (como Libro o Ebook) usando super().
# 2. Crear una lista de elementos: Guardar un par de objetos creados en una lista de Python.
# 3.Guardar en archivo (.txt): Escribir una función que recorra esa lista y guarde los datos de los 
# libros/e-books en un archivo de texto usando el bloque with open(...) con modo "w" o "a" y encoding="utf-8".
# 4.Leer el archivo: Hacer otra función que lea ese archivo de texto y lo imprima en la consola 
# para demostrar que los datos sobrevivieron y persisten.

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

pelicula1 = Pelicula("El Padrino", 175, "Francis Ford Coppola")
libro1 = Libro("El Túnel", 172, "Ernesto Sábato")
libro2 = Libro("Preguntale al Polvo", 187, "Fante")

lista_multimedia = [pelicula1, libro1, libro2]

def guardar_archivos(lista, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for item in lista:
            linea = f"titulo: {item.titulo}, duracion/cantidad: {item.medida}\n"
            archivo.write(linea)

    print("Datos guardados con exito en el archivo!")

guardar_archivos(lista_multimedia, "multimedia.txt")
class Libro:

    def __init__(self, id, titulo, autor, categoria, disponible=True, seccion=""):
        
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponible = disponible
        self.prestamos = 0
        self.seccion = seccion


    def mostrar(self):

        estado = "Disponible" if self.disponible else "No disponible"

        print("--------------------------")
        print("ID:", self.id)
        print("Titulo:", self.titulo)
        print("Autor:", self.autor)
        print("Categoria:", self.categoria)
        print("Prestamos:", self.prestamos)
        print("Seccion:", self.seccion)
        print("Estado:", estado)
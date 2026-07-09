class Usuario:

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.libros_prestados = []


    def mostrar(self):

        print("--------------------------")
        print("ID:", self.id)
        print("Nombre:", self.nombre)

        print("Libros prestados:")

        if len(self.libros_prestados) == 0:
            print("Ninguno")
        else:
            for libro in self.libros_prestados:
                print("-", libro.titulo)



    def puede_prestar(self):

        return len(self.libros_prestados) < 3
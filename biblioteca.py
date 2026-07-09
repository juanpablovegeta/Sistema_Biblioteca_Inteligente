import json
from libro import Libro
from usuario import Usuario


class Biblioteca:

    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []


    def agregar_libro(self, libro):

        self.libros.append(libro)

        print("Libro agregado correctamente")


    def mostrar_libros(self):

        if len(self.libros) == 0:
            print("No hay libros registrados")
            return

        for libro in self.libros:
            libro.mostrar()



    def buscar_libro(self, titulo):

        for libro in self.libros:

            if libro.titulo.lower() == titulo.lower():
                return libro

        return None



    def cambiar_estado(self, titulo):

        libro = self.buscar_libro(titulo)

        if libro:

            libro.disponible = not libro.disponible

            print("Estado actualizado")

        else:
            print("Libro no encontrado")



    def registrar_usuario(self, usuario):

        self.usuarios.append(usuario)

        print("Usuario registrado correctamente")



    def mostrar_usuarios(self):

        if len(self.usuarios) == 0:
            print("No hay usuarios registrados")
            return

        for usuario in self.usuarios:
            usuario.mostrar()



    def prestar_libro(self, id_usuario, titulo):

        usuario_encontrado = None


        for usuario in self.usuarios:

            if usuario.id == id_usuario:
                usuario_encontrado = usuario



        libro = self.buscar_libro(titulo)



        if usuario_encontrado == None:
            print("Usuario no encontrado")
            return


        if libro == None:
            print("Libro no encontrado")
            return



        if libro.disponible == False:
            print("El libro no está disponible")
            return



        if usuario_encontrado.puede_prestar() == False:
            print("El usuario ya tiene 3 libros prestados")
            return



        libro.disponible = False

        usuario_encontrado.libros_prestados.append(libro)

        libro.prestamos += 1


        self.prestamos.append({
            "usuario": usuario_encontrado.nombre,
            "libro": libro.titulo
        })


        print("Préstamo realizado correctamente")

    def guardar_datos(self):

        libros = []

        for libro in self.libros:

            libros.append({
                "id": libro.id,
                "titulo": libro.titulo,
                "autor": libro.autor,
                "categoria": libro.categoria,
                "disponible": libro.disponible
            })


        with open("libros.json","w") as archivo:
            json.dump(libros, archivo, indent=4)



        usuarios = []

        for usuario in self.usuarios:

            usuarios.append({
                "id": usuario.id,
                "nombre": usuario.nombre,
                "libros_prestados": [
                    libro.titulo for libro in usuario.libros_prestados
                ]
            })


        with open("usuarios.json","w") as archivo:
            json.dump(usuarios, archivo, indent=4)



        with open("prestamos.json","w") as archivo:

            json.dump(
                self.prestamos,
                archivo,
                indent=4
            )


        print("Datos guardados correctamente")

    def cargar_datos(self):

        try:

            with open("libros.json","r") as archivo:

                libros = json.load(archivo)


                for dato in libros:

                    libro = Libro(
                        dato["id"],
                        dato["titulo"],
                        dato["autor"],
                        dato["categoria"],
                        dato["disponible"],
                        dato.get("seccion","")
                    )

                    self.libros.append(libro)



            with open("usuarios.json","r") as archivo:

                usuarios = json.load(archivo)


                for dato in usuarios:

                    usuario = Usuario(
                        dato["id"],
                        dato["nombre"]
                    )

                    self.usuarios.append(usuario)



            with open("prestamos.json","r") as archivo:

                self.prestamos = json.load(archivo)



            print("Datos cargados correctamente")


        except FileNotFoundError:

            print("Archivos nuevos, iniciando sistema")

    def ordenar_titulo(self):

        libros = sorted(
            self.libros,
            key=lambda x:x.titulo
        )


        for libro in libros:
            libro.mostrar()



    def ordenar_autor(self):

        libros = sorted(
            self.libros,
            key=lambda x:x.autor
        )


        for libro in libros:
            libro.mostrar()



    def libro_mas_prestado(self):

        if len(self.libros) == 0:
            print("No hay libros")
            return


        libro = max(
            self.libros,
            key=lambda x:x.prestamos
        )


        print("Libro más prestado:")

        libro.mostrar()



    def usuario_mas_prestamos(self):

        if len(self.usuarios) == 0:
            print("No hay usuarios")
            return


        usuario = max(
            self.usuarios,
            key=lambda x:len(x.libros_prestados)
        )


        print("Usuario con más préstamos:")

        usuario.mostrar()


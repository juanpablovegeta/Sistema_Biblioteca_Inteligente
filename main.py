from usuario import Usuario
from libro import Libro
from biblioteca import Biblioteca
from grafo import Grafo


biblioteca = Biblioteca()

mapa = Grafo()


mapa.agregar_seccion("Entrada")
mapa.agregar_seccion("A")
mapa.agregar_seccion("B")
mapa.agregar_seccion("C")
mapa.agregar_seccion("D")


mapa.conectar("Entrada","A")
mapa.conectar("A","B")
mapa.conectar("A","C")
mapa.conectar("B","D")

biblioteca.cargar_datos()


while True:

    print("""
========= BIBLIOTECA INTELIGENTE =========

1. Agregar libro
2. Mostrar libros
3. Buscar libro
4. Cambiar disponibilidad
5. Registrar usuario
6. Prestar libro
7. Mostrar usuarios
8. Reportes
9. Buscar ruta del libro
10. Salir

""")

    opcion = input("Seleccione: ")


    if opcion == "1":

        id = int(input("ID: "))
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        categoria = input("Categoria: ")
        seccion = input("Seccion (Entrada/A/B/C/D): ")


        libro = Libro(
            id,
            titulo,
            autor,
            categoria,
            True,
            seccion
        )


        biblioteca.agregar_libro(libro)


    elif opcion == "2":

        biblioteca.mostrar_libros()


    elif opcion == "3":

        titulo = input("Titulo a buscar: ")

        resultado = biblioteca.buscar_libro(titulo)

        if resultado:
            resultado.mostrar()
        else:
            print("No encontrado")


    elif opcion == "4":

        titulo = input("Titulo del libro: ")

        biblioteca.cambiar_estado(titulo)


    elif opcion == "5":

        id = int(input("ID usuario: "))
        nombre = input("Nombre: ")

        usuario = Usuario(id,nombre)

        biblioteca.registrar_usuario(usuario)



    elif opcion == "6":

        id_usuario = int(input("ID usuario: "))
        titulo = input("Titulo libro: ")

        biblioteca.prestar_libro(
            id_usuario,
            titulo
        )



    elif opcion == "7":

        biblioteca.mostrar_usuarios()

    elif opcion == "8":

        print("""
    ------ REPORTES ------

    1. Ordenar por titulo
    2. Ordenar por autor
    3. Libro más prestado
    4. Usuario con más préstamos

    """)

        reporte = input("Seleccione: ")


        if reporte == "1":
            biblioteca.ordenar_titulo()

        elif reporte == "2":
            biblioteca.ordenar_autor()

        elif reporte == "3":
            biblioteca.libro_mas_prestado()

        elif reporte == "4":
            biblioteca.usuario_mas_prestamos()


    elif opcion == "9":

        titulo = input("Titulo del libro: ")


        libro = biblioteca.buscar_libro(titulo)


        if libro:

            ruta = mapa.buscar_ruta(
                "Entrada",
                libro.seccion
            )


            if ruta:

                print("Ruta:")
                print(
                    " -> ".join(ruta)
                )

            else:
                print("No existe una ruta hacia esa sección")


        else:
            print("Libro no encontrado")

    elif opcion == "10":

        biblioteca.guardar_datos()

        print("Sistema cerrado")

        break
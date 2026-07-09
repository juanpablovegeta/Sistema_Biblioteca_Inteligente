class Seccion:

    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []



class Grafo:

    def __init__(self):
        self.secciones = {}



    def agregar_seccion(self, nombre):

        self.secciones[nombre] = Seccion(nombre)



    def conectar(self, origen, destino):

        self.secciones[origen].conexiones.append(
            self.secciones[destino]
        )



    def buscar_ruta(self, inicio, destino):

        visitados = []

        ruta = self.recorrer(
            self.secciones[inicio],
            destino,
            visitados
        )

        return ruta



    def recorrer(self, actual, destino, camino):

        camino.append(actual.nombre)


        if actual.nombre == destino:
            return camino


        for siguiente in actual.conexiones:

            if siguiente.nombre not in camino:

                resultado = self.recorrer(
                    siguiente,
                    destino,
                    camino.copy()
                )


                if resultado:
                    return resultado


        return None
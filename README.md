#  Sistema de Biblioteca Inteligente

##  Descripción

Sistema de gestión bibliotecaria desarrollado en Python utilizando Programación Orientada a Objetos (POO), estructuras de datos, manejo de archivos JSON y algoritmos de búsqueda.

El sistema permite administrar libros, usuarios, préstamos y un mapa de navegación dentro de la biblioteca utilizando teoría de grafos.

---

#  Características del sistema

##  Gestión de libros

Permite:

- Registrar libros.
- Mostrar catálogo completo.
- Buscar libros por título.
- Cambiar disponibilidad del libro.
- Guardar la ubicación física del libro dentro de la biblioteca.

Cada libro contiene:

- ID
- Título
- Autor
- Categoría
- Disponibilidad
- Número de préstamos
- Sección


---

##  Gestión de usuarios

Permite:

- Registrar usuarios.
- Mostrar usuarios registrados.
- Controlar libros prestados.

Reglas implementadas:

- Un usuario puede tener máximo 3 libros prestados.
- No permite prestar libros que no están disponibles.


---

##  Sistema de préstamos

El sistema permite:

- Realizar préstamos.
- Cambiar estado del libro automáticamente.
- Registrar historial de préstamos.


Ejemplo:

Usuario: Jp
Libro: Programacion Python


---

#  Persistencia de datos

El sistema utiliza archivos JSON para guardar información automáticamente.

Archivos utilizados:


libros.json
usuarios.json
prestamos.json


Los datos se cargan automáticamente al iniciar el programa y se guardan al cerrar.


---

#  Reportes y algoritmos

El sistema implementa:

- Ordenamiento por título.
- Ordenamiento por autor.
- Libro más prestado.
- Usuario con más préstamos.

Se utilizan funciones de búsqueda y ordenamiento de Python.


---

#  Mapa de biblioteca con grafos

Se implementó un sistema de navegación mediante grafos.

Estructura del mapa:


Entrada
|
A
/
B C
|
D


El sistema calcula la ruta más corta hacia la sección donde se encuentra un libro.

Ejemplo:


Libro: Programacion Python

Ruta:
Entrada -> A -> B -> D


---

#  Estructura del proyecto


Sistema_Biblioteca_Inteligente/

│
├── main.py
├── libro.py
├── usuario.py
├── biblioteca.py
├── grafo.py
│
├── libros.json
├── usuarios.json
└── prestamos.json


---

#  Ejecución del programa

Requisitos:

- Python 3.x


Ejecutar:


python main.py


---

#  Tecnologías utilizadas

- Python
- Programación Orientada a Objetos
- Listas y diccionarios
- Archivos JSON
- Algoritmos de búsqueda
- Algoritmos de ordenamiento
- Grafos y recursividad


---

#  Autor

Juan Pablo Valadez Hernández



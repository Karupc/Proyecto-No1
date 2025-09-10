class Usuario:
    def __init__(self, nombre, correo, id):
        self.nombre = nombre
        self.correo = correo
        self.id = id

class Estudiante (Usuario):
    def __init__(self, nombre, correo, id):
        super().__init__(nombre, correo, id)

class Instructor(Usuario):
    def __init__(self, nombre, correo, id):
        super().__init__(nombre, correo, id)
        self.cursos_nuevos = []

    def crear_curso(self, nombre, cod):
        nombre = input("Ingrese el nombre del curso: ")
        cod = input("Ingrese el código del curso: ")
        curso = Curso(nombre, cod, self)
        self.cursos_nuevos.append(curso)
        print(f"El curso -{nombre}- ha sido creado")
        return curso

    def crear_evaluacion(self, curso, titulo, tipo, punteo):
        titulo = input("Ingresar el título de la evaluación: ")
        tipo = input("Ingrese que tipo de evaluación es (tarea o examen): ")
        punteo = input("Ingrese la ponderación: ")
        evaluacion = Evaluacion(titulo, tipo, punteo, curso)
        curso.evaluaciones.append(evaluacion)
        print(f"Se ha creado la evaluacion -{titulo}- en el curso -{curso.nombre}-")
        return evaluacion

class Curso:
    def __init__(self, nombre, cod, instructor):
        self.nombre = nombre
        self.cod = cod
        self.instructor = instructor
        self.estudiantes = []
        self.evaluaciones = []

    def incribir_estudiante(self, estudiante):
        pass

class Evaluacion:
    def __init__(self, titulo, tipo, punteo, curso):
        self.titulo = titulo
        self.tipo = tipo
        self.punteo = punteo
        self.curso = curso
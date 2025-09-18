class Usuario:
    def __init__(self, nombre, correo, id):
        self.nombre = nombre
        self.correo = correo
        self.id = id

class Estudiante (Usuario):
    def __init__(self, nombre, correro, id):
        super().__init__(nombre, correo, id)

class Instructor(Usuario):
    def __init__(self, nombre, correo, id):
        super().__init__(nombre, correo, id)
        self.cursos_nuevos = []

class Curso:
    def __init__(self, nombre, cod, instructor):
        self.nombre = nombre
        self.cod = cod
        self.instructor = instructor
        self.estudiantes = []
        seld.evaluaciones = []

class Evaluacion:
    def __init__(self, titulo, tipo, punteo, curso):
        self.titulo = titulo
        self.tipo = tipo
        self.punteo = punteo
        self.curso = curso
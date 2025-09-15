class Usuario:
    def __init__(self, nombre, correo, id):
        self.nombre = nombre
        self._correo = correo
        self.id = id

    @property
    def correo(self):
        return self._correo
    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo

class Estudiante (Usuario):
    def __init__(self, nombre, correo, id):
        super().__init__(nombre, correo, id)
        self.calificaciones = {}

class Instructor(Usuario):
    def __init__(self, nombre, correo, id):
        super().__init__(nombre, correo, id)
        self.cursos_nuevos = []

    def crear_curso(self, nombre, cod):
        try:
            nombre = input("Ingrese el nombre del curso: ").strip()
            cod = input("Ingrese el código del curso: ").strip()
            if not nombre or not cod:
                print("Debes ingresar nnombre y código ya que no pueden estar vacíos")
                return None
            curso = Curso(nombre, cod, self)
            self.cursos_nuevos.append(curso)
            print(f"El curso -{nombre}- ha sido creado")
            return curso
        except Exception as e:
            print(f"Error inesperado, vuelva a intentarlo: {e}")

    def crear_evaluacion(self, curso, titulo, tipo, punteo):
        try:
            titulo = input("Ingresar el título de la evaluación: ").strip()
            while True:
                tipo = input("Ingrese que tipo de evaluación es (tarea o examen): ").lower()
                if tipo in ["examen", "tarea"]:
                    break
                else:
                    print("El tipo es inválido, debe ingresar examen o tarea")
            while True:
                try:
                    punteo = int(input("Ingrese la ponderación: "))
                    if 0 <= punteo <= 100:
                        break
                    else:
                        print("La ponderación debe estar entre un rando de 0 y 100")
                except ValueError:
                    print("ERROR: El valor debe ser válido")

            evaluacion = Evaluacion(titulo, tipo, punteo, curso)
            curso.evaluaciones.append(evaluacion)
            print(f"Se ha creado la evaluacion -{titulo}- en el curso -{curso.nombre}-")
            return evaluacion
        except Exception as e:
            print(f"Error inesperado, vuelva a intentarlo: {e}")

class Curso:
    def __init__(self, nombre, cod, instructor):
        self.nombre = nombre
        self.cod = cod
        self.instructor = instructor
        self.estudiantes = []
        self.evaluaciones = []

    def incribir_estudiante(self):
        try:
            nombre = input("Ingresar el nombre del o la estudiante: ").strip()
            correo = input("Ingresar el correo del o la estudiante: ").strip()
            id = input("Ingresar el ID del o la estudiante").strip()
            if not nombre or not correo or not id:
                print("Es necesario llenar toda la información")

            for est in self.estudiantes:
                if est.id == id:
                    print("El estudiante ya está inscrito en este curso")

            estudiante = Estudiante(nombre, correo, id)
            print(f"{nombre} ha sido inscrit@ al curso {self.nombre}")
            return estudiante
        except Exception as e:
            print(f"Error inesperado, vuelva a intentarlo: {e}")


class Evaluacion:
    def __init__(self, titulo, tipo, punteo, curso):
        self.titulo = titulo
        self.tipo = tipo
        self.punteo = punteo
        self.curso = curso

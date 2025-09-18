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
                    punteo = input("Ingrese la ponderación: ")
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
        # Este diccionario almacena las calificaciones de los estudiantes por su ID.
        # Es una estructura de datos ideal para búsquedas rápidas.
        self.calificaciones = {}

    def registrar_calificacion(self, estudiante_id, evaluacion_titulo, nota):
        try:
            # Se usa el ID del estudiante como clave para acceder a sus calificaciones.
            if estudiante_id not in self.calificaciones:
                raise ValueError(f"No encuentro al estudiante con ID {estudiante_id} en este curso.")

            # Verifica si la evaluación existe en la lista de evaluaciones del curso.
            evaluacion_existe = any(e.titulo == evaluacion_titulo for e in self.evaluaciones)
            if not evaluacion_existe:
                raise ValueError(f"La evaluación '{evaluacion_titulo}' no existe aquí.")

            # Asigna la nota al diccionario de calificaciones del estudiante.
            self.calificaciones[estudiante_id][evaluacion_titulo] = nota
            print(
                f"La calificación de {nota} para el estudiante {estudiante_id} en '{evaluacion_titulo}' se guardó correctamente.")

        except ValueError as e:
            # Captura y muestra errores específicos, como estudiantes o evaluaciones no encontrados.
            print(f"Hubo un error: {e}")

    def consultar_estudiantes_y_calificaciones(self):
        print(f"\n--- Revisando las calificaciones del curso de {self.nombre} ---")
        if not self.estudiantes:
            print("Todavía no hay estudiantes inscritos en este curso.")
            return

        # Itera sobre la lista de objetos de estudiantes.
        for estudiante in self.estudiantes:
            print(f"\n  > Estudiante: {estudiante.nombre} (ID: {estudiante.id})")

            # Verifica si el estudiante tiene alguna calificación registrada en el diccionario.
            if estudiante.id in self.calificaciones and self.calificaciones[estudiante.id]:
                print("    - Notas:")
                # Recorre el diccionario de calificaciones del estudiante.
                for evaluacion, nota in self.calificaciones[estudiante.id].items():
                    print(f"      -> {evaluacion}: {nota}")
            else:
                print("    - Este estudiante aún no tiene notas registradas.")


class Plataforma:
    def __init__(self):
        # La plataforma centraliza todos los cursos para facilitar los reportes globales.
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def generar_reporte_promedios_bajos(self, umbral=70):

        print(f"\n--- Reporte de estudiantes con promedios por debajo de {umbral} ---")
        estudiantes_encontrados = False

        if not self.cursos:
            print("Parece que no hay cursos registrados en la plataforma.")
            return

        # Itera sobre todos los cursos registrados en la plataforma.
        for curso in self.cursos:
            print(f"\nRevisando el curso de {curso.nombre}:")

            if not curso.estudiantes:
                print("  - Este curso no tiene estudiantes.")
                continue

            # Itera sobre los estudiantes de cada curso.
            for estudiante in curso.estudiantes:
                # Obtiene las calificaciones del estudiante.
                calificaciones = curso.calificaciones.get(estudiante.id, {})

                # Si el estudiante tiene calificaciones, calcula su promedio.
                if calificaciones:
                    promedio = sum(calificaciones.values()) / len(calificaciones)
                    if promedio < umbral:
                        print(
                            f"  -> Alerta: {estudiante.nombre} (ID: {estudiante.id}) tiene un promedio de {promedio:.2f}.")
                        estudiantes_encontrados = True

        if not estudiantes_encontrados:
            print("\nTodos los estudiantes tienen un promedio por encima del umbral. Sigan así.")
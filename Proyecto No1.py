class Usuario:
    def __init__(self, nombre, correo, id, *args, **kwargs):
        self.nombre = nombre
        self._correo = correo
        self.id = id
        self.extra = kwargs

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo


class Estudiante(Usuario):
    def __init__(self, nombre, correo, id, *args, **kwargs):
        super().__init__(nombre, correo, id, *args, **kwargs)
        self.calificaciones = {}
        self.tipo = "estudiante"


class Instructor(Usuario):
    def __init__(self, nombre, correo, id, *args, **kwargs):
        super().__init__(nombre, correo, id, *args, **kwargs)
        self.cursos_nuevos = []
        self.tipo = "instructor"

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
        self.calificaciones = {}

    def incribir_estudiante(self):
        try:
            nombre = input("Ingresar el nombre del o la estudiante: ").strip()
            correo = input("Ingresar el correo del o la estudiante: ").strip()
            id_estudiante = input("Ingresar el ID del o la estudiante").strip()
            if not nombre or not correo or not id_estudiante:
                print("Es necesario llenar toda la información")
                return None

            for est in self.estudiantes:
                if est.id == id_estudiante:
                    print("El estudiante ya está inscrito en este curso")
                    return None

            estudiante = Estudiante(nombre, correo, id_estudiante)
            self.estudiantes.append(estudiante)
            self.calificaciones[estudiante.id] = {}
            print(f"{nombre} ha sido inscrit@ al curso {self.nombre}")
            return estudiante
        except Exception as e:
            print(f"Error inesperado, vuelva a intentarlo: {e}")

    def registrar_calificacion(self):
        try:
            if not self.estudiantes:
                print("No hay estudiantes inscritos en este curso")
                return
            if not self.evaluaciones:
                print("No hay evaluaciones creadas en este curso")
                return

            print("\nEstudiantes inscritos:")
            numeroEst = 1
            for alumno in self.estudiantes:
                print(f"{numeroEst}. {alumno.nombre} (ID: {alumno.id})")
                numeroEst += 1

            seleccionEst = int(input("Seleccione un estudiante por número: ")) - 1
            if seleccionEst < 0 or seleccionEst >= len(self.estudiantes):
                print("Opción inválida")
                return

            alumno_elegido = self.estudiantes[seleccionEst]

            print("\nEvaluaciones disponibles:")
            numeroEva = 1
            for evaluacion in self.evaluaciones:
                print(f"{numeroEva}. {evaluacion.titulo} ({evaluacion.tipo}, punteo {evaluacion.punteo})")
                numeroEva += 1

            seleccionEva = int(input("Seleccione una evaluación por número: ")) - 1
            if seleccionEva < 0 or seleccionEva >= len(self.evaluaciones):
                print("Opción inválida")
                return

            evaluacion_elegida = self.evaluaciones[seleccionEva]

            nota = float(input(f"Ingrese la nota obtenida en '{evaluacion_elegida.titulo}': "))
            if nota < 0 or nota > evaluacion_elegida.punteo:
                print(f"La nota debe estar entre 0 y {evaluacion_elegida.punteo}")
                return

            if alumno_elegido.id not in self.calificaciones:
                self.calificaciones[alumno_elegido.id] = {}
            self.calificaciones[alumno_elegido.id][evaluacion_elegida.titulo] = nota
            print(f"Nota registrada: {alumno_elegido.nombre} obtuvo {nota}/{evaluacion_elegida.punteo}")
        except ValueError:
            print("Entrada inválida, debe ingresar un número")
        except Exception as e:
            print(f"Error inesperado, vuelva a intentarlo: {e}")

    def consultar_estudiantes_y_calificaciones(self):
        print(f"\n--- Estudiantes y Calificaciones del Curso: {self.nombre} ---")
        if not self.estudiantes:
            print("No hay estudiantes inscritos en este curso.")
            return

        for estudiante in self.estudiantes:
            print(f"  > Estudiante: {estudiante.nombre} (ID: {estudiante.id})")

            if estudiante.id in self.calificaciones and self.calificaciones[estudiante.id]:
                print("    - Calificaciones:")
                for evaluacion, nota in self.calificaciones[estudiante.id].items():
                    print(f"      -> {evaluacion}: {nota}")
            else:
                print("    - Aún no se han registrado calificaciones.")


class Evaluacion:
    def __init__(self, titulo, tipo, punteo, curso):
        self.titulo = titulo
        self.tipo = tipo
        self.punteo = punteo
        self.curso = curso


class Plataforma:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def generar_reporte_promedios_bajos(self, umbral=70):
        print(f"\n--- Reporte de Estudiantes con Promedio Bajo (Menor a {umbral}) ---")
        estudiantes_con_promedio_bajo = False

        if not self.cursos:
            print("No hay cursos registrados en la plataforma.")
            return

        for curso in self.cursos:
            print(f"\nCurso: {curso.nombre}")

            if not curso.estudiantes:
                print("  - No hay estudiantes en este curso.")
                continue

            for estudiante in curso.estudiantes:
                calificaciones = curso.calificaciones.get(estudiante.id, {})

                if calificaciones:
                    promedio = sum(calificaciones.values()) / len(calificaciones)
                    if promedio < umbral:
                        print(
                            f"  -> Alerta: {estudiante.nombre} (ID: {estudiante.id}) tiene un promedio de {promedio:.2f}.")
                        estudiantes_con_promedio_bajo = True

        if not estudiantes_con_promedio_bajo:
            print("\n¡Excelente! No se encontraron estudiantes con promedio bajo en la plataforma.")


usuarios = []
cursos = []
plataforma = Plataforma()

def menu_estudiante(estudiante):
    while True:
        print(f"¡Hola! {estudiante.nombre} este es tu menú\n"
            "-----MENÚ DE ESTUDIANTES----\n"
            "1.- Ver los cursos en los que estás inscrito\n"
            "2.- Ver tus calificaciones\n"
            "3.- Salir a menú principal")
        try:
            opcion = int(input("Seleccione una opción: "))

            match opcion:
                case 1:
                    cursos_inscrito = [c for c in cursos if estudiante in c.estudiantes]
                    if not cursos_inscrito:
                        print("No estás inscrito en ningún curso")
                    else:
                        print("\nCursos en los que estás inscrito:")
                        for curso in cursos_inscrito:
                            print(f"- {curso.nombre}")
                case 2:
                    cursos_inscrito = [c for c in cursos if estudiante in c.estudiantes]
                    if not cursos_inscrito:
                        print("No estás inscrito en ningún curso.")
                    else:
                        for curso in cursos_inscrito:
                            print(f"\nCurso: {curso.nombre}")
                            notas = curso.calificaciones.get(estudiante.id, {})
                            if notas:
                                for evaluacion, nota in notas.items():
                                    print(f"  {evaluacion}: {nota}")
                            else:
                                print("  Sin calificaciones registradas.")
                case 3:
                    break
                case _:
                    print("Opción inválida")
        except ValueError:
            print("Entrada inválida")

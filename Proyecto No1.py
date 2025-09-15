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

class Estudiante (Usuario):
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

            alumno_elegido.calificaciones[evaluacion_elegida.titulo] = nota
            print(f"Nota registrada: {alumno_elegido.nombre} obtuvo {nota}/{evaluacion_elegida.punteo}")
        except ValueError:
            print("Entrada inválida, debe ingresar un número")
        except Exception as e:
            print(f"Error inesperado, vuelva a intentarlo: {e}")

class Evaluacion:
    def __init__(self, titulo, tipo, punteo, curso):
        self.titulo = titulo
        self.tipo = tipo
        self.punteo = punteo
        self.curso = curso

usuarios = []
cursos = []

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar usuario (Estudiante o Instructor)")
    print("2. Crear curso (solo instructor)")
    print("3. Inscribir estudiante en curso")
    print("4. Crear evaluación en un curso (solo instructor)")
    print("5. Registrar calificación")
    print("6. Consultar información (cursos, estudiantes, evaluaciones, calificaciones)")
    print("7. Generar reportes simples (estudiantes con promedio bajo)")
    print("8. Salir")

    try:
        opcion = int(input("Seleccione una opción: ").strip())

        match opcion:
            case 1:
                tipo = input("¿Registrar Estudiante (E) o Instructor (I)? ").strip().lower()
                nombre = input("Nombre: ").strip()
                correo = input("Correo: ").strip()
                id = input("ID: ").strip()

                if tipo == "e":
                    usuarios.append(Estudiante(nombre, correo, id))
                    print(f"Estudiante '{nombre}' registrado")
                elif tipo == "i":
                    usuarios.append(Instructor(nombre, correo, id))
                    print(f"Instructor '{nombre}' registrado")
                else:
                    print("Tipo inválido")

            case 2:
                if not usuarios:
                    print("No hay usuarios registrados")
                    continue

                print("\nInstructores registrados:")
                instructores = []
                contador = 1
                for usuario in usuarios:
                    if usuario.tipo == "instructor":
                        print(f"{contador}. {usuario.nombre}")
                        instructores.append(usuario)
                        contador += 1

                if not instructores:
                    print("No hay instructores para crear cursos")
                    continue

                seleccion = int(input("Seleccione un instructor por número: ")) - 1
                if 0 <= seleccion < len(instructores):
                    instructores[seleccion].crear_curso()
                else:
                    print("Opción inválida")
            case 3:
                print("Hola")
            case 4:
                print("Hola")
            case 5:
                print("Hola")
            case 6:
                print("Hola")
            case 7:
                print("Hola")
            case 8:
                print("Saliendo del programa")
                break

            case _:
                print("Opción no válida, intente de nuevo")
    except ValueError:
        print("Entrada inválida, debe ingresar un número entero")
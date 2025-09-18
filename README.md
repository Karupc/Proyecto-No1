# Sistema de Gestión de Cursos

Este proyecto es un sistema sencillo en Python que permite manejar cursos, usuarios (estudiantes e instructores), evaluaciones y calificaciones.  
Fue desarrollado como parte de un trabajo en grupo para el curso de Programación Orientada a Objetos.

## Funcionalidades principales

El programa tiene un menú interactivo en consola que permite:

1. Crear y administrar cursos  
   - Cada curso tiene un nombre, un código y un instructor asignado.

2. Registrar usuarios  
   - Se pueden registrar estudiantes e instructores.  
   - Todos los usuarios tienen: nombre, correo e ID.

3. Inscribir estudiantes en cursos  
   - Un estudiante se puede inscribir a un curso existente.  
   - Cada curso guarda la lista de estudiantes inscritos.

4. Crear evaluaciones  
   - El instructor puede crear evaluaciones para su curso (tareas o exámenes).  
   - Cada evaluación tiene: título, tipo y punteo.

5. Registrar calificaciones  
   - Se registran notas por estudiante y por evaluación.  
   - Las calificaciones quedan asociadas al estudiante dentro del curso.

6. Consultar información  
   - Listar cursos disponibles.  
   - Ver estudiantes inscritos en un curso.  
   - Consultar evaluaciones de un curso.  
   - Revisar calificaciones de los estudiantes.

7. Generar reportes simples  
   - Por ejemplo, mostrar estudiantes con promedios bajos.

## Decisiones de diseño

- Se aplicaron los cuatro pilares de la Programación Orientada a Objetos:  
  - Abstracción: Clases con atributos esenciales.  
  - Encapsulamiento: Uso de atributos privados y @property.  
  - Herencia: Estudiante e Instructor heredan de Usuario.  
  - Polimorfismo: Un mismo método puede tener distinto comportamiento según el tipo de usuario.

- Se usaron listas y diccionarios para manejar cursos, evaluaciones y calificaciones.

- Se implementó un menú con match case y control de errores con try/except para que el usuario no rompa el programa al ingresar opciones inválidas.

## Mejoras a futuro

- Implementar interfaz gráfica.  
- Exportar los reportes a PDF o Excel.  
- Agregar autenticación para usuarios.  
- Mejorar validaciones y evitar datos duplicados.


## Autores

- Proyecto realizado por [grupo Maravilla]  
- Curso: Programación Avanzada
- Integrantes: Jose, Karla y Sebastian :)

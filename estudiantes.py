# Programa: Sistema de Gestión de Notas de Estudiantes
# Estructura de datos principal: Diccionario (Nombre del estudiante: Nota)

def mostrar_menu():
    """Muestra las opciones disponibles al usuario."""
    print("\n" + "="*40)
    print("   SISTEMA DE GESTIÓN DE NOTAS")
    print("="*40)
    print("1. 📝 Agregar o actualizar nota de un estudiante")
    print("2. 🔍 Buscar la nota de un estudiante")
    print("3. 🗑️  Eliminar el registro de un estudiante")
    print("4.  Mostrar todos los estudiantes y sus notas.")
    print("5. 🚪 Salir del programa")
    print("="*40)

def agregar_estudiante(estudiantes):
    """Agrega un nuevo estudiante o actualiza su nota si ya existe."""
    nombre = input("Ingrese el nombre del estudiante: ").strip().title()
    try:
        nota = float(input("Ingrese la nota (0.0 - 10.0): "))
        if 0 <= nota <= 10:
            estudiantes[nombre] = nota
            print(f"✅ Éxito: La nota de {nombre} ha sido registrada/actualizada.")
        else:
            print("️ Error: La nota debe estar entre 0 y 10.")
    except ValueError:
        print("⚠️ Error: Por favor, ingrese un número válido para la nota.")

def buscar_estudiante(estudiantes):
    """Busca la nota de un estudiante específico."""
    nombre = input("Ingrese el nombre del estudiante a buscar: ").strip().title()
    if nombre in estudiantes: # Operación de búsqueda en diccionario
        print(f"🔎 El estudiante {nombre} tiene una nota de: {estudiantes[nombre]}")
    else:
        print(f"❌ El estudiante {nombre} no se encuentra en el registro.")

def eliminar_estudiante(estudiantes):
    """Elimina el registro de un estudiante."""
    nombre = input("Ingrese el nombre del estudiante a eliminar: ").strip().title()
    if nombre in estudiantes:
        del estudiantes[nombre] # Operación de eliminación
        print(f"🗑️  El registro de {nombre} ha sido eliminado.")
    else:
        print(f"❌ No se puede eliminar. El estudiante {nombre} no existe.")

def mostrar_todos(estudiantes):
    """Recorre el diccionario y muestra todos los datos."""
    print("\n--- 📊 LISTA DE ESTUDIANTES Y NOTAS ---")
    if not estudiantes: # Verifica si el diccionario está vacío
        print("No hay estudiantes registrados en el sistema.")
    else:
        # Operación de recorrido (iteración) sobre el diccionario
        for nombre, nota in estudiantes.items():
            estado = "Aprobado" if nota >= 5.0 else "Reprobado"
            print(f"👤 {nombre:<20} | Nota: {nota:<5} | Estado: {estado}")
    print("---------------------------------------")

def main():
    # 1. Implementación de la colección de datos (Diccionario vacío)
    estudiantes = {} 
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == '1':
            agregar_estudiante(estudiantes)
        elif opcion == '2':
            buscar_estudiante(estudiantes)
        elif opcion == '3':
            eliminar_estudiante(estudiantes)
        elif opcion == '4':
            mostrar_todos(estudiantes)
        elif opcion == '5':
            print(" ¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print("⚠️ Opción no válida. Por favor, seleccione un número del 1 al 5.")

# Bloque principal de ejecución
if __name__ == "__main__":
    main()
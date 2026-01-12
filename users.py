# empleados.py
RUTA_FICHERO = "empleados.txt"
import pandas as pd

def cargar_empleados():
    """Lee empleados.txt y devuelve una lista de diccionarios."""
    empleados = []
    try:
        with open(RUTA_FICHERO, "r", encoding="utf-8") as f:
            next(f)  # saltar encabezado
            for linea in f:
                partes = linea.strip().split(";")
                if len(partes) != 4:
                    continue
                emp = {
                    "id": int(partes[0]),
                    "nombre": partes[1],
                    "edad": int(partes[2]),
                    "puesto": partes[3],
                }
                empleados.append(emp)
    except FileNotFoundError:
        # Si no existe el archivo, empezamos con lista vacía
        empleados = []
    return empleados


def guardar_empleados(empleados):
    """Guarda la lista de empleados en empleados.txt."""
    with open(RUTA_FICHERO, "w", encoding="utf-8") as f:
        f.write("id;nombre;edad;puesto\n")
        for e in empleados:
            linea = f"{e['id']};{e['nombre']};{e['edad']};{e['puesto']}\n"
            f.write(linea)


def buscar_empleado_por_id(empleados, id_buscar):
    """Devuelve el diccionario del empleado con ese id, o None."""
    for e in empleados:
        if e["id"] == id_buscar:
            return e
    return None


def mostrar_empleado(e):
    """Imprime los datos de un empleado."""
    if e is None:
        print("Empleado no encontrado")
    else:
        print("----- EMPLEADO -----")
        print(f"ID: {e['id']}")
        print(f"Nombre: {e['nombre']}")
        print(f"Edad: {e['edad']}")
        print(f"Puesto: {e['puesto']}")
        print("--------------------")


def listar_empleados(empleados):
    """Muestra todos los empleados."""
    if not empleados:
        print("No hay empleados registrados")
        return
    for e in empleados:
        mostrar_empleado(e)


def agregar_empleado(empleados):
    """Pide datos por teclado y añade un empleado a la lista."""
    print("== Añadir empleado ==")
    nuevo_id = int(input("ID: "))
    # Comprobar si ya existe
    if buscar_empleado_por_id(empleados, nuevo_id) is not None:
        print("Ya existe un empleado con ese ID")
        return

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    puesto = input("Puesto: ")

    empleados.append({
        "id": nuevo_id,
        "nombre": nombre,
        "edad": edad,
        "puesto": puesto
    })
    print("Empleado añadido correctamente")


def editar_empleado(empleados):
    """Permite modificar los datos de un empleado."""
    print("== Editar empleado ==")
    id_editar = int(input("ID del empleado a editar: "))
    emp = buscar_empleado_por_id(empleados, id_editar)
    if emp is None:
        print("Empleado no encontrado")
        return

    print("Pulsa Enter para dejar el valor actual")
    nuevo_nombre = input(f"Nombre ({emp['nombre']}): ")
    nuevo_edad = input(f"Edad ({emp['edad']}): ")
    nuevo_puesto = input(f"Puesto ({emp['puesto']}): ")

    if nuevo_nombre != "":
        emp["nombre"] = nuevo_nombre
    if nuevo_edad != "":
        emp["edad"] = int(nuevo_edad)
    if nuevo_puesto != "":
        emp["puesto"] = nuevo_puesto

    print("Empleado actualizado")


def eliminar_empleado(empleados):
    """Elimina un empleado por ID."""
    print("== Eliminar empleado ==")
    id_eliminar = int(input("ID del empleado a eliminar: "))
    emp = buscar_empleado_por_id(empleados, id_eliminar)
    if emp is None:
        print("Empleado no encontrado")
        return
    empleados.remove(emp)
    print("Empleado eliminado")


def menu():
    empleados = cargar_empleados()
    while True:
        print("\n===== GESTIÓN DE EMPLEADOS =====")
        print("1. Listar empleados")
        print("2. Ver empleado por ID")
        print("3. Añadir empleado")
        print("4. Editar empleado")
        print("5. Eliminar empleado")
        print("6. Guardar y salir")

        opcion = input("Opción: ")

        if opcion == "1":
            listar_empleados(empleados)
            df = pd.DataFrame(empleados)
            print(df)
        elif opcion == "2":
            id_buscar = int(input("ID empleado: "))
            emp = buscar_empleado_por_id(empleados, id_buscar)
            mostrar_empleado(emp)
        elif opcion == "3":
            agregar_empleado(empleados)
        elif opcion == "4":
            editar_empleado(empleados)
        elif opcion == "5":
            eliminar_empleado(empleados)
        elif opcion == "6":
            guardar_empleados(empleados)
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()

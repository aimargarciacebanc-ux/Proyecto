# empleados.py
import pandas as pd

RUTA_FICHERO = "empleados.txt"


def cargar_empleados():
    """Lee empleados.txt con Pandas y devuelve DataFrame."""
    try:
        df = pd.read_csv(RUTA_FICHERO, sep=";", encoding="utf-8")
        return df
    except FileNotFoundError:
        # Crear DataFrame vacío con columnas
        return pd.DataFrame(columns=["id", "nombre", "edad", "puesto"])


def guardar_empleados(df):
    """Guarda DataFrame en empleados.txt con separador ;."""
    df.to_csv(RUTA_FICHERO, sep=";", index=False, encoding="utf-8")


def buscar_empleado_por_id(df, id_buscar):
    """Devuelve fila del DataFrame o None."""
    fila = df[df["id"] == id_buscar]
    if not fila.empty:
        return fila.iloc[0]
    return None


def mostrar_empleado(fila):
    """Imprime datos de un empleado."""
    if fila is None:
        print("Empleado no encontrado")
    else:
        print("----- EMPLEADO -----")
        print(f"ID: {fila['id']}")
        print(f"Nombre: {fila['nombre']}")
        print(f"Edad: {fila['edad']}")
        print(f"Puesto: {fila['puesto']}")
        print("--------------------")


def listar_empleados(df):
    """Muestra DataFrame con Pandas."""
    if df.empty:
        print("No hay empleados registrados")
        return
    print(df)  # Solo Pandas, sin lista Python


def agregar_empleado(df):
    """Añade fila nueva al DataFrame."""
    print("== Añadir empleado == ")
    nuevo_id = int(input("ID: "))
    if nuevo_id in df["id"].values:
        print("Ya existe un empleado con ese ID")
        return

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    puesto = input("Puesto: ")

    nuevo_empleado = pd.DataFrame({
        "id": [nuevo_id],
        "nombre": [nombre],
        "edad": [edad],
        "puesto": [puesto]
    })
    return pd.concat([df, nuevo_empleado], ignore_index=True)


def editar_empleado(df):
    """Edita fila en DataFrame."""
    print("== Editar empleado ==")
    id_editar = int(input("ID del empleado a editar: "))
    fila = df[df["id"] == id_editar]
    if fila.empty:
        print("Empleado no encontrado")
        return df

    print("Pulsa Enter para dejar el valor actual")
    nuevo_nombre = input(f"Nombre ({fila['nombre'].iloc[0]}): ") or fila['nombre'].iloc[0]
    nuevo_edad = input(f"Edad ({fila['edad'].iloc[0]}): ") or fila['edad'].iloc[0]
    nuevo_puesto = input(f"Puesto ({fila['puesto'].iloc[0]}): ") or fila['puesto'].iloc[0]

    df.loc[df["id"] == id_editar, "nombre"] = nuevo_nombre
    df.loc[df["id"] == id_editar, "edad"] = int(nuevo_edad)
    df.loc[df["id"] == id_editar, "puesto"] = nuevo_puesto
    return df


def eliminar_empleado(df):
    """Elimina fila del DataFrame."""
    print("== Eliminar empleado ==")
    id_eliminar = int(input("ID del empleado a eliminar: "))
    df = df[df["id"] != id_eliminar]
    return df


def menu():
    df = cargar_empleados()
    
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
            listar_empleados(df)
        elif opcion == "2":
            id_buscar = int(input("ID empleado: "))
            emp = buscar_empleado_por_id(df, id_buscar)
            mostrar_empleado(emp)
        elif opcion == "3":
            df = agregar_empleado(df)
        elif opcion == "4":
            df = editar_empleado(df)
        elif opcion == "5":
            df = eliminar_empleado(df)
        elif opcion == "6":
            guardar_empleados(df)
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()

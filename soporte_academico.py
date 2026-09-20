# ===============================================
# SISTEMA DE SOPORTE ACADÉMICO
# Laboratorio N° 2 - Funciones y Modularidad
# ===============================================

# -----------------------------------
# FUNCIONES DE VALIDACIÓN
# Álvaro Leandro Gutiérrez Carranza
# ----------------------------------
def validar_texto(valor, nombre_campo):
    """Valida que un texto no esté vacío."""
    if valor is None or valor.strip() == "":
        print(f"Error: El campo '{nombre_campo}' no puede estar vacío.")
        return False
    return True

def validar_codigo(codigo):
    """Valida que el código no esté vacío y tenga al menos 4 caracteres."""
    if not validar_texto(codigo, "código de estudiante"):
        return False
    if len(codigo.strip()) < 4:
        print("Error: El código debe tener al menos 4 caracteres.")
        return False
    return True

def validar_tipo_consulta(tipo):
    """Valida que el tipo de consulta esté en la lista permitida."""
    tipos_validos = ["matrícula", "pagos", "constancia", "plataforma", "otro"]
    if tipo.lower().strip() not in tipos_validos:
        print(f"Error: Tipo de consulta inválido. Use: {', '.join(tipos_validos)}")
        return False
    return True

# ----------------------------------
# FUNCIÓN DE CÁLCULO DE PRIORIDAD
# Álvaro Leandro Gutiérrez Carranza
# ----------------------------------
def calcular_prioridad(tipo_consulta):
    """Asigna prioridad según el tipo de consulta."""
    tipo = tipo_consulta.lower().strip()
    if tipo == "pagos" or tipo == "matrícula":
        return "ALTA"
    elif tipo == "plataforma":
        return "MEDIA"
    else:
        return "BAJA"

# ------------------------------
# FUNCIONES DE MENÚ Y REGISTRO
# Cristian Omar Huamán Rojas
# ------------------------------
def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n" + "=" * 45)
    print("   SISTEMA DE SOPORTE ACADÉMICO")
    print("=" * 45)
    print("1. Registrar nueva solicitud")
    print("2. Mostrar resumen de solicitudes")
    print("3. Salir")
    print("=" * 45)

def registrar_solicitud():
    """Registra una nueva solicitud validando los datos."""
    print("\n---REGISTRO DE NUEVA SOLICITUD ---")
    codigo = input("Ingrese código de estudiante: ")
    if not validar_codigo(codigo):
        return None
    nombre = input("Ingrese nombre del estudiante: ")
    if not validar_texto(nombre, "nombre"):
        return None
    tipo = input("Ingrese tipo de consulta (matrícula/pagos/constancia/plataforma/otro): ")
    if not validar_tipo_consulta(tipo):
        return None
    descripcion = input("Ingrese descripción breve: ")
    if not validar_texto(descripcion, "descripción"):
        return None
    prioridad = calcular_prioridad(tipo)
    solicitud = {
        "codigo": codigo.strip(),
        "nombre": nombre.strip(),
        "tipo": tipo.lower().strip(),
        "descripcion": descripcion.strip(),
        "prioridad": prioridad
    }
    print(f"\nSolicitud registrada con prioridad {prioridad}.")
    return solicitud

# --------------------------------------
# FUNCIONES DE RESUMEN Y LISTADO
# Zinedine Michael Callirgos Cabanillas
# --------------------------------------
def mostrar_resumen(solicitud):
    """Muestra el resumen de una solicitud."""
    print("\n" + "-" * 45)
    print("   RESUMEN DE LA SOLICITUD")
    print("-" * 45)
    print(f"  Código     : {solicitud['codigo']}")
    print(f"  Nombre     : {solicitud['nombre']}")
    print(f"  Tipo       : {solicitud['tipo']}")
    print(f"  Descripción: {solicitud['descripcion']}")
    print(f"  Prioridad  : {solicitud['prioridad']}")
    print("-" * 45)

def mostrar_todas_las_solicitudes(lista_solicitudes):
    """Muestra todas las solicitudes registradas."""
    if len(lista_solicitudes) == 0:
        print("\nNo hay solicitudes registradas.")
        return
    print(f"\n  Total de solicitudes registradas: {len(lista_solicitudes)}")
    for i, solicitud in enumerate(lista_solicitudes, 1):
        print(f"\n--- Solicitud N° {i} ---")
        mostrar_resumen(solicitud)

# -------------------------------
# FUNCIÓN DE ESTADÍSTICAS
# Anthony Rene Terraz Terrones
# -------------------------------
def mostrar_estadisticas(lista_solicitudes):
    """Muestra cuántas solicitudes hay por prioridad."""
    if len(lista_solicitudes) == 0:
        print("\nNo hay solicitudes para mostrar estadísticas.")
        return
    altas = sum(1 for s in lista_solicitudes if s["prioridad"] == "ALTA")
    medias = sum(1 for s in lista_solicitudes if s["prioridad"] == "MEDIA")
    bajas = sum(1 for s in lista_solicitudes if s["prioridad"] == "BAJA")
    print("\n" + "=" * 45)
    print("   ESTADÍSTICAS DE ATENCIÓN")
    print("=" * 45)
    print(f"Prioridad ALTA: {altas}")
    print(f"Prioridad MEDIA: {medias}")
    print(f"Prioridad BAJA : {bajas}")
    print("=" * 45)

# ----------------------------
# FUNCIÓN PRINCIPAL
# Juan Orlando Correa Flores
# ----------------------------
def main():
    """Controla el flujo principal del programa."""
    solicitudes = []
    opcion = ""
    while opcion != "3":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            if len(solicitudes) >= 3:
                print("\nYa se registraron 3 solicitudes (límite de la práctica).")
                continue
            nueva = registrar_solicitud()
            if nueva is not None:
                solicitudes.append(nueva)
                mostrar_resumen(nueva)
        elif opcion == "2":
            mostrar_todas_las_solicitudes(solicitudes)
        elif opcion == "3":
            print("\nSaliendo del sistema. ¡Hasta luego!")
        else:
            print("\nOpción inválida. Intente de nuevo.")

# ------------------
# PUNTO DE ENTRADA
# -------------------
if __name__ == "__main__":
    main()
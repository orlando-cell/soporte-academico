
# Archivo principal del sistema
 # cristian Huaman Rojas

def mostrar_menu():
    print("\n" + "=" * 45)
    print("   SISTEMA DE SOPORTE ACADÉMICO")
    print("=" * 45)
    print("1. Registrar nueva solicitud")
    print("2. Mostrar resumen de solicitudes")
    print("3. Salir")
    print("=" * 45)

def registrar_solicitud():
    print("\n--- REGISTRO DE NUEVA SOLICITUD ---")
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
    print(f"\n   Solicitud registrada con prioridad {prioridad}.")
    return solicitud

# Archivo principal del sistema
# Alvaro Leandro Gurtierrez Carranza

def validar_texto(valor, nombre_campo):
    if valor is None or valor.strip() == "":
        print(f"   Error: El campo '{nombre_campo}' no puede estar vacío.")
        return False
    return True

def validar_codigo(codigo):
    if not validar_texto(codigo, "código de estudiante"):
        return False
    if len(codigo.strip()) < 4:
        print("   Error: El código debe tener al menos 4 caracteres.")
        return False
    return True

def validar_tipo_consulta(tipo):
    tipos_validos = ["matrícula", "pagos", "constancia", "plataforma", "otro"]
    if tipo.lower().strip() not in tipos_validos:
        print(f"   Error: Tipo de consulta inválido. Use: {', '.join(tipos_validos)}")
        return False
    return True

def calcular_prioridad(tipo_consulta):
    tipo = tipo_consulta.lower().strip()
    if tipo == "pagos" or tipo == "matrícula":
        return "ALTA"
    elif tipo == "plataforma":
        return "MEDIA"
    else:
        return "BAJA"


# Archivo principal del sistema
# Orlando correa Flores
def main():
    solicitudes = []
    opcion = ""
    while opcion != "3":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            if len(solicitudes) >= 3:
                print("\n  ⚠ Ya se registraron 3 solicitudes (límite de la práctica).")
                continue
            nueva = registrar_solicitud()
            if nueva is not None:
                solicitudes.append(nueva)
                mostrar_resumen(nueva)
        elif opcion == "2":
            mostrar_todas_las_solicitudes(solicitudes)
        elif opcion == "3":
            print("\n  👋 Saliendo del sistema. ¡Hasta luego!")
        else:
            print("\n  ❌ Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()

def mostrar_estadisticas(lista_solicitudes):
    """Muestra cuántas solicitudes hay por prioridad."""
    if len(lista_solicitudes) == 0:
        print("\n   No hay solicitudes para mostrar estadísticas.")
        return
    altas = sum(1 for s in lista_solicitudes if s["prioridad"] == "ALTA")
    medias = sum(1 for s in lista_solicitudes if s["prioridad"] == "MEDIA")
    bajas = sum(1 for s in lista_solicitudes if s["prioridad"] == "BAJA")
    print("\n" + "=" * 45)
    print("   ESTADÍSTICAS DE ATENCIÓN")
    print("=" * 45)
    print(f"  Prioridad ALTA : {altas}")
    print(f"  Prioridad MEDIA: {medias}")
    print(f"  Prioridad BAJA : {bajas}")
    print("=" * 45)
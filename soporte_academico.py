# Archivo principal del sistema
 
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
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
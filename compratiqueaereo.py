

# creamos una lista para guardar las reservas
reservas = []
contador_id = 1  # contador para generar ID únicos

# Función para calcular el costo del equipaje principal
def calcular_costo_equipaje(peso):
    if peso <= 20:
        return 50000
    elif peso <= 30:
        return 70000
    elif peso <= 50:
        return 110000
    else:
        return None  # Peso no admitido

# Función para obtener el precio según el tipo de viaje
def obtener_precio_base(tipo_viaje):
    if tipo_viaje == "nacional":
        return 230000
    elif tipo_viaje == "internacional":
        return 4200000

# Función para generar un ID único
def generar_id(numero):
    return f"COMP{numero:04d}"

# Función principal para registrar un pasajero
def registrar_pasajero():
    global contador_id
    print("\n--- Registro de Pasajero ---")
    nombre = input("Nombre del pasajero: ").strip()
    
    # Validar tipo de viaje
    while True:
        tipo_viaje = input("Tipo de viaje (nacional/internacional): ").lower().strip()
        if tipo_viaje in ["nacional", "internacional"]:
            break
        print("Ingrese un tipo de viaje válido.")

    if tipo_viaje == "nacional":
        destino = "Bogotá - Medellín"
    else:
        destino = "Bogotá - España"
    print(f"Destino: {destino}")
    # Validar peso del equipaje principal
    while True:
        try:
            peso_principal = float(input("Peso del equipaje principal (kg): "))
            if peso_principal >= 0:
                break
        except:
            pass
        print("Ingrese un número válido.")
    #calculamos el costo del equipaje
    # y lo guardamos en la variable costo_equipaje
    costo_equipaje = calcular_costo_equipaje(peso_principal)
    estado_principal = costo_equipaje
    if estado_principal is not None:
        estado_principal = "Equipaje admitido"
    else:
        estado_principal = "No admitido"
    
    # variable Equipaje de mano muestra si el pasajero lleva equipaje de mano
    # y el peso del equipaje de mano
    lleva_mano = input("¿Lleva equipaje de mano? (si/no): ").lower().strip()
    if lleva_mano == "si":
        while True:
            try:
                peso_mano = float(input("Peso del equipaje de mano (kg): "))
                if peso_mano >= 0:
                    break
            except:
                pass
            print(" Ingrese un número válido.")
        estado_mano = peso_mano
        if estado_mano <= 13:
            estado_mano = "Equipaje de mano aceptado"
        else:
            estado_mano = " Rechazado (excede 13 kg)"   
        
    #ingresamos la fecha del viaje
    fecha = input("Fecha del viaje (DD/MM/AAAA): ").strip()
    #sumamos 1 al contador de id para generar un id único   
    id_compra = generar_id(contador_id)
    contador_id += 1
    #generamos el precio base según el tipo de viaje
    # y lo guardamos en la variable precio_base
    precio_base = obtener_precio_base(tipo_viaje)
    if costo_equipaje is not None:
        total = precio_base + costo_equipaje
    else:
        total = precio_base
    
    reserva = {
        "ID": id_compra,
        "Nombre": nombre,
        "Destino": destino,
        "Fecha": fecha,
        "Tipo": tipo_viaje,
        "Estado Equipaje Principal": estado_principal,
        "Estado Equipaje Mano": estado_mano,
        "Total": total if costo_equipaje is not None else precio_base,
    }
    # Agregamos la reserva a la lista de reservas
    reservas.append(reserva)
    
    print(" Reserva registrada con éxito.")
    print("--- RESUMEN ---")
    for clave, valor in reserva.items():
        print(f"{clave}: {valor}")

# Función para reportes del administrador
def menu_admin():
    while True:
        print(" Menú de Reportes")
        print("1. Total recaudado en todas las compras")
        print("2. Total recaudado en una fecha específica")
        print("3. Número total de pasajeros procesados")
        print("4. Número de pasajeros por tipo de viaje")
        print("5. Buscar compra por ID")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            total = sum(r["Total"] for r in reservas)
            print(f" Total recaudado: ${total}")
        
        elif opcion == "2":
            fecha = input("Ingrese la fecha (DD/MM/AAAA): ").strip()
            total = sum(r["Total"] for r in reservas if r["Fecha"] == fecha)
            print(f" Total en la fecha {fecha}: ${total}")
        
        elif opcion == "3":
            print(f" Pasajeros procesados: {len(reservas)}")
        
        elif opcion == "4":
            nacionales = sum(1 for r in reservas if r["Tipo"] == "nacional")
            internacionales = sum(1 for r in reservas if r["Tipo"] == "internacional")
            print(f"Nacionales: {nacionales}, Internacionales: {internacionales}")
        
        elif opcion == "5":
            buscar = input("Ingrese ID de compra: ").strip().upper()
            encontrado = False
            for r in reservas:
                if r["ID"] == buscar:
                    print("\n--- Detalles de la compra ---")
                    for clave, valor in r.items():
                        print(f"{clave}: {valor}")
                    encontrado = True
                    break
            if not encontrado:
                print(" Compra no encontrada.")
        
        elif opcion == "6":
            break
        
        else:
            print(" Opción inválida. Intenta de nuevo.")

# Menú principal
def menu_principal():
    while True:
        print(" Menú Principal")
        print("1. Registrar pasajero")
        print("2. Ver reportes (admin)")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_pasajero()
        elif opcion == "2":
            menu_admin()
        elif opcion == "3":
            print(" Gracias por usar el sistema. ¡Buen viaje!")
            break
        else:
            print(" Opción inválida.")

# Ejecutar el programa
menu_principal()

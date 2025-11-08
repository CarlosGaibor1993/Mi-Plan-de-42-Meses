try:
    capital_total = float(input('Ingrese su capital total: '))
    precio_de_entrada = float(input('Ingrese su precio de entrada: '))
    stop_loss = float(input('Ingrese su Stop loss: '))
    tendencia = input('¿Es la tendencia a favor? (si/no): ')

    # Usamos abs() para que el riesgo sea siempre un número positivo
    riesgo_en_dinero = abs(precio_de_entrada - stop_loss)
    porcentage_de_riesgo = (riesgo_en_dinero / capital_total) * 100

    # --- LÓGICA CORREGIDA ---
    # Combinamos TODAS las reglas en una sola condición con 'and'.
    # Si todas son verdaderas, entonces es GO.
    if (porcentage_de_riesgo <= 2) and (tendencia == 'si') and (stop_loss < precio_de_entrada):
        print("\n--- Resultado del Checklist ---")
        print(f"Riesgo de la operación: {porcentage_de_riesgo:.2f}%")
        print("GO. La operación cumple todas las reglas de riesgo.")

    # Si CUALQUIERA de las condiciones de arriba falla, vamos al 'else'.
    else:
        print("\n--- Resultado del Checklist ---")
        print("NO GO. La operación NO cumple las reglas de riesgo.")
        # Podemos añadir detalles para saber por qué falló
        if porcentage_de_riesgo > 2:
            print(f"- Motivo: El riesgo ({porcentage_de_riesgo:.2f}%) supera el límite del 2%.")
        if tendencia != 'si':
            print("- Motivo: La tendencia principal no está a favor.")
        if stop_loss >= precio_de_entrada:
            print("- Motivo: El stop-loss no es válido para una operación en largo.")

except ValueError:
    print('Error: El capital y los precios deben ser valores numéricos.')
except ZeroDivisionError:
    print('Error: El capital total no puede ser cero.')
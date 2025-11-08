portafolio = {'AAPL': 10, 'GOOG': 5}

try:
    ticker = input('Ingrese el ticker deseado: ')
    numero = int(input(f'Ingrese la cantidad deseada para {ticker}: '))

    # --- LÍNEA CLAVE AÑADIDA ---
    # Aquí es donde intentamos la actualización.
    # Esta línea puede causar un KeyError si el ticker no existe.
    portafolio[ticker] = numero

except ValueError:
    print('Error: Aquí debes poner solo un número entero.')
except KeyError:
    # Ahora este bloque SÍ puede activarse.
    print(f"Error: El ticker '{ticker}' no existe en el portfolio.")
else:
    # --- MENSAJE CORREGIDO ---
    # Usamos las variables 'ticker' y 'numero' para un mensaje correcto.
    print(f'Éxito: Se actualizó {ticker} a {numero} acciones.')
finally:
    # Este print ahora mostrará el portafolio actualizado (o el original si hubo error).
    print(f"Estado final del portafolio: {portafolio}")

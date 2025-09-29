def imprimer_ticket(**detalles_de_operacion: dict):
    detalles_de_operacion = {'Ticker':'NVDA', 'Tipo':'Compra','Cantidad': 50 ,'Precio': 125.50}
    detalles_de_operacion_2= {'Par':'EURUSD', 'Lotes':0.1 , 'Direccion': 'venta'}
    detalles_de_operacion.update(detalles_de_operacion_2)
    for clave, valor in detalles_de_operacion.items():
        print(detalles_de_operacion)
print(imprimer_ticket())


def imprimer_ticket(**detalles_de_operacion: dict):
    # Ya no creamos diccionarios aquí.
    # 'detalles_de_operacion' ya contiene los datos que se pasaron al llamar la función.

    print("--- TICKET DE OPERACIÓN ---")

    # El bucle es perfecto, solo cambiamos el print.
    for clave, valor in detalles_de_operacion.items():
        # Imprimimos la clave y el valor de ESTA vuelta del bucle
        print(f"- {clave.title()}: {valor}")

    print("---------------------------")


# --- ASÍ SE LLAMA LA FUNCIÓN CORREGIDA ---
# Le pasamos los datos como argumentos con nombre
imprimer_ticket(ticker='NVDA', tipo='Compra', cantidad=50, precio=125.50)

imprimer_ticket(par='EUR/USD', lotes=0.1, direccion='Venta')
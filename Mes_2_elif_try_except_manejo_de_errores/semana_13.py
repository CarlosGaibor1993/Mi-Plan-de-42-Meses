with open('../Carpeta Data/listas_compras.txt', 'r') as f:
    for indice , texto in enumerate(f):
        print(f"{indice + 1}: {texto.strip()}")

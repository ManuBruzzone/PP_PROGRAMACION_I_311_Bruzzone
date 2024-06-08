def crear_id(path: str) -> int:
    """Lee un numero de ID unico desde un archivo, lo incrementa en 1 y lo sobreescribe en el archivo.
    Si el archivo no existe, crea uno nuevo con el numero de ID inicializado en 1.

    Args:
        path (str): Ruta del archivo.

    Returns:
        int: Numero de identificacion unico.
    """
    try:
        with open(path, 'r') as archivo:
            contenido = archivo.read()
            numero_id = int(contenido) + 1
    except:
        print(f'El archivo {path} no existe. Se ha creado uno nuevo con el ID 1.')
        numero_id = 1
    
    with open(path, 'w') as archivo:
        archivo.write(str(numero_id))

    return numero_id
def crear_id(path):
    try:
       with open(path, 'r+') as archivo:
            contenido = archivo.read()
            numero_id = int(contenido)
            archivo.seek(0)  
            archivo.write(str(numero_id + 1))

    except:
        print('Se genero el archivo id con el id 1!.')
        numero_id = 1
        with open(path, 'w') as archivo:
            archivo.write('1')

    return numero_id
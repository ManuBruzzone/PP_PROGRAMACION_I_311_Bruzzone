import re

def crear_id(path: str, lista: list) -> int:
    """Lee un numero de ID unico desde un archivo, lo incrementa en 1 y lo sobreescribe en el archivo.
    Si el archivo no existe, crea uno nuevo con el numero de ID inicializado en la longitud de la lista .

    Args:
        path (str): Ruta del archivo.
        lista (list): Lista con los pacientes

    Returns:
        int: Numero de identificacion unico.
    """
    cantidad_inciial = len(lista) + 1
    try:
        with open(path, 'r') as archivo:
            contenido = archivo.read()
            numero_id = int(contenido) + 1
    except:
        print(f'El archivo {path} no existe. Se ha creado uno nuevo con el ID {cantidad_inciial}.')
        numero_id = cantidad_inciial 
    
    with open(path, 'w') as archivo:
        archivo.write(str(numero_id))

    return numero_id


def cargar_lista(path: str) -> list:
    """El cargar lista se encarga de generar uno por uno los diferentes pacientes dentro del archivo. Al iniciar se saltea la primera linea para evitar copiar la cabecera.

    Args:
        path (str): Direccion del archivo

    Returns:
        list: Retorna la lista de diccionarios con los diferentes pacientes
    """
    lista = []

    with open(path, 'r') as archivo:
        archivo.readline()

        for line in archivo:
            lectura = re.split(',|\n', line)
            paciente = {}
            paciente['id'] = lectura[0]
            paciente['id'] = int(paciente['id'])
            paciente['nombre'] = lectura[1]
            paciente['apellido'] = lectura[2]
            paciente['edad'] = lectura[3]
            paciente['edad'] = int(paciente['edad'])
            paciente['altura'] = lectura[4]
            paciente['altura'] = int(paciente['altura'])
            paciente['peso'] = lectura[5]
            paciente['peso'] = float(paciente['peso'])
            paciente['dni'] = lectura[6]
            paciente['grupo sanguineo'] = lectura[7]
            lista.append(paciente)

    return lista

def guardar_lista(path: str, lista: list) -> bool:
    """Guarda la lista utilizada durante el recorrido, ademas agrega la cabecera ignorada en la funcion "cargar_lista"

    Args:
        path (str): Direccion del archivo
        lista (list): Lista de diccionarios utilizada

    Returns:
        bool: Devuelve True para poder informar por fuera que el archivo se guardo
    """
    with open(path, 'w') as archivo:
        cabecera = 'id,nombre,apellido,edad,altura,peso,dni,grupo sanguineo'
        archivo.write(f'{cabecera}\n')
        for paciente in lista:
            escribir = ','.join([str(paciente['id']), paciente['nombre'], paciente['apellido'], str(paciente['edad']), str(paciente['altura']), str(paciente['peso']), paciente['dni'], paciente['grupo sanguineo']])
            archivo.write(f'{escribir}\n')
        
    return True
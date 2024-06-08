from os import system
from Package_Input.Input import *

#Create
def crear_paciente(id: int, nombre: str, apellido: str, edad: int, altura: int, peso: float, dni: int, grupo_sanguineo: str) -> dict:
    """Crea un diccionario con la información de un paciente.

    Args:
        id (int): ID unico del paciente.
        nombre (str): Nombre del paciente.
        apellido (str): Apellido del paciente.
        edad (int): Edad del paciente.
        altura (int): Altura del paciente.
        peso (float): Peso del paciente.
        dni (int): DNI del paciente.
        grupo sanguineo (str): Grupo sanguineo del paciente.

    Returns:
        dict: Diccionario con la información del paciente.
    """

    diccionario_paciente = {
        'id': id,
        'nombre' : nombre,
        'apellido' : apellido,
        'edad' : edad,
        'altura': altura,
        'peso': peso,
        'dni': dni,
        'grupo sanguineo': grupo_sanguineo,
    }

    return diccionario_paciente


def ingresar_paciente_lista(lista_pacientes: list,id: int):
    """Solicita informacion del paciente al usuario y agrega el nuevo paciente a la lista.

    Args:
        lista_pacientes (list): Lista que contiene los diferentes pacientes.
        id (int): ID unico del paciente.

    En esta funcion le solicitamos al usario que ingrese los diferentes datos necesarios para poder crear un "paciente". Al mismo tiempo esos datos se validan utilizando funciones propias de validacion.
    En caso que todos los datos sean correctos, creara el paciente utilizando la funcion "crear_paciente" y se agregara a la lista "lista_pacientes". Si algun dato falla no se agregara el paciente y se redireccionara al menu principal. 
    """
    nombre = get_string('Ingrese el nombre: ','Re-Ingrese el nombre: ',1, 20, 3)
    system('cls')
    apellido = get_string('Ingrese el apellido: ','Re-Ingrese el apellido: ',1, 20, 3)
    system('cls')
    edad = get_int('Ingrese la edad: ','Re-Ingrese la edad: ',1, 120, 3)
    system('cls')
    altura = get_int('Ingrese la altura: ','Re-Ingrese la altura: ', 30, 230, 3)
    system('cls')
    peso = get_float('Ingrese el peso: ','Re-Ingrese el peso: ', 10, 300, 3)
    system('cls')
    dni = get_int('Ingrese el DNI: ','Re-Ingrese el DNI: ', 4000000, 99999999, 3)
    system('cls')
    grupo_sanguineo = get_string_grupo_sanguineo('Ingrese el grupo sanguineo: ','Re-Ingrese el grupo sanguineo: ', 2, 3, 3)
    system('cls')
    
    if nombre != None and apellido != None and edad != None and altura != None and peso != None and dni != None and grupo_sanguineo != None:

        diccionario_pacientes = crear_paciente(id, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo)

        lista_pacientes.append(diccionario_pacientes)

        print(f'Se creo correctamente el paciente con DNI: {dni}\n\nDATOS CARGADOS:\nNombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nAltura: {altura}\nPeso: {peso}\nDNI: {dni}\nGrupo Sanguineo: {grupo_sanguineo}')
    else:
        print('No se pudo cargar el paciente: uno o más datos no son válidos.\nSi desea volver a intentar re ingrese la opcion "1" en el menu principal')

#Read
def mostrar_un_paciente(un_paciente: dict):
    """Imprime los detalles de un paciente en formato de tabla.

    Args:
        un_paciente (dict): un Diccionario que contiene la información del paciente.
    """
    print(f'| {un_paciente['nombre']:>12} | {un_paciente['apellido']:>12} | {un_paciente['edad']:>12} | {un_paciente['altura']:>12} cm | {un_paciente['peso']:>12} kg | {un_paciente['dni']:>12} | {un_paciente['grupo sanguineo']:>25} |')


def mostrar_todos_los_paciente(lista_pacientes: list[dict]):
    """Imprime los detalles de todos los pacientes en formato de tabla llamando a la funcion "mostrar_un_paciente".

    Args:
        lista_pacientes (list[dict]): Lista que contiene los diccionarios de los pacientes.
    """
    encabezado = f"{'*'*125}\n| {'Nombre':>12} | {'Apellido':>12} | {'Edad':>12} | {'Altura':>12}    | {'Peso':>12}    | {'DNI':>12} | {'Grupo Sanguineo':>25} |\n{'-'*125}"
    print(encabezado)
    for paciente in lista_pacientes:
        mostrar_un_paciente(paciente)
    print(f"{'-'*125}")


def buscar_paciente(lista_pacientes: list[dict], dni:int):
    """Busca un paciente por su número de DNI y muestra sus detalles llamando a la funcion "mostrar_un_pacientes".

    Args:
        lista_pacientes (list[dict]): Lista que contiene los diccionarios de los pacientes.
        dni (int): DNI del paciente.
    """
    for paciente in lista_pacientes:
        if dni == paciente['dni']:
            encabezado = f"{'*'*125}\n| {'Nombre':>12} | {'Apellido':>12} | {'Edad':>12} | {'Altura':>12}    | {'Peso':>12}    | {'DNI':>12} | {'Grupo Sanguineo':>25} |\n{'-'*125}"
            print(encabezado)
            mostrar_un_paciente(paciente)
        else:
            print(f'No existe el paciente con DNI {dni}')


def calcular_promedio(lista_pacientes: list[dict]):
    """Calcula el promedio de edad, altura o peso de los pacientes.

    Args:
        lista_pacientes (list[dict]): Lista que contiene los diccionarios de los pacientes.
    """
    edad = 0
    altura = 0
    peso = 0
    cantidad_pacientes = len(lista_pacientes)
    for paciente in lista_pacientes:
        edad += paciente['edad']
        altura += paciente['altura']
        peso += paciente['peso']

    bandera_seguir = True
    while bandera_seguir == True:
        opcion = input('Elija el dato sobre el cual desea saber el promedio.\n1. Edad\n2. altura\n3. Peso\n4. Salir\nAqui su respuesta: ')
        system('cls')
        match opcion:
            case '1':
                variable = edad
                mensaje = 'La edad'
            case '2':
                variable = altura
                mensaje = 'La altura'
            case '3':
                variable = peso
                mensaje = 'El peso'
            case '4':
                bandera_seguir = False
                break
            case _:
                print('Ingrese una opcion valida!')

        calcular_promedio = variable / cantidad_pacientes

        print(f'{mensaje} es promedio es: {calcular_promedio}')
        system('pause')
        system('cls')


def ordenar_pacientes(lista_pacientes: list[dict]):
    """Ordena la lista de pacientes según los criterios especificados por el usuario. Se le consulta al usuario sobre sus preferencias y se realiza el llamada a la funcion "burbujeo" para ordenar.

    Args:
        lista_pacientes (list[dict]): Lista que contiene los diccionarios de los pacientes.
    """
    bandera_seguir = True
    lista_pacientes_temporal = []
    while bandera_seguir == True:
        opcion = input('Ordene la lista a su gusto!\nOrdenar por:\n1. Nombre\n2. Apellido\n3. Altura\n4. Grupo Sanguineo\n5. Salir\nAqui su respuesta: ')
        system('cls')
        match opcion:
            case '1':
                variable = 'nombre'
            case '2':
                variable = 'apellido'
            case '3':
                variable = 'altura'
            case '4':
                variable = 'grupo sanguineo'
            case '5':
                bandera_seguir = False
                break
        
        opcion = input('Ordene la lista a su gusto!\n1. Ordenar de manera ascendente\n2. Ordenar de manera descendente\n3. atras\nAqui su respuesta: ')       
        system('cls')
        match opcion:
            case '1':
                ordenamiento = 'ascendente'
            case '2':
                ordenamiento = 'descendente'
            case '3':
                break
        
        lista_pacientes_temporal = lista_pacientes
        burbujeo(lista_pacientes_temporal, variable, ordenamiento)
        mostrar_todos_los_paciente(lista_pacientes_temporal)

        opcion = input('\nAsi es como quedaria la lista con sus preferencias de ordenamiento. Desea guardar los cambios?\n1. Si\n2. No\nAqui su respuesta: ')
        system('cls')
        match opcion:
            case '1':
                lista_pacientes = lista_pacientes_temporal
                print('Cambios guardados!')
            case '2':
                print('No se guardaron los cambios.')

        system('pause')
        system('cls')


def burbujeo(lista: list[dict], variable: str, ordenamiento:str):
    """Ordena una lista de diccionarios de pacientes utilizando el algoritmo de ordenamiento burbuja.

    Args:
        lista (list): Lista que contiene los diccionarios de los pacientes a ordenar.
        variable (str): Variable por la cual se ordenarán los pacientes (por ejemplo, 'nombre', 'apellido', etc).
        ordenamiento (str): Dirección del ordenamiento ('ascendente' o 'descendente').

    Returns:
        list: Lista de pacientes ordenada.
    """

    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if ordenamiento == 'ascendente':
                if lista[j][variable] > lista[j + 1][variable]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                if lista[j][variable] < lista[j + 1][variable]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

#Update
def modificar_paciente(lista_pacientes: list[dict], dni: int):
    """Modifica los datos de un paciente en la lista de pacientes consultando con el usuario sobre sus preferencias.

    Args:
        lista_pacientes (list[dict]): Lista que contiene los diccionarios de los pacientes.
        dni (int): DNI del paciente que se desea modificar.
    """
    for paciente in lista_pacientes:
        if dni == paciente['dni']:
            paciente_temporal = paciente
            cambios_realizados = []
            bandera_seguir = True
            while bandera_seguir == True:
                system('cls')
                opcion = input('Elija el dato a modificar\n1. Nombre\n2. Apellido\n3. Dni\n4. Edad\n5. Altura\n6. Peso\n7. Grupo Sanguineo\n\n8. Salir y guardar\n9. Salir sin guardar\nAqui su respuesta: ')
                system('cls')
                match opcion:
                    case '1':
                        nuevo_nombre = get_string('Ingrese el nombre nuevo: ','Re-Ingrese el nombre nuevo: ',1, 20, 3)
                        cambios_realizados.append(f'Nombre cambiado de {paciente_temporal['nombre']} a {nuevo_nombre}')
                        paciente_temporal['nombre'] = nuevo_nombre
                    case '2':
                        nuevo_apellido = get_string('Ingrese el apellido nuevo: ','Re-Ingrese el apellido nuevo: ',1, 20, 3)
                        cambios_realizados.append(f'Apellido cambiado de {paciente_temporal['apellido']} a {nuevo_apellido}')
                        paciente_temporal['apellido'] = nuevo_apellido
                    case '3':
                        nuevo_dni = get_int('Ingrese el DNI nuevo: ','Re-Ingrese el DNI nuevo: ', 4000000, 99999999, 3)
                        cambios_realizados.append(f'DNI cambiado de {paciente_temporal['dni']} a {nuevo_dni}')
                        paciente_temporal['DNI'] = nuevo_dni
                    case '4':
                        nueva_edad = get_int('Ingrese la edad nueva: ','Re-Ingrese la edad nueva: ',1, 120, 3)
                        cambios_realizados.append(f'Edad cambiada de {paciente_temporal['edad']} a {nueva_edad}')
                        paciente_temporal['edad'] = nueva_edad
                    case '5':
                        nueva_altura = get_int('Ingrese la altura nueva: ','Re-Ingrese la altura nueva: ', 30, 230, 3)
                        cambios_realizados.append(f'Altura cambiada de {paciente_temporal['altura']} a {nueva_altura}')
                        paciente_temporal['altura'] = nueva_altura
                    case '6':
                        nuevo_peso = get_float('Ingrese el peso nuevo: ','Re-Ingrese el peso nuevo: ', 10, 300, 3)
                        cambios_realizados.append(f'Peso cambiado de {paciente_temporal['peso']} a {nuevo_peso}')
                        paciente_temporal['peso'] = nuevo_peso
                    case '7':
                        nuevo_grupo_sanguineo = get_string_grupo_sanguineo('Ingrese el grupo sanguineo nuevo: ','Re-Ingrese el grupo sanguineo nuevo: ', 2, 3, 3)
                        cambios_realizados.append(f'Grupo sanguineo cambiado de {paciente_temporal['grupo sanguineo']} a {nuevo_grupo_sanguineo}')
                        paciente_temporal['grupo sanguineo'] = nuevo_grupo_sanguineo
                    case '8':
                        paciente = paciente_temporal
                        bandera_seguir = False
                        print('\nOperacion guardada con exito!')
                        if cambios_realizados:
                            print('Cambios realizados:')
                            for cambio in cambios_realizados:
                                print(cambio)
                        else:
                            print('No se realizaron cambios.')
                        break
                    case '9':
                        bandera_seguir = False
                        print('Operacion cancelada!')
                        break
                    case _:
                        print('Ingrese una opcion valida!')

#Delete
def eliminar_paciente(lista_pacientes: list[dict], dni: int):
    """Elimina un paciente de la lista de pacientes segun su DNI.

    Args:
        lista_pacientes (list[dict]): Lista que contiene los diccionarios de los pacientes.
        dni (int): DNI del paciente que se desea eliminar.
    """
    bandera_seguir = True
    while bandera_seguir:
        opcion = input(f'Esta a un paso de eliminar el paciente {dni}.\nDesea continuar con la operacion? Si/No: ')
        system('cls')
        match opcion:
            case 'Si':
                eliminado = None
                for paciente in lista_pacientes:
                    if dni == paciente['dni']:
                        eliminado = paciente

                if eliminado != None:
                    lista_pacientes.remove(eliminado)
                    print(f'El paciente con DNI {dni} fue eliminado')
                    bandera_seguir = False
                    break

                else:
                    print(f'El paciente con DNI {dni} no existe')

            case 'No':
                bandera_seguir = False
                break
            case _:
                print('Ingrese una opcion valida!')
                system('pause')
                system('cls')
from os import system
from Package_Input.Input import *
from generales import *

def crear_paciente(id: int, nombre: str, apellido: str, edad: int, altura: int, peso: float, dni: str, grupo_sanguineo: str) -> dict:
    """Crea un diccionario con la información de un paciente.

    Args:
        id (int): ID unico del paciente.
        nombre (str): Nombre del paciente.
        apellido (str): Apellido del paciente.
        edad (int): Edad del paciente.
        altura (int): Altura del paciente.
        peso (float): Peso del paciente.
        dni (str): DNI del paciente.
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


def ingresar_paciente_lista(lista_pacientes: list,id: int) -> bool:
    """Solicita informacion del paciente al usuario y agrega el nuevo paciente a la lista.
    En esta funcion le solicitamos al usario que ingrese los diferentes datos necesarios para poder crear un "paciente". Al mismo tiempo esos datos se validan utilizando funciones propias de validacion.
    En caso que todos los datos sean correctos, creara el paciente utilizando la funcion "crear_paciente" y se agregara a la lista "lista_pacientes". Si algun dato falla no se agregara el paciente y se redireccionara al menu principal. 
    

    Args:
        lista_pacientes (list): Lista que contiene los diferentes pacientes.
        id (int): ID unico del paciente.

    Returns:
        bool : En caso de completarse exitosamente el ingreso de paciente retornara True, caso contrario retornara False.
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
    dni = str(dni).zfill(8)
    system('cls')
    grupo_sanguineo = get_string_grupo_sanguineo('Ingrese el grupo sanguineo ( A(-\+) | B(-\+) | AB(-\+) | 0(-\+) ): ','Re-Ingrese el grupo sanguineo: ', 2, 3, 3)
    system('cls')
    
    if nombre != None and apellido != None and edad != None and altura != None and peso != None and dni != None and grupo_sanguineo != None:

        diccionario_pacientes = crear_paciente(id, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo)

        lista_pacientes.append(diccionario_pacientes)

        ingreso_paciente = True

        print(f'Se creo correctamente el paciente con DNI: {dni}\n\nDATOS CARGADOS:\nNombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nAltura: {altura}\nPeso: {peso}\nDNI: {dni}\nGrupo Sanguineo: {grupo_sanguineo}')
    else:
        print('No se pudo cargar el paciente: uno o más datos no son válidos.\nSi desea volver a intentar re ingrese la opcion "1" en el menu principal')

        ingreso_paciente = False

    return ingreso_paciente


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
    print(f"{'*'*125}")


def buscar_paciente(lista_pacientes: list[dict], dni:str):
    """Busca un paciente por su número de DNI y muestra sus detalles llamando a la funcion "mostrar_un_pacientes".

    Args:
        lista_pacientes (list[dict]): Lista que contiene los diccionarios de los pacientes.
        dni (str): DNI del paciente.
    """
    for paciente in lista_pacientes:
        if dni == paciente['dni']:
            encabezado = f"{'*'*125}\n| {'Nombre':>12} | {'Apellido':>12} | {'Edad':>12} | {'Altura':>12}    | {'Peso':>12}    | {'DNI':>12} | {'Grupo Sanguineo':>25} |\n{'-'*125}"
            print(encabezado)
            mostrar_un_paciente(paciente)
            print(f"{'*'*125}")
        else:
            print(f'No se existe el paciente con DNI {dni}')


def calcular_promedio_pacientes(lista_pacientes: list[dict]):
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
        variable = None
        opcion = input('Elija el dato sobre el cual desea saber el promedio.\n1. Edad\n2. altura\n3. Peso\n4. Salir\nAqui su respuesta: ')
        system('cls')
        match opcion:
            case '1':
                variable = edad
                mensaje = 'edad'
            case '2':
                variable = altura
                mensaje = 'altura'
            case '3':
                variable = peso
                mensaje = 'peso'
            case '4':
                bandera_seguir = False
                break
            case _:
                print('Ingrese una opcion valida la proxima!')

        if variable == None:
            break

        promedio = calcular_promedio(variable, cantidad_pacientes)

        print(f'El promedio de {mensaje} es de: {promedio}')
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
        variable_valida = False
        while variable_valida == False:
            opcion = input('Ordene la lista a su gusto!\nOrdenar por:\n1. Nombre\n2. Apellido\n3. Altura\n4. Grupo Sanguineo\n5. Salir\nAqui su respuesta: ')
            system('cls')
            match opcion:
                case '1':
                    variable = 'nombre'
                    variable_valida = True
                case '2':
                    variable = 'apellido'
                    variable_valida = True
                case '3':
                    variable = 'altura'
                    variable_valida = True
                case '4':
                    variable = 'grupo sanguineo'
                    variable_valida = True
                case '5':
                    bandera_seguir = False
                    variable_valida = True
                    break
                case _:
                    print('Ingrese una opcion valida!')
                    system('pause')
                    system('cls')

        if bandera_seguir == False:
            break

        ordenamiento_valido = False
        while ordenamiento_valido == False: 
            opcion = input('Ordene la lista a su gusto!\n1. Ordenar de manera ascendente\n2. Ordenar de manera descendente\nAqui su respuesta: ')       
            system('cls')
            match opcion:
                case '1':
                    ordenamiento = 'ascendente'
                    ordenamiento_valido = True
                case '2':
                    ordenamiento = 'descendente'
                    ordenamiento_valido = True
                case _:
                    print('Ingrese una opcion valida!')
                    system('pause')
                    system('cls')
        
        lista_pacientes_temporal = lista_pacientes
        burbujeo(lista_pacientes_temporal, variable, ordenamiento)
        mostrar_todos_los_paciente(lista_pacientes_temporal)

        opcion = input(f'\nAsi es como quedaria la lista ordenandola por {variable} de manera {ordenamiento}. Desea guardar los cambios?\n1. Si\n2. No\nAqui su respuesta: ')
        system('cls')
        match opcion:
            case '1':
                lista_pacientes = lista_pacientes_temporal
                print('Cambios guardados!')
            case '2':
                print('No se guardaron los cambios.')

        system('pause')
        system('cls')



def modificar_paciente(lista_pacientes: list[dict], dni: str):
    """Modifica los datos de un paciente en la lista de pacientes consultando con el usuario sobre sus preferencias.

    Args:
        lista_pacientes (list[dict]): Lista que contiene los diccionarios de los pacientes.
        dni (str): DNI del paciente que se desea modificar.
    """
    for paciente in lista_pacientes:
        if dni == paciente['dni']:
            original_nombre = paciente['nombre']
            original_apellido = paciente['apellido']
            original_dni = paciente['dni']
            original_edad = paciente['edad']
            original_altura = paciente['altura']
            original_peso = paciente['peso']
            original_grupo_sanguineo = paciente['grupo sanguineo']
            cambios_realizados = []
            bandera_seguir = True
            while bandera_seguir == True:
                system('cls')
                opcion = input('Elija el dato a modificar\n1. Nombre\n2. Apellido\n3. Dni\n4. Edad\n5. Altura\n6. Peso\n7. Grupo Sanguineo\n\n8. SALIR Y GUARDAR\n9. SALIR SIN GUARDAR\nAqui su respuesta: ')
                system('cls')
                match opcion:
                    case '1':
                        nuevo_nombre = get_string('Ingrese el nombre nuevo: ','Re-Ingrese el nombre nuevo: ',1, 20, 3)
                        if nuevo_nombre != None:
                            cambios_realizados.append(f'Nombre cambiado de {paciente['nombre']} a {nuevo_nombre}')
                            paciente['nombre'] = nuevo_nombre
                        else:
                            system('cls')
                            print('El nombre ingresado no es valido!')
                            system('pause')

                    case '2':
                        nuevo_apellido = get_string('Ingrese el apellido nuevo: ','Re-Ingrese el apellido nuevo: ',1, 20, 3)
                        if nuevo_apellido != None:
                            cambios_realizados.append(f'Apellido cambiado de {paciente['apellido']} a {nuevo_apellido}')
                            paciente['apellido'] = nuevo_apellido
                        else:
                            system('cls')
                            print('El apellido ingresado no es valido!')
                            system('pause')

                    case '3':
                        nuevo_dni = get_int('Ingrese el DNI nuevo: ','Re-Ingrese el DNI nuevo: ', 4000000, 99999999, 3)
                        if nuevo_dni:
                            nuevo_dni = str(nuevo_dni).zfill(8)
                            cambios_realizados.append(f'DNI cambiado de {paciente['dni']} a {nuevo_dni}')
                            paciente['dni'] = nuevo_dni
                        else:
                            system('cls')
                            print('El DNI ingresado no es valido!')
                            system('pause')

                    case '4':
                        nueva_edad = get_int('Ingrese la edad nueva: ','Re-Ingrese la edad nueva: ',1, 120, 3)
                        if nueva_edad != None:                            
                            cambios_realizados.append(f'Edad cambiada de {paciente['edad']} a {nueva_edad}')
                            paciente['edad'] = nueva_edad
                        else:
                            system('cls')
                            print('La edad ingresada no es valida!')
                            system('pause')

                    case '5':
                        nueva_altura = get_int('Ingrese la altura nueva: ','Re-Ingrese la altura nueva: ', 30, 230, 3)
                        if nueva_altura != None:
                            cambios_realizados.append(f'Altura cambiada de {paciente['altura']} a {nueva_altura}')
                            paciente['altura'] = nueva_altura
                        else:
                            system('cls')
                            print('La altura ingresada no es valida!')
                            system('pause')

                    case '6':
                        nuevo_peso = get_float('Ingrese el peso nuevo: ','Re-Ingrese el peso nuevo: ', 10, 300, 3)
                        if nuevo_peso != None:
                            cambios_realizados.append(f'Peso cambiado de {paciente['peso']} a {nuevo_peso}')
                            paciente['peso'] = nuevo_peso
                        else:
                            system('cls')
                            print('El peso ingresado no es valido!')
                            system('pause')

                    case '7':
                        nuevo_grupo_sanguineo = get_string_grupo_sanguineo('Ingrese el grupo sanguineo nuevo: ','Re-Ingrese el grupo sanguineo nuevo: ', 2, 3, 3)
                        if nuevo_grupo_sanguineo != None:
                            cambios_realizados.append(f'Grupo sanguineo cambiado de {paciente['grupo sanguineo']} a {nuevo_grupo_sanguineo}')
                            paciente['grupo sanguineo'] = nuevo_grupo_sanguineo
                        else:
                            system('cls')
                            print('El grupo sanguineo ingresado no es valido!')
                            system('pause')

                    case '8':
                        bandera_seguir = False
                        print('Operacion guardada con exito!')
                        if cambios_realizados:
                            print('\nCambios realizados:')
                            for cambio in cambios_realizados:
                                print(cambio)
                        else:
                            print('No se realizaron cambios.')
                        break

                    case '9':
                        paciente['nombre'] = original_nombre
                        paciente['apellido'] = original_apellido
                        paciente['dni'] = original_dni
                        paciente['edad'] = original_edad
                        paciente['altura'] = original_altura
                        paciente['peso'] = original_peso
                        paciente['grupo sanguineo'] = original_grupo_sanguineo
                        bandera_seguir = False
                        print('Operacion cancelada!')
                        break

        else:
            print(f'No se encontro el paciente con DNI {dni}')


def eliminar_paciente(lista_pacientes: list[dict], dni: str) -> bool:
    """Elimina un paciente de la lista de pacientes segun su DNI.

    Args:
        lista_pacientes (list[dict]): Lista que contiene los diccionarios de los pacientes.
        dni (int): DNI del paciente que se desea eliminar.

    Return:
        bool : Retorna True en caso de que se haya podido eliminar o False en caso de que no se haya podido eliminar.
    """
    bandera_seguir = True
    eliminacion = False
    while bandera_seguir:
        opcion = input(f'Esta a un paso de eliminar el paciente {dni}.\nDesea continuar con la operacion?\n1. Si\n2. No\nAqui su respuesta: ')
        system('cls')
        match opcion:
            case '1':
                eliminado = None
                for paciente in lista_pacientes:
                    if dni == paciente['dni']:
                        eliminado = paciente

                if eliminado != None:
                    lista_pacientes.remove(eliminado)
                    eliminacion = True
                    bandera_seguir = False
                    break

                else:
                    print(f'El paciente con DNI {dni} no existe!')
                    bandera_seguir = False
                    break
            case '2':
                bandera_seguir = False
                break
            case _:
                print('Ingrese una opcion valida!')
                system('pause')
                system('cls')

    return eliminacion
from os import system
from Package_Input.Input import *

#Create
def crear_paciente(id, nombre: str, apellido: str, edad: int, altura: int, peso: float, dni: int, grupo_sanguineo: str):
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
    print(f'| {un_paciente['nombre']:>12} | {un_paciente['apellido']:>12} | {un_paciente['edad']:>12} | {un_paciente['altura']:>12} cm | {un_paciente['peso']:>12} kg | {un_paciente['dni']:>12} | {un_paciente['grupo sanguineo']:>25} |')


def mostrar_todos_los_paciente(lista_paciente: list[dict]):
    for paciente in lista_paciente:
        mostrar_un_paciente(paciente)


def buscar_paciente(lista_pacientes: list[dict], dni:int):
        for paciente in lista_pacientes:
            if dni == paciente['dni']:
                mostrar_un_paciente(paciente)


def calcular_promedio(lista_pacientes):
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
        match opcion:
            case '1':
                system('cls')
                variable = edad
            case '2':
                system('cls')
                variable = altura
            case '3':
                system('cls')
                variable = peso
            case '4':
                bandera_seguir = False
                break
            case _:
                print('Ingrese una opcion valida!')
            
        calcular_promedio =  variable / cantidad_pacientes

        print(f'{variable} promedio es: {calcular_promedio}')


def ordenar_pacientes(lista_pacientes):
    pass


#Update
def modificar_paciente(lista_pacientes: list[dict], dni: int):
    for paciente in lista_pacientes:
        if dni == paciente['dni']:
            bandera_seguir = True
            while bandera_seguir == True:
                opcion = input('Elija el dato a modificar\n1. Nombre\n2. Apellido\n3. Dni\n4. Edad\n5. Altura\n6. Peso\n7. Grupo Sanguineo\n8. Salir\nAqui su respuesta: ')
                match opcion:
                    case '1':
                        nuevo_nombre = get_int('Ingrese el nombre nuevo: ','Re-Ingrese el nombre nuevo: ',1, 20, 3)
                        paciente['nombre'] = nuevo_nombre
                    case '2':
                        nuevo_apellido = get_string('Ingrese el apellido nuevo: ','Re-Ingrese el apellido nuevo: ',1, 20, 3)
                        paciente['apellido'] = nuevo_apellido
                    case '3':
                        nuevo_dni = get_int('Ingrese el DNI nuevo: ','Re-Ingrese el DNI nuevo: ', 4000000, 99999999, 3)
                        paciente['DNI'] = nuevo_dni
                    case '4':
                        nueva_edad = get_int('Ingrese la edad nueva: ','Re-Ingrese la edad nueva: ',1, 120, 3)
                        paciente['edad'] = nueva_edad
                    case '5':
                        nueva_altura = get_int('Ingrese la altura nueva: ','Re-Ingrese la altura nueva: ', 30, 230, 3)
                        paciente['altura'] = nueva_altura
                    case '6':
                        nuevo_peso = get_float('Ingrese el peso nuevo: ','Re-Ingrese el peso nuevo: ', 10, 300, 3)
                        paciente['peso'] = nuevo_peso
                    case '7':
                        nuevo_grupo_sanguineo = get_string_grupo_sanguineo('Ingrese el grupo sanguineo nuevo: ','Re-Ingrese el grupo sanguineo nuevo: ', 2, 3, 3)
                        paciente['grupo sanguineo'] = nuevo_grupo_sanguineo
                    case '8':
                        bandera_seguir = False
                        print('Operacion cancelada!')
                        break
                
                continuar = input(f'Desea seguir modificando la informacion del paciente con id {paciente['id']}? (si/no)\nSu respuesta: ')
                if continuar == 'no':
                    break


#Delete
def eliminar_paciente(lista_pacientes, dni):
    bandera_seguir = True
    while bandera_seguir:
        opcion = input(f'Esta a un paso de eliminar el paciente {dni}.\nDesea continuar con la operacion? Si/No: ')    
        match opcion:
            case 'Si':
                eliminado = None
                for paciente in lista_pacientes:
                    if dni == paciente['dni']:
                        eliminado = paciente
                        break

                if eliminado != None:
                    lista_pacientes.remove(eliminado)

            case 'No':
                bandera_seguir = False
                break
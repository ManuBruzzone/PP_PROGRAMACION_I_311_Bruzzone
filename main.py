from os import system
from pacientes import *
from archivos import *

def mostrar_menu():
    """Muestra un menu de opciones al usuario y devuelve la opción seleccionada.

    Returns:
        str: La opcion seleccionada por el usuario.
    """
    opcion = input('---MENU---\n1. Dar de alta\n2. Modificar\n3. Eliminar\n4. Mostrar todos\n5. Ordenar pacientes\n6. Buscar paciente por DNI\n7. Calcular promedio\n8. Salir\nElija una opcion: ')
    return opcion

path_generador_id = './Generador_ID'

lista_pacientes = []

system('cls')
bandera_ingreso = False
while True:
    opcion = mostrar_menu()
    system('cls')
    match opcion:
        case '1':

            id = crear_id(path_generador_id)
            ingresar_paciente_lista(lista_pacientes, id)

            bandera_ingreso = True

        case '2':
            if bandera_ingreso == True:

                dni = int(input('Ingrese el DNI del paciente a modificar: '))
                modificar_paciente(lista_pacientes, dni)

        case '3':
            if bandera_ingreso == True:

                dni = int(input('Ingrese el DNI del paciente a Eliminar: '))
                eliminar_paciente(lista_pacientes, dni)

        case '4':
            if bandera_ingreso == True:

                mostrar_todos_los_paciente(lista_pacientes)

        case '5':
            if bandera_ingreso == True:

                ordenar_pacientes(lista_pacientes)
             
        case '6':
            if bandera_ingreso == True:

                dni = int(input('Ingrese el DNI del paciente del cual desea informacion: ')) 
                buscar_paciente(lista_pacientes, dni)

        case '7':
            if bandera_ingreso == True:
                
                calcular_promedio(lista_pacientes)

        case '8':
            break

        case _:
            system('cls')
            print('Ingrese una opcion valida!')

    system('pause')
    system('cls')
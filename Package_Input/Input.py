from Package_Input.Validate import *

def get_int (mensaje: str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> int|None:
    
    cantidad_reintentos = 0

    numero_entero_final = None

    while cantidad_reintentos < reintentos:
        try:
            numero = input(mensaje)
            numero = int(numero)

            if validate_number(numero, minimo, maximo):
                numero_entero_final = numero
                break

            else:
                cantidad_reintentos += 1
                if cantidad_reintentos < reintentos:
                    print(f'{mensaje_error}{cantidad_reintentos}/{reintentos}')
        except:
            cantidad_reintentos += 1
            if cantidad_reintentos < reintentos:
                print(f'{mensaje_error} {cantidad_reintentos}/{reintentos}')

    return numero_entero_final


def get_float (mensaje: str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> float|None:

    cantidad_reintentos = 0

    numero_flotante_final = None

    while cantidad_reintentos < reintentos:
        numero = input(mensaje)
        numero = float(numero)

        if validate_number(numero, minimo, maximo):
            numero_flotante_final = numero
            break

        else:
            cantidad_reintentos += 1
            if cantidad_reintentos < reintentos:
                print(f'{mensaje_error}{cantidad_reintentos}/{reintentos}')

    return numero_flotante_final


def get_string(mensaje: str, mensaje_error: str, longitud_minima: int, longitud_maxima: int, reintentos: int) -> str|None:
    
    cantidad_reintentos = 0

    cadena_final = None

    while cantidad_reintentos < reintentos:
        cadena = input(mensaje)

        if validate_length(cadena, longitud_minima, longitud_maxima):
            cadena_final = cadena
            break

        else:
            cantidad_reintentos += 1
            print(f'{mensaje_error}{cantidad_reintentos}/{reintentos}')


    return cadena_final

def get_string_puesto(mensaje: str, mensaje_error: str, longitud_minima: int, longitud_maxima: int, reintentos: int) -> str|None:

    cantidad_reintentos = 0

    cadena_final = None

    while cantidad_reintentos < reintentos:
        cadena = input(mensaje)

        if validate_length(cadena, longitud_minima, longitud_maxima) and validate_puesto(cadena):
            cadena_final = cadena
            break

        else:
            cantidad_reintentos += 1
            print(f'{mensaje_error}{cantidad_reintentos}/{reintentos}')


    return cadena_final
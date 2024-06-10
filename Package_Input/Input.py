from Package_Input.Validate import *

def get_int (mensaje: str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> int|None:
    """Solicita al usuario un numero entero dentro de un rango especifico, con un numero limitado de reintentos.

    Args:
        mensaje (str): Mensaje mostrado al usuario para solicitar el número.
        mensaje_error (str): Mensaje de error mostrado al usuario en caso de entrada fallida.
        minimo (int): Valor minimo aceptable para el número.
        maximo (int): Valor maximo aceptable para el número.
        reintentos (int): Numero maximo de reintentos permitidos en caso de entrada invalida.

    Returns:
        int | None: El numero entero valido ingresado por el usuario o None si se excedieron los reintentos.
    """
    
    cantidad_reintentos = 0

    numero_entero_final = None

    while cantidad_reintentos < reintentos:
        try:
            numero = input(mensaje).strip()
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
    """Solicita al usuario un numero flotante dentro de un rango especifico, con un numero limitado de reintentos.

    Args:
        mensaje (str): Mensaje mostrado al usuario para solicitar el número.
        mensaje_error (str): Mensaje de error mostrado al usuario en caso de entrada fallida.
        minimo (int): Valor minimo aceptable para el número.
        maximo (int): Valor maximo aceptable para el número.
        reintentos (int): Numero maximo de reintentos permitidos en caso de entrada invalida.

    Returns:
        float | None: El numero flotante valido ingresado por el usuario o None si se excedieron los reintentos.
    """

    cantidad_reintentos = 0

    numero_flotante_final = None

    while cantidad_reintentos < reintentos:
        try:
            numero = input(mensaje).strip()
            numero = float(numero)

            if validate_number(numero, minimo, maximo):
                numero_flotante_final = numero
                break

            else:
                cantidad_reintentos += 1
                if cantidad_reintentos < reintentos:
                    print(f'{mensaje_error}{cantidad_reintentos}/{reintentos}')

        except:
            cantidad_reintentos += 1
            if cantidad_reintentos < reintentos:
                print(f'{mensaje_error} {cantidad_reintentos}/{reintentos}')

    return numero_flotante_final


def get_string(mensaje: str, mensaje_error: str, longitud_minima: int, longitud_maxima: int, reintentos: int) -> str|None:
    """Solicita al usuario una cadena de texto dentro de una longitud especifica, permitiendo un numero limitado de reintentos.

    Args:
        mensaje (str): Mensaje mostrado al usuario para solicitar la cadena de texto.
        mensaje_error (str): Mensaje de error mostrado al usuario en caso de entrada invalida.
        longitud_minima (int): Longitud minima aceptable para la cadena de texto.
        longitud_maxima (int): Longitud maxima aceptable para la cadena de texto.
        reintentos (int): Numero maximo de reintentos permitidos en caso de entrada invalida.

    Returns:
        str | None: La cadena de texto valida ingresada por el usuario o None si se excedieron los reintentos.
    """
    
    cantidad_reintentos = 0

    cadena_final = None

    while cantidad_reintentos < reintentos:
        cadena = input(mensaje).strip()

        if validate_len(cadena, longitud_minima, longitud_maxima) and cadena.isalpha():
            cadena_final = cadena.capitalize()
            break

        else:
            cantidad_reintentos += 1
            print(f'{mensaje_error}{cantidad_reintentos}/{reintentos}')

    return cadena_final


def get_string_grupo_sanguineo(mensaje: str, mensaje_error: str, longitud_minima: int, longitud_maxima: int, reintentos: int) -> str|None:
    """Solicita al usuario una cadena de texto correspondiente a un grupo sanguineo, validando su longitud y formato, con un numero limitado de reintentos.

    Args:
        mensaje (str): Mensaje mostrado al usuario para solicitar la cadena de texto.
        mensaje_error (str): Mensaje de error mostrado al usuario en caso de entrada invalida.
        longitud_minima (int): Longitud minima aceptable para la cadena de texto.
        longitud_maxima (int): Longitud maxima aceptable para la cadena de texto.
        reintentos (int): Numero máximo de reintentos permitidos en caso de entrada invalida.

    Returns:
        str | None: La cadena de texto valida ingresada por el usuario o None si se excedieron los reintentos.
    """

    cantidad_reintentos = 0

    cadena_final = None

    while cantidad_reintentos < reintentos:
        cadena = input(mensaje).strip()
        cadena = cadena.capitalize()

        if validate_len(cadena, longitud_minima, longitud_maxima) and validate_grupo_sanguineo(cadena):
            cadena_final = cadena
            break

        else:
            cantidad_reintentos += 1
            print(f'{mensaje_error}{cantidad_reintentos}/{reintentos}')

    return cadena_final
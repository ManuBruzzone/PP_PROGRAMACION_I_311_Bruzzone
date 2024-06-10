def validate_number(numero: float|int, minimo: int, maximo: int) -> bool:
    """Valida que un numero este dentro de un rango especifico.

    Args:
        numero (float|int): El número a validar.
        minimo (int): El valor minimo aceptable.
        maximo (int): El valor maximo aceptable.

    Returns:
        bool: True si el numero esta dentro del rango, False en caso contrario.
    """
    
    validacion = False

    if numero >= minimo and numero <= maximo:
        
        validacion = True

    return validacion


def validate_len(cadena: str, len_minima: int, len_maxima: int) -> bool:
    """Valida que la longitud de una cadena este dentro de los limites especificados.

    Args:
        cadena (str): La cadena de texto a validar.
        len_minima (int): La longitud minima aceptable.
        len_maxima (int): La longitud maxima aceptable.

    Returns:
        bool: True si la longitud de la cadena está dentro de los límites, False en caso contrario.
    """
    validacion = False

    longitud = len(cadena)

    if  longitud >= len_minima and longitud <= len_maxima:
        
        validacion = True

    return validacion


def validate_grupo_sanguineo(cadena: str) -> bool:
    """Valida que una cadena corresponda a un grupo sanguineo valido.

    Args:
        cadena (str): La cadena de texto a validar.

    Returns:
        bool: True si la cadena corresponde a un grupo sanguineo válido, False en caso contrario.
    """
    validacion = False

    puestos_validos = {'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', '0+', '0-'}
    for puesto in puestos_validos:
        if cadena == puesto:
            validacion = True 
            break

    return validacion
def validate_number(numero: float, minimo: int, maximo: int) -> bool:
    
    validacion = False

    if numero >= minimo and numero <= maximo:
        
        validacion = True

    return validacion


def validate_len(cadena: str, len_minima: int, len_maxima: int) -> bool:
    
    validacion = False

    longitud = len(cadena)

    if  longitud >= len_minima and longitud <= len_maxima:
        
        validacion = True

    return validacion


def validate_ishalpha(cadena: str):
    validacion = False

    if cadena.isalpha():

        validacion = True

    return validacion


def validate_grupo_sanguineo(cadena: str) -> bool:

    validacion = False

    puestos_validos = {'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'}
    for puesto in puestos_validos:
        if cadena == puesto:
            validacion = True 
            break

    return validacion
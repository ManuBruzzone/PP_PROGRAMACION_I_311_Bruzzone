def validate_number(numero: float, minimo: int, maximo: int) -> bool:
    
    validacion = False

    if numero >= minimo and numero <= maximo:
        
        validacion = True

    return validacion

def validate_length(cadena: str, len_minima: int, len_maxima: int) -> bool:
    
    validacion = False

    longitud = len(cadena)

    if  longitud >= len_minima and longitud <= len_maxima and cadena.isalpha():
        
        validacion = True

    return validacion

def validate_puesto(cadena: str) -> bool:

    validacion = False

    puestos_validos = {"Gerente", "Supervisor", "Analista", "Encargado", "Asistente"}
    for puesto in puestos_validos:
        if cadena == puesto:
            validacion = True 
            break

    return validacion
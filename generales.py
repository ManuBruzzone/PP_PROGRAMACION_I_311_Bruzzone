def burbujeo(lista: list[dict], variable: str, ordenamiento:str) -> list:
    """Ordena una lista de diccionarios de pacientes utilizando el algoritmo de ordenamiento burbuja.

    Args:
        lista (list): Lista que contiene los diccionarios a ordenar.
        variable (str): Variable por la cual se ordenaran (por ejemplo, 'nombre', 'apellido', etc).
        ordenamiento (str): Direccion del ordenamiento ('ascendente' o 'descendente').

    Returns:
        list: Lista ordenada.
    """

    m = len(lista)

    for i in range(m):
        for j in range(0, m - i - 1):
            if ordenamiento == 'ascendente':
                if lista[j][variable] > lista[j + 1][variable]:
                    lista_temporal = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = lista_temporal
            else:
                if lista[j][variable] < lista[j + 1][variable]:
                    lista_temporal = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = lista_temporal

    return lista


def calcular_promedio(variable: int|float, cantidad_calcular: int) -> float:
    """Funcion general que calcula el promedio de la variable recibida.

    Args:
        variable (int | float): Variable recibida de la cual se desea saber el promedio
        cantidad_calcular (int): La cantidad recibida por la cual se dividira la variable

    Returns:
        float: Promedio final
    """

    promedio = variable / cantidad_calcular

    return promedio
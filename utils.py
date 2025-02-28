def validar_numero_positivo(numero):
    if numero <= 0:
        raise ValueError("El número debe ser positivo")
    return numero

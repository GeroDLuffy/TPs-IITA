def redondear(numero):
    parte_decimal = numero - int(numero)
    if parte_decimal >= 0.5:
        return int(numero) + 1
    else:
        return int(numero)

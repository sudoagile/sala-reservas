def verificar_disponibilidad(reservas, nueva):
    for reserva in reservas:
        if reserva["sala"] == nueva["sala"] and reserva["hora"] == nueva["hora"]:
            return False
    return True
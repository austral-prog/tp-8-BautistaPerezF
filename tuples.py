def get_coordinate(record):
    coordenadas = []
    for elements in record:
        coordenadas.append(elements[1])
    return coordenadas


def convert_coordinate(coordinate):
    coordenadas_correctas = []
    for cords in coordinate:
        coordenadas_correctas.append((cords[0], cords[1]))
    return coordenadas_correctas



def create_record(azara_record, rui_record):
    new_tuple = ()
    a, b = azara_record
    d, c, d = rui_record
    if convert_coordinate(b) == c:
        new_tuple = azara_record + rui_record
        return new_tuple
    else:
        return "not a match"

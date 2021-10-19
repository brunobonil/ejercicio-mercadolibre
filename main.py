import re

def isMutant(adn):
    adn_str = ' '.join(adn)
    long = len(adn[0])

    horizontal = re.compile(r'^A{4}|T{4}|C{4}|G{4}$') # Busca coincidencias horizontales
    vertical = re.compile(r'([ACTG])(.{' + re.escape(str(long)) + r'}\1){3}') # Busca coincidencias verticales
    oblicuo_desc = re.compile(r'([ACTG])(.{' + re.escape(str(long + 1)) + r'}\1){3}') # Busca coincidencias en diagonal de izquierda a derecha
    oblicuo_asc = re.compile(r'([ACTG])(.{' + re.escape(str(long - 1)) + r'}\1){3}') # Busca coincidencias en diagonal de derecha a izquierda

    # Creo una lista con las expresiones regulares
    expr = [horizontal, vertical, oblicuo_desc, oblicuo_asc]
    result = list()
    
    # Itero sobre la lista para determinar si encontraron una coincidencia
    for i in expr:
        buscar = i.finditer(adn_str)

    #En caso de encontrar una coincidencia se agrega un True a la lista
        for i in buscar:
            result.append((bool(i)))


    # Se realiza un conteo de la cantidad de coincidencias que hubo
    if result.count(True) > 1:
        return True
    else:
        return False

if __name__ == '__main__':

    adn = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]

    print(isMutant(adn))
    
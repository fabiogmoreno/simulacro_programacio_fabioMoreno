'''3. Buscar producto:
• Implementar un algoritmo de búsqueda que permita al usuario encontrar
 un producto específico por su nombre 
y muestre por pantalla todos los datos de ese producto (nombre, precio y cantidad).'''

def buscar_producto(stock:list[list],nombre_a_encontrar:str) -> None:

    se_encontro = None

    for i in range(len(stock)):

        if stock[i][0] == nombre_a_encontrar:
            #lista_agregar = [nombre,precio,cantidad]
            print(f'\t\t{stock[i][0]}\t{stock[i][1]}\t{stock[i][2]}')
            se_encontro = True
    
    if se_encontro == None:
        print('No se encontro ningun producto a buscar...')
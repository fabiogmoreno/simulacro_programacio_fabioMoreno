#lista_agregar = [nombre,precio,cantidad]
'''Mostrar producto más caro:
• Desarrollar una función que identifique y muestre el producto más caro del inventario.'''

def producto_mas_caro(lista:list[list])->None:

    max_precio = float('-inf')
    
    for i in range(len(lista)):

        if lista[i][1] > max_precio:
            max_precio = lista[i][1]
    
    print(f'El mas caro de los producto es con el precio: {max_precio} ')

def producto_mas_barato(lista:list[list])->None:

    min_precio = float('inf')

    for i in range(len(lista)):

        if lista[i][1] < min_precio:
            min_precio = lista[i][1]
    
    print(f'El mas barato de los producto es con el precio: {min_precio} ')

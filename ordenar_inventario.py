'''Ordenar inventario:
• Utilizar un algoritmo de ordenamiento para ordenar los 
productos en función de su precio de manera ascendente 
y luego mostrar por pantalla los productos ordenados.'''

def ordenar_producto_precio(lista:list):
    # lista_agregar = [nombre,precio,cantidad]
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j][1] > lista[j+1][1]:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
                
    print('MOSTRAR  PRODUCTO ORDENADO ASC POR PRECIO: ')
    for i in range(len(lista)):
        print(f'\t{lista[i][0]}\t{lista[i][1]}\t{lista[i][2]}')

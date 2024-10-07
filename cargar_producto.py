'''2. Cargar inventario:
• Desarrollar una función que permita al usuario ingresar los datos del o los
 productos en una matriz (nombre, precio, cantidad).
• El sistema debe permitir al usuario ingresar la cantidad deseada de productos.'''
def cargar_inventario(lista:list)->list:
    
    nombre = input('Ingrese el nombre del producto: ')
    precio = float(input('Ingrese el precio del producto: '))
    cantidad = int(input('Ingrese la cantidad: '))

    lista_agregar = [nombre,precio,cantidad]

    lista += [lista_agregar]
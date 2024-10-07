'''1. Menú Principal: Mostrar un menú con las siguientes opciones disponibles:
• Cargar producto/s.
• Buscar producto.
• Ordenar inventario.
• Mostrar producto más caro y más barato.
• Mostrar productos con precio mayor a 15000.
• Salir'''
 
 
from cargar_producto import cargar_inventario as cargar_stock
from inventario import inventario as stock
from buscar_producto import buscar_producto as encontrar_stock
from ordenar_inventario import ordenar_producto_precio as ordenar_precio_asc
from mostrar_producto import producto_mas_barato,producto_mas_caro
Entrar = True

while Entrar:
    print('''\t\t\tMENU PRINCIPAL:
            \t\t1) Cargar prodcuto/s
            \t\t2) Buscar producto
            \t\t3) Ordenar inventario
            \t\t4) Mostrar producto mas caro y mas barato
            \t\t5) Mostrar productos con precio mayor a 15000
            \t\t6) Salir
    ''')
    opcion_menu = int(input('Ingrese una opcion: '))

    if opcion_menu == 1: 

        cargar_stock(stock)

    elif opcion_menu == 2:
        
        preguntar_prodcuto = input('Ingrese el nombre del producto que desea buscar: ')
        encontrar_stock(stock,preguntar_prodcuto)

    elif opcion_menu == 3:
        
        ordenar_precio_asc(stock)

    elif opcion_menu == 4:

       producto_mas_caro(stock)

    elif opcion_menu == 5:

        producto_mas_barato(stock)
         

    elif opcion_menu == 6:
        Entrar = False
        break
    
        
    input('Apretar para volver al menu principal.....')
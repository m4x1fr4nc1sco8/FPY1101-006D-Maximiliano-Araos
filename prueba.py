'''Este algoritmo permite administrar el stock de una tienda'''

import os
print('*'*50)
print('Administracion de Stock'.center(50, '*'))
print('*'*50)
print()
productos = {'escoba': 5, 'huevos': 25, 'leche': 9, 'harina': 3}
menup = ['Ver Stock de productos', 'Añadir nuevo producto', 'Ajustar Stock', 'Eliminar producto', 'Salir']
while True:
    for ind, opt in enumerate(menup):
        print(f'{ind+1}. {opt}')
    ans = input('¿Que quieres hacer?\n')
    if ans == '1':
        os.system('cls')
        for a, b in productos.items():
            print(f'{a}: {b}')
        print()
    elif ans == '2':
        os.system('cls')
        while True:
            opcion = input('¿Que producto desea agregar al stock?\n')
            if opcion.replace(' ', '').isalpha():
                break
        if opcion.lower() in productos:
            os.system('cls')
            print('Error: El producto ya existe\n')
            continue
        else:
            os.system('cls')
            productos[opcion.lower()] = 0
            print('¡Producto agregado exitosamente!\n')
    elif ans == '3':
        os.system('cls')
        while True:
            opcion = input('Ingrese el nombre del producto a ajustar:\n')
            if opcion.replace(' ', '').isalpha():
                break
        if opcion.lower() in productos:
            os.system('cls')
            cantidad = input('Ingrese el nuevo stock del producto:\n')
            productos[opcion.lower()] = (cantidad)
            print('¡Producto ajustado exitosamente!')
        else:
            os.system('cls')
            print('Error: El producto no existe\n')
    elif ans == '4':
        os.system('cls')
        while True:
            opcion = input('¿Que producto desea eliminar del stock?\n')
            if opcion.replace(' ', '').isalpha():
                break
        if opcion.lower() in productos:
            os.system('cls')
            del productos[opcion.lower()]
            print('¡Producto borrado exitosamente!\n')
        else:
            os.system('cls')
            print('Error: El producto no existe\n')
    elif ans == '5':
        os.system('cls')
        exit('Gracias por usar nuestro programa, ¡Adios!\n')
    else:
        os.system('cls')
        print('Error: Ingresaste una opcion no valida\n')
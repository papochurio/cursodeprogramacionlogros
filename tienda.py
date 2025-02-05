print("Bienvenidos a virla supermarket\n")

print("¿Que deseas hacer?\n")

nombres = []
precios = []

while True:
    print("\n1-Para añadir un objeto elige: 1")
    print("2-Para revisar lo que hay en el carrito elige: 2")
    print("3-Para eliminar un objeto del carrito elige:3")
    print("4-para calcular el total del carrito elige: 4")
    print("5-Para salir elige: 5")
    
    elegir = int(input("Por favor, elige un numero:\n"))
    
    
    if elegir == 1:
        nombre = input("¿Cual es el nombre del producto?")
        precio = float(input("cual es el precio del producto?"))
        nombres.append(nombre)
        precios.append(precio)
        print("\nEl producto ha sido agregado")
    elif elegir == 2:
        if len(nombres) == 0:
            print("\n No hay productos en el carrito")
            
        else:
            for i in range(len(nombres)):
                 print(f"{i+1}. - {nombres[i]} - ${precios[i]} \n")
           
    elif elegir == 3:
        eliminar = int(input("Por favor, coloca el numero del producto a eliminar"))
        resta = eliminar - 1
        nombres.pop(resta)
        precios.pop(resta)
        print("\nEl articulo ha sido eliminado")
         
    elif elegir == 4:
        indio = sum(precios)
        print(f"\n{indio}")
        
    else:
        print("\nGracias por tu compra, ¡ADIOS!")
        
        break
            
        
        

    
            
            
        
        
        
        
        
        
        
    
            
        
    


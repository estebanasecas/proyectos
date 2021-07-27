# Este programa simula la interacción con un cajero automatico
                                                                                                            

#------------------------------------------------------------------------------------------------------ ultimos movimientos

movimientos = 0
lista = []

def ultimos_mov():

    global movimientos
    
    if movimientos > 0:
        
        print("--------------------------------------------------")
        print("                                    *Saldo Actual*\n")

        for i in range(0, movimientos):

            print('\t', i+1, "%s         %s%s         %s" % (lista[0], lista[1], lista[2], lista[3]))            
   
            del lista[0:4]

        print('--------------------------------------------------')

        movimientos = 0

    else:
     
        print("\n-----------------------------------------------")
        print("No registra ningún movimiento nuevo todavía.")                                     
        print("-----------------------------------------------")
  
    menu()

#------------------------------------------------------------------------------------------------------ deposito

def deposito():

    global saldo_actual
    global movimientos

    while True:

        deposito = input("\nCuanto dinero desea depositar: ")

        try:

            deposito = int(deposito)

            saldo_actual = saldo_actual + deposito

            print("\n-----------------------------")
            print("Ha depositado $%d" % deposito)
            print("Su saldo actual es $%d" % saldo_actual)
            print("-----------------------------")

            lista[0:0] = ['Deposito', '+', deposito, saldo_actual]            
                                                         
            movimientos += 1
            
            menu()
            
        except ValueError:

            print("\nEl comando ingresado no es válido. Intente nuevamente.")


#------------------------------------------------------------------------------------------------------ retiro


def retiro():

    global saldo_actual
    global movimientos

    while True:

        retiro = input("\nCuanto dinero desea retirar: ")

        try:

            retiro = int(retiro)

            if retiro <= saldo_actual:
        
                saldo_actual = saldo_actual - retiro
                print("\n-----------------------------")
                print("Ha retirado $%d" % retiro)
                print("Su saldo actual es $%d" % saldo_actual)
                print("-----------------------------")

                lista[0:0] = ['Retiro  ', '-', retiro, saldo_actual]
        
                movimientos += 1               

                menu()

            else:

                print("\n-----------------------------")
                print("No dispone de esa cantidad")
                print("Su saldo actual es $%d" % saldo_actual)
                print("-----------------------------")
                menu()

        except ValueError:

            print("\nEl comando ingresado no es válido. Intente nuevamente.")
   

#------------------------------------------------------------------------------------------------------ consulta

saldo_actual = 500

def consulta():

    global movimientos

    print("\n-----------------------------")
    print("Su saldo actual es: $%d" % saldo_actual)
    print("-----------------------------")

    lista[0:0] = ['Consulta', '  ', '  ', saldo_actual]
    
    movimientos += 1    

    menu()

#------------------------------------------------------------------------------------------------------ end

def end():

    print("\n-----------------------------------------------")
    print("Muchas gracias por utilizar nuestros servicios.")
    print("-----------------------------------------------")
    exit(0)

#------------------------------------------------------------------------------------------------------ menu

def menu():
           
    print("""\nPor favor seleccione una opción:

1. Consulta de saldo.
2. Retiro de efectivo
3. Depósito de efectivo.
4. Últimos movimientos.
5. Salir             
    """)
   
    opcion = input('> ')

    while True:           
        
        if opcion == "1":
            consulta()           
            
        elif opcion == "2":
            retiro()
                      
        elif opcion == "3":
            deposito()
                       
        elif opcion == "4":
            ultimos_mov()          
           
        elif opcion == "5":
            end()     

        else:
            print("""\nEl comando ingresado no es válido. Intente nuevamente.
        
Por favor seleccione una opción:

1. Consulta de saldo.
2. Retiro de efectivo
3. Depósito de efectivo.
4. Últimos movimientos.
5. Salir             
            """)

            opcion = input('> ') 

#------------------------------------------------------------------------------------------------------ start    

def start():

    input("""----------------------------------------------------------------\n
            **************************************** 
            *Bienvenido al sitema ATM Banco Ahorro*
            ****************************************
            (Por favor presione enter para continuar)""")

    menu()


start()




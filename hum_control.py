# - *- coding: utf- 8 - *-

import random
import time

#------------------------------------------------------------------------------------------------------------------------- logica

def logica():

    print"Es esto correcto (s/n): ", 
    correcto = raw_input()

    if correcto == 's':

        while True:

            print "-----------------------------------------------"
            time.sleep(2)
            print "\n*Programa iniciado*"
            time.sleep(2)
            print "\nIniciando comprobación de humedad en suelo..."
            time.sleep(2)
            hum_random = random.randint(0, 100) 
            print "\nHumedad actual contenida en suelo(%):", hum_random
            time.sleep(2)


            if hum_random >= hum_ini and hum_random <= hum_fin :

                print"\nHº actual dentro de parámetros establecidos(%)", hum_ini, '-', hum_fin, ('\n') 
                time.sleep(2)

            elif hum_random > hum_fin:

                print"\nHº fuera de paramentros establecidos(%)", hum_ini, '-', hum_fin 
                time.sleep(2)
                print"\nIniciando drenaje de suelo..."
                time.sleep(2)
                print"\nDesecando suelo..."
                time.sleep(2)
                print"\nHumedad de suelo regulada."
                time.sleep(2)
                print"\nDrenaje finalizado."
                time.sleep(2)
                hum_reg = (hum_ini + hum_fin) / 2
                print"\nHumedad actual contenida en suelo(%):", hum_reg, '\n'
                time.sleep(2)                

            else:

                print"\nHº fuera de paramentros establecidos(%)", hum_ini, '-', hum_fin 
                time.sleep(2)
                print"\nAbriendo aspersores..."
                time.sleep(2)
                print"\nHumedeciendo suelo..."
                time.sleep(2)
                print"\nHumedad de suelo regulada."
                time.sleep(2)
                print"\nCerrando Aspersores..."
                time.sleep(2)
                hum_reg = (hum_ini + hum_fin) / 2
                print"\nHumedad actual contenida en suelo(%):", hum_reg, '\n'
                time.sleep(2)

        
    elif correcto == 'n':
        print "------------------------------------------"
        ingreso()

    else:
        print "\n>El caracter ingresado no es un número válido."
        print "------------------------------------------"
        ingreso()    


hum_ini = 0
hum_fin = 0
#-------------------------------------------------------------------------------------------------------------------------- ingreso

def ingreso():

    while True:

        print "\nPor favor ingrese los siguientes datos:"
        print "\nNúmero de porcentaje de Hº inicial: ",
        hum_ini = raw_input()

        try :
            
            hum_ini = int(hum_ini)
            global hum_ini  

            while True:
          
                print "\nNúmero de porcentaje de Hº final: ",
                hum_fin = raw_input()
           
                try :
                   
                    hum_fin = int(hum_fin)
                    global hum_fin
             

                    if hum_fin > hum_ini:

                        print "\nRango humedad en suelo requerido(%):", hum_ini, '-', hum_fin          
                        logica()
                        break                  

                    elif hum_fin == hum_ini:

                        print "\nPorcentaje de humedad en suelo requerido(%):", hum_ini
                        logica()
                        break
                                                          
                    else:
                        print ">El número de porcentaje de Hº debe ser igual o mayor a (%)", "%d" % hum_ini           
             
                except ValueError:

                    print ">El caracter ingresado no es un número válido."
                    print "\nPor favor ingrese los siguientes datos:"
                  
        except ValueError:

            print ">El caracter ingresado no es un número válido."

    
#------------------------------------------------------------------------------------------------------------------------ bienvenida

def bienvenida():

    print """
-----------------------------------------------------------------------------------
         *** Bienvenido,
             Este programa se encarga de mantener la  tierra con la humedad deseada
             mediante el control de porcentaje de agua en tierra.

             El contenido de humedad de los suelos típicamente se encuentra en un 
             rango de 5 a 50 % cuando se encuentran en su máxima 
             capacidad de retención (capacidad de campo).
-----------------------------------------------------------------------------------"""

    ingreso()


 
bienvenida()
             
             

import time
import random    


def tomar_datos():

    global hum_ini   # primero ejecuta luego guarda en variable
    global hum_fin

    hum_ini = input("\nPor favor ingrese Hº inicial: ")

    hum_fin = input("Por favor ingrese Hº final: ")

    # verificacion

    while True:
        
        try: 
            hum_ini = int(hum_ini)
            hum_fin = int(hum_fin)

        except ValueError:
            print("Debe ingresar solo numeros. Por favor intente nuevamente: ") 
            tomar_datos()

        else:
            break

    if hum_ini < 5:
        print("\nEl valor Hº inicial no puede ser menor a (%) 5")
        tomar_datos()

    else:
        pass

    if hum_fin < hum_ini:
        print("\nEl valor Hº final debe ser igual o superior al de Hº inicial.")
        tomar_datos()

    else:
        pass


def confirmar_datos():

    global correcto

    print("\nLa Hº del terreneno se mantedra dentro del rango de humedadad (%)", hum_ini, '-', hum_fin)
    correcto = input("Es esto correcto?(s/n) ")
    

#--------------------------------------------------------------------------------------------------------------- ^funciones^   


print("""-----------------------------------------------------------------------------------
         *** Bienvenido,
             Este programa se encarga de mantener el terreno con la humedad deseada
             mediante el control de porcentaje de agua en tierra.

             El contenido de humedad de los suelos típicamente se encuentra en un 
             rango de 5 a 50 % cuando se encuentran en su máxima 
             capacidad de retención (capacidad de campo). Por encima de 50 % 
             se considera terreno inundado.
-----------------------------------------------------------------------------------""")

hum_ini = ''
hum_fin = ''

tomar_datos()

correcto = ''

confirmar_datos()

while True:

    if correcto == 's':
            break

    elif correcto == 'n':
        tomar_datos()
        confirmar_datos()

    else:
        print("\nRespuesta invalida. Por favor intente nuevamente.")
        confirmar_datos()

hum_sel = (hum_ini + hum_fin) / 2

while True:

    hum_random = random.randint(5, 100)

    print("\n---------------------------------------------------------------")
    time.sleep(2)
    print("\nIniciando programa...")
    time.sleep(2)  

    print("\nIniciando analisis de humedad en suelo...")
    time.sleep(2)

    print("\nHº actual (%)", hum_random)
    time.sleep(2)

    if hum_random >= hum_ini and hum_random <= hum_fin:
        print("\nHº actual dentro de parámetros establecidos (%)", hum_ini,'-',hum_fin)

    elif hum_random < hum_ini:
        print("\nHº fuera de paramentros establecidos (%)", hum_ini,'-',hum_fin)
        time.sleep(2)
        print("\nIniciando aspersores...")
        time.sleep(2)
        print("\nHumedeciendo terreno...")
        time.sleep(2)
        print("\nCerrando aspersores...")
        time.sleep(2)
        print("\nHumedad del terreno controlada.")
        time.sleep(2)
        print("\nHº actual (%)", hum_sel)


    elif hum_random > hum_fin:
        print("\nHº fuera de paramentros establecidos (%)", hum_ini,'-',hum_fin)
        time.sleep(2)
        print("\nIniciando drenaje de agua en terreno...")
        time.sleep(2)
        print("\nDesecando terreno...")
        time.sleep(2)
        print("\nDrenaje finalizado")
        time.sleep(2)
        print("\nHumedad del terreno controlada.")        
        time.sleep(2)
        print("\nHº actual (%)", hum_sel)
    
    else:
        pass

    time.sleep(2)















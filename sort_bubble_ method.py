# This script order a list of numbers using 'Bubble method'

lista=[]

while True:

    try:
        number = int(input("Please put a number: "))
        lista.append(number)

    except ValueError:
        print("\nonly a number!\n")
        continue

    other = input("Do you want another number?(s/n) ")
    if other == 's':
        continue
    break

print("\nDisordered numbers: ", lista)

for i in range(1, len(lista)):           # how many times execute 'down for'

    for x in range(0, len(lista)-i):       # each pass execute 'down code'              

        if lista[x] > lista[x+1]:

            aux = lista[x]
            lista[x] = lista[x+1]       
            lista[x+1] = aux

print("\nOrdered numbers:", lista)          

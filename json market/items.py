# This script read and modify a json database file
import json
        
  
with open("items.json") as items:
    
    items_store = json.load(items)
print("*************************")
print("*WELCOME TO MARKET STORE*")
print("*************************")

print("\n- List of items - (item / price)\n")
print(items_store)
print("\nNumber of items:", len(items_store))

while True:

    print('\n-------------------------')
    print("\n> Principal Menu <\n")
    print("\t1.Make a purchase")
    print("\t2.Actualize list")
    print("\t3.Print list")
    print("\t4.Exit")

    option = input('\t\nOption: ')
    # 
    while option == '1':                                                 # MAKE A PURCHASE

        items_list = []

        items_number = input("\nHow many items do yo want to buy?: ")

        try:
            items_number = int(items_number)

        except ValueError:       
            print("\n*You must put only a number*")
            continue
        #             
        for i in range(1, items_number+1):

            while True:

                item = input('\titem%d: ' % i)

                try:
                    items_store[item]
                        
                except KeyError:
                    print("*Item not in store*")

                else:
                    items_list.append(item)
                    break 
        #        
        print("\nSELECTED ITEMS\n")
        total = 0
        for i in items_list:

            print(i)
            print("\t$ %d" % items_store[i])
            total += items_store[i]
        
        correct = input("\nIs that correct?(s/n) ")
        #
        if correct == 's':
            print("\nYour total is: $", total)

            another_purchase = input("\nDo yo want to make another purchase?(s/n) ")

            if another_purchase == 's':
                continue
            else:
                break
    
        else:
            print('Aborted operation.')

            another_purchase = input("\nDo yo want to make another purchase?(s/n) ")

            if another_purchase == 's':
                continue
            else:
                break

    #
    while option == '2':                                            # ACTUALIZE LIST

        print('\n-------------------------')
        print("\nWhat do you want to do?")    
        print("\t1.add item")
        print("\t2.remove item")
        print("\t3.return to menu")
        
        actualize = input('\nOption: ')
        #
        if actualize == '1':              # add item
            
            new_item = input("Add new item: ")
            new_price = input("Add item price: ")
            
            try:
                new_price = int(new_price)

            except ValueError:
                print("*Price must be a number*")
    
            else:            
                items_store[new_item] = new_price
                print("\nSucces!!!")
       
                with open('items.json', 'w') as new_items_store:
                    json.dump(items_store, new_items_store)
        #
        elif actualize == '2':            # remove item

            rem_item = input("Add item yow want to remove: ")

            try:
                items_store.pop(rem_item)
                print('\nSucces!!!')

            except KeyError:
                print("\n*The item does not exist*")        

            else:
                with open('items.json', 'w') as new_items_store:
                    json.dump(items_store, new_items_store)                    
        #
        elif actualize == '3':            # return to menu
            break          
        #
        else:                           
            print("\n*Option does not exist. Please, try again*")
    
    #
    while option == '3':                                            # PRINT LIST

        print('\n-------------------------')
        print("\n- List of items - (item / price)\n")
        print('\n',items_store)
        print("\nNumber of items:", len(items_store))
        break

    while option == '4':                                            # EXIT

        print('Goodbye!!!')
        exit(0)

    while option != '1' and option != '2' and option != '3' :
        print("\n*Option does not exist. Please, try again*")
        break   
    




 



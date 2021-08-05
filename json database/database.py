# This script read and modify a json database file
import json

with open("database.json") as clients:

    database = json.load(clients)                                    # Create a database dict from json file         


print("CLIENT DATABASE:")

number_pass = (len(database) // 4)

for i in range(0, number_pass) :

    i = i + 1
    i = str(i)

    print('')
    print(i+".Client name:", database[i+'.Name'])                    # Print database 
    print(i+".Client lastname:", database[i+'.Lastname'])              
    print(i+".Client telephone:", database[i+'.Telephone'])            
    print(i+".Client children:", database[i+'.Children'])              

update = input("\nDo you want to update the database?(s/n) ")

if update == 's':

    # update json database file

    count = len(database) // 4 + 1
    client_added = 1    
 
    while True:

        count = str(count)        

        print('')
        name = input(count+ ".Client name: ")                        # New customer input
        lastname = input(count+ ".Client lastname: ") 
        telephone = input(count+ ".Client telephone: ")                    
        
        while True:

            children = input(count+ ".How many children: ")

            try: 
                children = int(children)
                break

            except ValueError:
                print("You mus put a number.")   
                             
        children_list = []      

        for i in range(0, children):
            
            name = input("\tName: ")
            children_list.append(name)  

        database[count+".Name"] = name                               # Add new customer to actual dict
        database[count+".Lastname"] = lastname
        database[count+".Telephone"] = telephone
        database[count+".Children"] = children_list 
           
        new_client = input("\nAdd new client?(s/n) ")

        if new_client == 's':
            count = int(count)
            count += 1
            client_added += 1
        else:
            break

    print("\nDATABASE HAS BEEN UPDATED!")
    print("Added  %d  new clients" % client_added)
    print("Total clients: ", len(database)// 4)


    with open("database_updated.json", 'w') as update:

        json.dump(database, update)

else :
    exit(0)

    
                                   



    








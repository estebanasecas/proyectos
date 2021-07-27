
# Enjoy this dungeon adventure!
# If you get stuck and you are a coward chicken, here the magic keywords to pass : search keys / search carrot / check items

import time 

keys_founded = []
deaths = 0

#---------------------------------------------------------------------------------------------------------------------- Final door

def final_door():

    print("""\n>>>>>
\nYou are front of the door at the end of the corridor."""),
    input()
    print("It's a big door in solid wood. I cannot open it!"),
    input()
    print("There is a big padlock with five holes. Maybe I could 'check' my items."), input()
        
    while True:

        print("What do you do?")
        print("(open) the door / (back) to the hall\n")
        option = input('> ')

        if option == "open":
            if len(keys_founded) == 5:
                
                print("\n*** YOU OPEN THE DOOR. YOU ARE THE NEW DUNGEON MASTER!!! ***")
                print("\n*** YOU OPEN THE DOOR. YOU ARE THE NEW DUNGEON MASTER!!! ***")
                print("\n*** YOU OPEN THE DOOR. YOU ARE THE NEW DUNGEON MASTER!!! ***")
                print("\n*** YOU OPEN THE DOOR. YOU ARE THE NEW DUNGEON MASTER!!! ***")
                print("\n*** YOU OPEN THE DOOR. YOU ARE THE NEW DUNGEON MASTER!!! ***")
                print("\nNumber of deaths: ", deaths)
                exit(0)
                                  
            else:
                print("\nYou don't have all the keys!"), input()  

        elif option == "back":
            print("\nYou are returning to the hall...\n")
            time.sleep(2)
            hall()
            break

        elif option == "search keys":
            print("\nSearching keys...\n")
            time.sleep(2)
            print("I cannot find any keys in this place."), input()

        elif option == "search carrot":
            print("\nSearching carrot...")
            time.sleep(2)
            print("\nThere is not a carrot here."), input()

        elif option == "check items":

            print("\nChecking items...")
            time.sleep(2) 
            print("Number of keys you have: ", keys_founded)
            while carrot == 1:
                print("Another items: 1 carrot") 
                break
            input()
           
        else:
            stupid()

#---------------------------------------------------------------------------------------------------------------------- Door 4

key_door_4 = 1

def door_4():

    global key_door_4                        # Global Override

    print("\n>>>>>")
    print("\nYou open the door 4."), input()
    print("This room has a hugh collection of shields and armors."), input()    

    while True:

        option = door_3_4_option()

        if option == "leave":

            print("\nYou are leaving the room...\n")
            time.sleep(2), hall()

        elif option == "search keys":
            print("\nSearching keys...")
            time.sleep(2)
            if key_door_4 == 1:
                print("\nYou find a key behind a shield!"), input()
                keys_founded.append(1)                
                key_door_4 = 0
            else:
                print("\nThere isn't more keys in this place."), input()

        elif option == "search carrot":

            print("\nSearching a carrot...")
            time.sleep(2)
            print("\nThere is not a carrot here."), input()

        elif option == "check items":

            print("\nChecking items...")
            time.sleep(2)
            print("\nNumber of keys you have: ", keys_founded)
            while carrot == 1:
                print("Another items: 1 carrot")
            input()              
         
        else:
            stupid()

#---------------------------------------------------------------------------------------------------------------------- Door 3

def door_3_4_option():

    print("What do you do?")
    print("(leave) the room")
    option = input('\n> ')
    return option

#---------------------------------------------------------------------------- /

key_door_3 = 1

def door_3():

    global key_door_3                # Global Override
    global carrot                    # Global Override
    
    print("\n>>>>>")
    print("\nYou open the door 3."), input()
    print("This room seems like a kitchen."), input()

    while True:

        option = door_3_4_option()

        if option == "leave":
            print("\nYou are leaving the room...\n")
            time.sleep(2)
            hall()

        elif option == "search keys":
            print("\nSearching keys...")
            time.sleep(2)
            if key_door_3 == 1:
                print("\nYou find a key in a stew!"), input()
                keys_founded.append(1)                
                key_door_3 = 0
            else:
                print("\nThere isn't more keys in this place."), input() 

        elif option == "search carrot":

            print("\nSearching a carrot...")
            time.sleep(2)
            if carrot == 0:               
                print("\nYou find a carrot in the fridge!"), input()
                carrot = 1
            else:
                print("\nThere is no more carrots here."), input()

        elif option == "check items":

                print("\nChecking items...")
                time.sleep(2)
                print("\nNumber of keys you have: ", keys_founded)
                while carrot == 1:
                    print("Another items: 1 carrot")
                    break
                input()
        else:
            stupid()
                    
#---------------------------------------------------------------------------------------------------------------------- Door 2       

key_door_2 = 1

def door_2():

    global key_door_2
    
    print("\n>>>>>")
    print("\nYou open the door 2."), input()
    print("This room is entirely empty.")
    print("There is only a little chest in the center of the room."), input()

    while True:    

        print("What do you do?")
        print("(leave) the room / (look) at the chest")
        option = input('\n> ')

        if option == "leave":
            print("\nYou are leaving the room...\n")
            time.sleep(2), hall()

        elif option == "look":

            if key_door_2 == 1 and len(keys_founded) != 4:
                print("\nThe chest is also empty.")
                print("There is a note..."), input()
                print("\t\"If want you some magic see")
                print("\tcollect must four other keys\"\n"), input() 

            elif key_door_2 == 1 and len(keys_founded) == 4:
                print("\nYou find a key!"), input()
                keys_founded.append(1)
                key_door_2 = 0

            else:
                print("\nThe chest is empty.")
                print("You has taken the key already."), input()

        elif option == "search keys":
            print("\nSearching keys...")
            time.sleep(2)
            print("\nThere is not keys in this place."), input() 

        elif option == "search carrot":

            print("\nSearching a carrot...")
            time.sleep(2)
            print("\nThere is not a carrot here."), input()

        elif option == "check items":

            print("\nChecking items...")
            time.sleep(2)
            print("\nNumber of keys you have: ", keys_founded), input()
            while carrot == 1:
                print("Another items: 1 carrot"), input()
                break
               
        else:
            stupid()      
    
#---------------------------------------------------------------------------------------------------------------------- Door 1

witch = 1
carrot = 0

def door_1():

    global witch                              # Global Override 
    global carrot                             # Global Override

    print("\n>>>>>")
    print("\nYou open the door 1."), input()

    while witch == 1:

        print("You see the witch bababanga who lives here."), 
        input()
        print("You notice that she has a key around her neck."),
        input()
        print("She will give it to you if you give a carrot to her."),
        input()
        print("Maybe you need to 'search' a carrot."), input()

        while True:

            print("What do you do?")
            print("(trick) to her / (give) her a carrot / (leave) the room")
            option = input('\n> ')
                   
            if option == "trick":
                print("\nYou give her a stick of wood but she discovers you and transforms you in a hot dog.")
                play_again()

            elif option == "give":

                if carrot == 1:
                    print("\nThe witch takes the carrot and")
                    print("flies away in her flying broom."), input()                
                    witch = 0
                    carrot = 0
                    keys_founded.append(1)
                    print("You find a key!"), input()
                    print("You has nothing to do here now."),
                    input()
                    print("You're leaving the room...\n")
                    time.sleep(3), hall()
                                              
                else:
                    print("\nYou doesn't have a carrot to her.")
                    print("The witch punish your insolence and transforms you in a cigarrete and smokes it.")
                    play_again()

            elif option == "leave":
                print("\nYou run away like a coward to find a carrot and come back."), input()
                hall()
                break

            elif option == "search keys":
                print("\nThe key is hanging from the witch's neck.!"), input() 

            elif option == "search carrot":
                print("\nSearching a carrot...")
                time.sleep(2)
                print("\nThere is not a carrot here."), input()

            elif option == "check items":

                print("\nChecking items...") 
                time.sleep(2)
                print("\nNumber of keys you have: ", keys_founded)
                while carrot == 1:
                    print("Another items: 1 carrot")
                    break
                input()               

            else:
                stupid()

    else:
        print("The witch flew away in her flying broom."),
        input()
        print("You has nothing to do here now."), 
        input() 
        print("You're leaving the room...")
        time.sleep(2), hall()
        

#---------------------------------------------------------------------------------------------------------------------- Hall

key_hall = 1

def hall():

    global key_hall              # Override : change global value of the variable

    print(""">>>>>                                                                                    final door
                                                                                             [ ]         
You are in a hall wich has two doors at your left and two doors at your right.        
At the end of the corridor there is final door bigger than the others.              door 3 []   [] door 4
Maybe you must 'look' the doors...                                                      
                                                                                    door 1 []   [] door 2
                                                                                              *                    """)
    while True:

        print("What do you do?")
        option = input('\n> ')

        if option == "look door 1":
            door_1()
            break         
        elif option == "look door 2":
            door_2()
            break
        elif option == "look door 3":
            door_3()
            break
        elif option == "look door 4":
            door_4()
            break
        elif option == "look final door":  
            final_door()
            break

        elif option == "search keys":

            print("\nSearching a key...")
            time.sleep(2)

            if key_hall == 1:                             
                print("\nYou find a key!"), input()
                keys_founded.append(1)
                key_hall = 0                             
            else:
                print("\nThere isn't more keys in this place."), input()

        elif option == "search carrot":
                print("\nSearching a carrot...")
                time.sleep(2)
                print("\nThere is not a carrot here."), input()

        elif option == "check items":

            print("\nChecking items...") 
            time.sleep(2)
            print("\nNumber of keys you have: ", keys_founded)
            while carrot == 1:
                print("Another items: 1 carrot"), input()
                break

        else:  
            stupid()
 
#---------------------------------------------------------------------------------------------------------------------- Main door

def main_door():

    print("""\n>>>>>
\nYou are in front of the main castle's door.
Next to the door yo see a chain with a handle at the end."""), 
    input()
    print("Also you notice an old man in a corner under a cape."),
    input()
    print("He looks strange be careful!"), input()
    print("What do you do?")
    print("(look for) another way / (pull) the handle / (talk) to the old man") 
    
    option = input('\n> ')

    while option == "talk":

        print("""\n>>>>>
\n\tOld man: 
\t        "Ohh stranger don't pull the handle, it's a trap!
\t         If you dare to enter to this castle you will need 
\t         to 'search' the five keys and find them."""), input()
        print("What do you do?")
        print("(look for) another way / (pull) the handle / (talk) to the old man again.")
         
        option = input('\n> ')

        if option == "talk":
            print("\nThe old man turns mad and kill you.")
            play_again()
        
        else:
            pass
  
    while option == "pull":
        print("\nA trap is opened and you fall in the darkness. Nobody see you again.")
        play_again()

    while option == "look for":
        print("\n>>>>>")
        print("\nYou go around the house."),
        input()
        print("You find a ladder standing against the wall. You climb it."),
        input()
        print("There is a small window. You get trough it to take a look."),
        input()
        print("You slip like a fool and you fall from the height inside the castle."),
        input()
        print("You cannot get back now."), input()        

        hall()

    else:
        stupid()


#------------------------------------------------------------------------------ Play again

def play_again():

    global keys_founded 
    global key_door_2 
    global key_door_3 
    global key_door_4 
    global key_hall 
    global witch 
    global carrot 
    global deaths

    while True:

        again = input("Do you want to play it again?(y/n)") 

        if again == 'y':            
            keys_founded = []
            key_door_2 = 1
            key_door_3 = 1
            key_door_4 = 1
            key_hall = 1
            witch = 1
            carrot = 0
            deaths += 1
            start()

        elif again == 'n':
            exit(0)

        else:
            print("\nIncorrect answer. Try again...")


#------------------------------------------------------------------------------ Stupid 
       
def stupid():
    print("\nYour legs are shaking and you become insane like an idiot. Good job!")
    play_again()

#---------------------------------------------------------------------------------------------------------------------- Start

def start():

    print("""\n***************************************************
* You must choose the right answer                *
* to exit alive from the dungeon... Enjoy it!     *
***************************************************\n 
You are in the middle of nowhere.
It's raining and you're cold."""),
    input()
    print("You distinguish a castle far away."), input()
    print("What do you do?") 
    print("(wait) for help / (go) to the castle") 

    option = input('\n> ')

    if option == "wait":
        print("Your body is discovered days later and helps come.")
        play_again() 
    elif option == "go":
        main_door()
    else:
        stupid()


start()
        
        








# If you get stuck!
# Magic keywords to pass : search keys / search carrot / check items

import time 

keys_founded = []

#--------------------------------------------------------------------------------------------------------------------------- Final door

def final_door_option():

    print "\nWhat do you do?"
    print "(open) the door / (back) to the hall"
    option = raw_input('\n>')
    return option

#---------------------------------------------------------------------------- /

def final_door():

    print """\n>>>>>
\nYou are front of the door at the end of the corridor.""",
    raw_input()
    print "It's a big door in solid wood. I cannot open it!",
    raw_input()
    print "There is a big padlock with five holes. Maybe I could 'check' my items.", raw_input()
        
    while True:

        print "What do you do?"
        print "(open) the door / (back) to the hall\n"
        option = raw_input('> ')

        if option == "open":
            if len(keys_founded) == 5:
                while True:
                    print "*** YOU OPEN THE DOOR. YOU WIN!!! ***"                 
            else:
                print "\nYou don't have all the keys!", raw_input()  

        elif option == "back":
            print"\nYou are returning to the hall...\n"
            time.sleep(3)
            hall()
            break

        elif option == "search keys":
            print "\nSearching keys...\n"
            time.sleep(2)
            print "I cannot find any keys in this place.", raw_input()

        elif option == "search carrot":
            print "\nSearching carrot..."
            time.sleep(2)
            print "\nThere is not a carrot here.", raw_input()

        elif option == "check items":

            print "\nChecking items..."
            time.sleep(2) 
            print "Number of keys you have: ", keys_founded
            while carrot == 1:
                print "Another items: 1 carrot" 
                break
            raw_input()
           
        else:
            stupid()

#--------------------------------------------------------------------------------------------------------------------------- Door 4

key_door_4 = 1

def door_4():

    print "\n>>>>>"
    print "\nYou open the door 4.", raw_input()
    print "This room has a hugh collection of shields and armors.", raw_input()    

    while True:

        option = door_3_4_option()

        if option == "leave":

            print "\nYou are leaving the room...\n"
            time.sleep(3), hall()

        elif option == "search keys":
            print "\nSearching keys..."
            time.sleep(2)
            if key_door_4 == 1:
                print "\nYou find a key behind a shield!", raw_input()
                keys_founded.append(1)
                global key_door_4                        # Global Override
                key_door_4 = 0
            else:
                print "\nThere isn't more keys in this place.", raw_input()

        elif option == "search carrot":

            print "\nSearching a carrot..."
            time.sleep(2)
            print "\nThere is not a carrot here.", raw_input()

        elif option == "check items":

            print "\nChecking items..."
            time.sleep(2)
            print "\nNumber of keys you have: ", keys_founded
            while carrot == 1:
                print "Another items: 1 carrot"
            raw_input()              
         
        else:
            stupid()

#--------------------------------------------------------------------------------------------------------------------------- Door 3

def door_3_4_option():

    print "What do you do?"
    print "(leave) the room"
    option = raw_input('\n> ')
    return option

#---------------------------------------------------------------------------- /

key_door_3 = 1

def door_3():
    
    print "\n>>>>>"
    print "\nYou open the door 3.", raw_input()
    print "This room seems like a kitchen.", raw_input()

    while True:

        option = door_3_4_option()

        if option == "leave":
            print "\nYou are leaving the room...\n"
            time.sleep(3)
            hall()

        elif option == "search keys":
            print "\nSearching keys..."
            time.sleep(2)
            if key_door_3 == 1:
                print "\nYou find a key in a stew!", raw_input()
                keys_founded.append(1)
                global key_door_3                # Global Override
                key_door_3 = 0
            else:
                print "\nThere isn't more keys in this place.", raw_input() 

        elif option == "search carrot":

            print "\nSearching a carrot..."
            time.sleep(2)
            if carrot == 0:               
                print "\nYou find a carrot in the fridge!", raw_input()
                global carrot                    # Global Override
                carrot = 1
            else:
                print "\nThere is no more carrots here.", raw_input()

        elif option == "check items":

                print "\nChecking items..."
                time.sleep(2)
                print "\nNumber of keys you have: ", keys_founded
                while carrot == 1:
                    print "Another items: 1 carrot"
                    break
                raw_input()
        else:
            stupid()
                    
#--------------------------------------------------------------------------------------------------------------------------- Door 2       

key_door_2 = 1

def door_2():
    
    print "\n>>>>>"
    print "\nYou open the door 2.", raw_input()
    print "This room is entirely empty."
    print "There is only a little chest in the center of the room.", raw_input()

    while True:    

        print "What do you do?"
        print "(leave) the room / (look) at the chest"
        option = raw_input('\n> ')

        if option == "leave":
            print"\nYou are leaving the room...\n"
            time.sleep(3), hall()

        elif option == "look":

            if key_door_2 == 1 and len(keys_founded) != 4:
                print "\nThe chest is also empty."
                print "There is a note...", raw_input()
                print "\t\"If want you some magic see"
                print "\tcollect must four other keys\"\n", raw_input() 

            elif key_door_2 == 1 and len(keys_founded) == 4:
                print "\nYou find a key!", raw_input()
                keys_founded.append(1)
                global key_door_2
                key_door_2 = 0

            else:
                print "\nThe chest is empty."
                print "You has taken the key already.", raw_input()

        elif option == "search keys":
            print "\nSearching keys..."
            time.sleep(2)
            print "\nThere is not keys in this place.", raw_input() 

        elif option == "search carrot":

            print "\nSearching a carrot..."
            time.sleep(2)
            print "\nThere is not a carrot here.", raw_input()

        elif option == "check items":

            print "\nChecking items..."
            time.sleep(2)
            print "\nNumber of keys you have: ", keys_founded, raw_input()
            while carrot == 1:
                print "Another items: 1 carrot", raw_input()
                break
               
        else:
            stupid()      
    
#--------------------------------------------------------------------------------------------------------------------------- Door 1

def door_1_option():

    print "What do you do?"
    print "(trick) to her / (give) her a carrot / (leave) the room"
    option = raw_input('\n> ')
    return option

#---------------------------------------------------------------------------- / 

witch = 1
carrot = 0

def door_1():

    print "\n>>>>>"
    print "\nYou open the door 1.", raw_input()

    while witch == 1:

        print"You see the witch bababanga who lives here.", 
        raw_input()
        print "You notice that she has a key around her neck.",
        raw_input()
        print "She will give it to you if you give a carrot to her.",
        raw_input()
        print "Maybe you need to 'search' a carrot.", raw_input()

        while True:

            option = door_1_option()

            if option == "trick":
                print "\nYou give her a stick of wood but she discovers you and transforms you in a hot dog."
                exit(0)

            elif option == "give":

                if carrot == 1:
                    print "\nThe witch takes the carrot and"
                    print "flies away in her flying broom.", raw_input()                
                    global witch                              # Global Override 
                    witch = 0
                    global carrot                             # Global Override
                    carrot = 0
                    keys_founded.append(1)
                    print "You find a key!", raw_input()
                    print "You has nothing to do here now.",
                    raw_input()
                    print "You're leaving the room...\n"
                    time.sleep(3), hall()
                                              
                else:
                    print "\nYou doesn't have a carrot to her."
                    print "The witch punish your insolence and transforms you in a cigarrete and smokes it."
                    exit(0)

            elif option == "leave":
                print "\nYou run away like a coward to find a carrot and come back.", raw_input()
                hall()
                break

            elif option == "search keys":
                print "\nThe key is hanging from the witch's neck.!", raw_input() 

            elif option == "search carrot":
                print "\nSearching a carrot..."
                time.sleep(2)
                print "\nThere is not a carrot here.", raw_input()

            elif option == "check items":

                print "\nChecking items..." 
                time.sleep(2)
                print "\nNumber of keys you have: ", keys_founded
                while carrot == 1:
                    print "Another items: 1 carrot"
                    break
                raw_input()               

            else:
                stupid()

    else:
        print "The witch flew away in her flying broom.",
        raw_input()
        print "You has nothing to do here now.", 
        raw_input() 
        print "You're leaving the room..."
        time.sleep(3), hall()
        

#--------------------------------------------------------------------------------------------------------------------------- Hall

key_hall = 1

def hall():
    print """>>>>>                                                                                    final door
                                                                                             [ ]         
You are in a hall wich has two doors at your left and two doors at your right.        
At the end of the corridor there is final door bigger than the others.              door 3 []   [] door 4
Maybe you must 'look' the doors...                                                      
                                                                                    door 1 []   [] door 2
                                                                                              *                    """
    while True:

        print"What do you do?"
        option = raw_input('\n> ')

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

            print "\nSearching a key..."
            time.sleep(2)

            if key_hall == 1:                             
                print "\nYou find a key!", raw_input()
                keys_founded.append(1)
                global key_hall              # Override : change global value of the variable
                key_hall = 0                             
            else:
                print "\nThere isn't more keys in this place.", raw_input()

        elif option == "search carrot":
                print "\nSearching a carrot..."
                time.sleep(2)
                print "\nThere is not a carrot here.", raw_input()

        elif option == "check items":

            print "\nChecking items..." 
            time.sleep(2)
            print "\nNumber of keys you have: ", keys_founded
            while carrot == 1:
                print "Another items: 1 carrot", raw_input()
                break

        else:  
            stupid()
 
#---------------------------------------------------------------------------------------------------------------------- Main door

def main_door():

    print """\n>>>>>
\nYou are in front of the main castle's door.
Next to the door yo see a chain with a handle at he end.""", 
    raw_input()
    print "Also you notice an old man in a corner under a cape.",
    raw_input()
    print "He looks strange be careful!", raw_input()
    print "What do you do?"
    print "(look for) another way / (pull) the handle / (talk) to the old man" 
    
    option = raw_input('\n> ')

    while option == "talk":

        print """\n>>>>>
\n\tOld man: 
\t        "Ohh stranger don't pull the handle, it's a trap!
\t         If you dare to enter to this castle you will need 
\t         to 'search' the five keys and find them.""", raw_input()
        print "What do you do?"
        print "(look for) another way / (pull) the handle / (talk) to the old man again."
         
        option = raw_input('\n> ')

        if option == "talk":
            print "\nThe old man turns mad and kill you."
            exit(0)
        
        else:
            pass
  
    while option == "pull":
        print "\nA trap is opened and you fall in the darkness. Nobody see you again."
        exit(0)

    while option == "look for":
        print "\n>>>>>"
        print "\nYou go around the house...",
        raw_input()
        print "You find a ladder standing against the wall. You climb it.",
        raw_input()
        print "There is a small window. You get trough it to take a look.",
        raw_input()
        print "You slip like a fool and you fall from the height inside the castle.",
        raw_input()
        print "You cannot get back now.", raw_input()        

        hall()

    else:
        stupid()
 
#------------------------------------------------------------------------------------------------------------------------------ Stupid
        
def stupid():
    print "\nYou doubt and you become insane like an idiot. Good job!"
    exit(0)

#------------------------------------------------------------------------------------------------------------------------------ Start

def start():

    print"""\n***************************************************
* This is a game.You must choose the right answer *
* to exit alive... Enjoy it!                      *
***************************************************\n 
You are in the middle of nowhere.
It's raining and you're cold.""",
    raw_input()
    print "You distinguish a castle far away.", raw_input()
    print "What do you do?" 
    print "(wait) for help / (go) to the castle" 

    option = raw_input('\n> ')

    if option == "wait":
        print "Your body is discovered days later and helps come."
        exit(0) 
    elif option == "go":
        main_door()
    else:
        stupid()


start()
        
        







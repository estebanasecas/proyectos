# This script show result in shell and make a json file 

import requests
import json

print("*********")
print("*Pokedex*") 
print("*********")

while True:

    print("\nWelcome to pokedex")

    name = input("What pokemon are you looking for? ")

    pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/" + name)
    #
    if pokemon_req.status_code == 200:
        
        pokemon = pokemon_req.json()
                
        my_pokemon_name = pokemon['forms'][0]['name']
        my_pokemon_type = pokemon['types'][0]['type']['name']
        my_pokemon_weight = pokemon['weight']        
        my_pokemon_moves = []
      
        for i in range(0, len(pokemon['moves'])):

            my_pokemon_moves.append(pokemon['moves'][i]['move']['name'])

        my_pokemon = {}                                  # make my dict
        my_pokemon['name'] = my_pokemon_name
        my_pokemon['type'] = my_pokemon_type
        my_pokemon['weight'] = my_pokemon_weight  
        my_pokemon['moves'] = my_pokemon_moves

        print("\nName: "+ my_pokemon['name'])
        print("\nType: "+ my_pokemon['type'])
        print("\nWeight: %d lbs" % my_pokemon['weight'])
        print("\nMoves: ", my_pokemon['moves'])

        with open('api_pokedex_' + my_pokemon['name'] + '_delete.json', 'w') as pokemon_json:

            json.dump(my_pokemon, pokemon_json)
    #   
    else:
        print("\nPokemon not in database :(")
    #
    again = input("\nDo you want to search another pokemon?(s/n) ")

    if again == 's':
        print("\n----------------------------")
    else:
        break       

    





        

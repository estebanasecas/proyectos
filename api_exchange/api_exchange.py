# This script consult world currencies and print results in shell 

import requests
import json


def request(input_code):

    my_request = requests.get("https://v6.exchangerate-api.com/v6/952a96187ed9ffbb9dce41d1/latest/"+input_code.upper())
                                                                     #   {       my api key       }    
    return my_request.json()

#-------------------------------------------------------------------------------------------------------------

print('**************')
print('*API-EXCHANGE*')
print('**************')

while True:
    
    print("\nPlease, select an option:")

    print("\n1.Consult Country Currency Code")
    print("2.Consult specific currency")
    print("3.Exchange currency operation")
    print("4.Exit")

    option = input('\nOption: ')

    with open('country_codes.json') as codes:
            currency_codes = json.load(codes)
    #
    if option == '1':
        
        print("\nCOUNTRY              CURRENCY               CODE\n")

        for i in currency_codes:

            print("%s      %s        %s" % (currency_codes[i][1],currency_codes[i][0],i))

        print("\n---------------------------------------------")
    #   
    elif option == '2':
        
        input_code = input("\nPlease write currency code: ")

        try:        
            currency_codes[input_code.upper()]                                     # verification code exists
        except KeyError:
            print("\nCurrency code does not exist.") 
            continue      
        # 
        print('')    
        print(currency_codes[input_code.upper()][1] + ' (' + currency_codes[input_code.upper()][0] + ')')
        print('')
        #
        currency_data = request(input_code)

        for i in currency_data['conversion_rates']:

            print("%s        %.3f" % (i, currency_data['conversion_rates'][i]))
        
        print("\nLast update currency: " + currency_data['time_last_update_utc'])
        print("Next update currecny: " + currency_data['time_next_update_utc']+'\n')
        print("\n---------------------------------------------")
    #
    elif option == '3':
        
        from_curr = input('\nfrom: ')
        to_curr = input('to: ')
        amount = input('Please specify amount: ')

        try:
            amount = int(amount)                                          # verification int number
        except ValueError:
            print("\nAmount Error. Must be a int number. Try again.")       
            print("\n---------------------------------------------")
            continue 

        try:        
            currency_codes[from_curr.upper()]                             # verification code exists  
            currency_codes[to_curr.upper()]                   
        except KeyError:
            print("\nCurrency Error. Code does not exist. Try again.")
            print("\n---------------------------------------------")
            continue
        #
        from_currency_data = request(from_curr)
   
        result = amount * from_currency_data['conversion_rates'][to_curr.upper()]

        print('\n*Conversion succes!*')
        print("\n\t%s  %.3f" % (from_curr.upper(), amount))
        print("\t%s  %.3f" % (to_curr.upper(), result))
        
        print("\nLast update currency: " + from_currency_data['time_last_update_utc'])
        print("Next update currecny: " + from_currency_data['time_next_update_utc'])

        print("\n---------------------------------------------")
    #
    elif option == '4':
        
        print('\nGOODBYE!')
        exit(0)

    else:
        print("\nError. Option does not exist. Try again.")
        print("\n---------------------------------------------")
        







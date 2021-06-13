import random

# This program determinates a winner from a raffle.

# Who pay ($100) or more is a participant and has acces to the rafle.
# Who pay less is a contributor but does not have acces to the rafle.
# Who doesnt't pay nothing is not a contributor and nor does not have acces to the rafle.

print '\n****************'
print '*Rafle\'s winner* '
print '****************'

database = {}

for i in range(0, 10):  # here database until 10 people         This for
                                                              #         - take input data
    name = raw_input('\nName: ')                              #         - change data type (Paid) str > int
                                                              #         - actualiize database
    paid = raw_input('Paid: $ ')

    while paid == str(paid) :

        try:

            paid = int(paid)

        except ValueError:

            print "Must put integer number."
            paid = raw_input('Has paid: $') 

    database[name] = paid


print '\nActualized database: ', database 


participants = {}      # create a sub-dict                                                    
contributors = {}      # create a sub-dict
none = {}              # create a sub-dict


collected_money = 0
number_participants = 0
number_contributors = 0
number_none = 0
for i in database:                                            # This for
                                                              #         - break down database
    if database[i] >= 100:                                    #         - divert to sub-dict
                                                              #         - collect money
        participants[i] = database[i]                         #         - count participants/contributors/none
        collected_money += database[i]
        number_participants += 1

    elif database[i] < 100 and database[i] > 0:

        contributors[i] = database[i]
        collected_money += database[i]
        number_contributors += 1

    else:
       
        none[i] = database[i]
        number_none += 1


print '\nParticipants: ', participants, '- %d participants -' % number_participants
print 'Contributors: ', contributors, '- %d contributors -' % number_contributors
print 'none: ', none, '- %d none -' % number_none

print '\nCollected money: $ ', collected_money


number = 0
for name in participants:                                     # This for
                                                              #         - assigns a number to each participant
    number += 1                                               #           who participes in the rafle 
    participants[name] = number


print '\nAssignement_numbers', participants

random_number = random.randint(1, number)

print '\nThe winner number is ', random_number


for i in participants:                                        # This for
                                                              #         - determines who win the rafle 
    if random_number == participants[i]:

        print '\n********************' 
        print 'The winner is ', i
        print '********************' 
















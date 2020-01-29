# TASK:
#  Two nonnegative numbers (0 <= number_1 <= number_2 <= 999999) - command line arguments.
#  Finding the number of "dream tickets" whose numbers located between the number_1 to number_2 inclusive. 
#  If the number in the interval is less than 6 digits, at its beginning zeros are added to the required number, 
#   as is the case with the numbering of the tickets

import sys
number_1=int(sys.argv[1])
number_2=int(sys.argv[2])
number_of_dream_tickets=0
dream_ticket=[]
if 0<=number_1<=number_2<=999999:
  while number_1<=number_2:
    number_1=str(number_1)
    number_1=number_1.zfill(6)
    x=int(number_1[0])+int(number_1[1])+int(number_1[2])
    y=int(number_1[3])+int(number_1[4])+int(number_1[5])
    if x==y:
      number_of_dream_tickets+=1
      dream_ticket.append(number_1)
    number_1=int(number_1)
    number_1+=1
else:
 print ("The entered argument does not satisfy the condition 0<=number_1<=number_2<=999999. Please try again")
print ("Number of Dream tickets:", number_of_dream_tickets)
print ("Dream tickets:", dream_ticket)
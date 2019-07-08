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
 print ("Введений аргумент не задовольняє умову 0<=number_1<=number_2<=999999. Будь ласка, повторіть спробу")
print ("Number of Dream tickets:", number_of_dream_tickets)
print ("Dream tickets:", dream_ticket)

# Два цілих невід'ємних числа (0<=number_1<=number_2<=999999) - аргументи командного рядка.
# Пошук кількості "щасливих квитків", чиї номери лежать на проміжку від number_1 до number_2 включно. 
#Якщо число на проміжку має менше 6 розрядів, вважати, що на його початку дописуються нулі у необхідній кількості, як це і відбувається при нумерації квитків. 

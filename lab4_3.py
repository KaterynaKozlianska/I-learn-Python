import sys
x=str("(")
y=str(")")
flag=True

z=str(sys.argv[1:])
z=z.replace(",","").replace("[","").replace("]","").replace("'","").replace(" ","")

if (len(z))%2==0 and len(z)>0:
 for i in range (len(z)//2):
  i=i*2
  if z[i]==x[0] and z[(i+1)]==y[0]:
   flag
  else:
   flag=False
elif len(z)<1:
 flag=False
 print ('Please input more then zero symbols')
else: 
 flag=False

if flag:
 print ("YES")
else:
 print ("NO")

 #Рядок, що складається з відкриваючих та закриваючих круглих дужок - аргумент командного рядка. Для передачі в якості рядка послідовність береться в подвійні лапки
 #Рядок "YES", якщо вхідний рядок містить правильну дужкову послідовність; або рядок "NO", якщо послідовність є неправильною. Дужкова послідовність вважається правильною, якщо всі дужки можна розбити попарно "відкриваюча"-"закриваюча", при чому в кожній парі закриваюча дужка слідує після відкриваючої
#  TASK
# String consisting of opening and closing parentheses is a command line argument.
# YES "if the input line contains the correct parenthesis, or" NO "if the sequence is incorrect. 
#The parenthesis is correct if all the brackets can be broken in pairs" opening "-" closing ", with in each pair the closing bracket follows after the opening

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
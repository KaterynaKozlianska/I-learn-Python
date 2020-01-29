# TASK:
#  String consisting of opening and closing bracket is a command line argument.
#  YES "if the input line contains the correct bracket, or" NO "if the sequence is incorrect. 
#   The bracket is correct if all the brackets can be broken in pairs "opening" - "closing", with in each pair the closing bracket follows after the opening

import sys
opening=str("(")
closing=str(")")
flag=True

x=str(sys.argv[1:])
x=x.replace(",","").replace("[","").replace("]","").replace("'","").replace(" ","")

if (len(x))%2==0 and len(x)>0:
 for i in range (len(x)//2):
  i=i*2
  if x[i]==opening[0] and x[(i+1)]==closing[0]:
   flag
  else:
   flag=False
elif len(x)<1:
 flag=False
 print ('Please input more then zero symbols')
else: 
 flag=False

if flag:
 print ("YES")
else:
 print ("NO")
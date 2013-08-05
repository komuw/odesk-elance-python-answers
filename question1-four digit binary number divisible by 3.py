"""1. time(10min) 
Write a program which will accept 4 digit binary numbers each separated by a comma as its input and then check whether they are divisible by 3 or not. The numbers that are divisible by 3 are to be printed, separated by a comma.

Example
Suppose the following input is given to the program:
0011,0100,0101,1001
Then, the output of the program should be:
0011, 1001
Note: You should assume that input to the program is from console input (raw_input)
"""
x=raw_input("please enter 4 binary numbers separated by a comma")
#print "x is:", x, "\n"  #for debugging purposes
a=x[0:4] #slicin isn't inclusive of outer limit
b=x[5:9] #1010
c=x[10:14]
d=x[15]+x[16]+x[17]+x[18]

#convert the 4 binary numbers to base10
a_dec=(int(a[3])*1)+(int(a[2])*2)+(int(a[1])*4)+(int(a[0])*8) #3
b_dec=(int(b[3])*1)+(int(b[2])*2)+(int(b[1])*4)+(int(b[0])*8)
c_dec=(int(c[3])*1)+(int(c[2])*2)+(int(c[1])*4)+(int(c[0])*8)
d_dec=(int(d[3])*1)+(int(d[2])*2)+(int(d[1])*4)+(int(d[0])*8)

list=[]
if (a_dec%3==0):
  list.append(a)
else:
	pass
if (b_dec%3==0):
	list.append(b)
else:
	pass
if (c_dec%3==0):
	list.append(c)
else:
	pass
if (d_dec%3==0):
	list.append(d)
else:
	pass
	
for i in list:
	print i+",",





"""8. (8min) 
Write a program to calculate the bill amount, in cents, for the units of power consumed. Following are the rates applicable:
1. First 0-100 units: 60 cents per unit
2. Next 200 units: 70 cents per unit
3. Beyond 300 units: 80 cents per unit
The program should accept three different usage unit readings.

Example
If the following inputs are supplied:
305
180
120
Then, the output should be:
20400
11600
7400
Note: You should assume that input to the program is from console input (raw_input

a=raw_input("input the first unit reading")
b=raw_input("input the second unit reading")
c=raw_input("input the third unit reading")
a=int(a)
b=int(b)
c=int(c)
print "\n calculating price.... . ..."
print "..... .. .\n"

def elec_price(x):
  if x in range(0, 101):
		price=x*60
	elif x in range(101, 301):
		price=(100*60)+((x-100)*70)
	else:
		price=(100*60)+(200*70)+((x-300)*80)
	print price

elec_price(a)
elec_price(b)
elec_price(c)
print "\n"





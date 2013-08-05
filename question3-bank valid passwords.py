"""3. (10min)
A bank has implemented criteria for determining whether the transaction passwords typed by customers of the bank are valid or not.
Following are the criteria for checking the transaction password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [*#+@]
4. Minimum length of transaction password: 4
5. Maximum length of transaction password: 6
6. No space is allowed
Write a program which will accept a sequence of comma separated transaction passwords and will check them according to the bank's criteria. Passwords that match the criteria are to be printed, each separated by a comma."""
import re
pass_list=raw_input("Enter the passwords, they should be comma separated> ")
y=pass_list.split(",") #produce an array of passwords
#print y
#password="k$u9@J"
def pass_checker(s):
  a=re.compile(r"[a-z]")
	b=re.compile(r"[0-9]")
	c=re.compile(r"[A-Z]")
	d=re.compile(r"[*#+@]")
	d2=re.compile("[\s]") #will be true if there's white space
	if len(s) in range(4, 7):
		if (a.search(s) and b.search(s) and c.search(s) and d.search(s) and not d2.search(s)):
			print s+",",
		else:
			pass
	else:
		pass


for x in y:  #take each pass & check if it meets creteria
	pass_checker(x)





import random

#A function to shuffle the characters in a string
def shuffle(string):
	templist = list(string)
	random.shuffle(templist)
	return ''.join(templist)

#Program starts here
upper1=chr(random.randint(65,90)) #Generate random uppercase letter based on ASCII
upper2=chr(random.randint(65,90)) #Generate random uppercase letter based on ASCII
lower1=chr(random.randint(97,122)) #Generate random lowercase letter
lower2=chr(random.randint(97,122)) #Generate random lowercase letter
num_1=chr(random.randint(48,57)) #Generate random number
num_2=chr(random.randint(48,57)) #Generate random number
sym_1=chr(random.randint(35,38)) #Generate random symbol
sym_2=chr(random.randint(60,64)) #Generate random symbol


# Generate password using all the characters in a random order
password = upper1 + upper2 + lower1 + lower2 + num_1 + num_2 + sym_1 + sym_2
#password = shuffle(password)

#output
print(password)
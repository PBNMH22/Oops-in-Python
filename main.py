# args and kwargs in python 

''' Please un-comment print to see results '''

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)


subject = ['Math', 'Art']
info = {'name': 'Deepak', 'age': 25}

student_info(*subject,**info)


work_hours = [('Deepak', 100), ('Chnadu', 200), ('Deva', 300)]

def myfunc(**kwargs):

	if 'fruit' in kwargs:
		print('my fruit is {}'.format(kwargs['fruit']))

	else: 
		print('I did not find any fruit here')

myfunc(fruit= 'Apple', veg = 'Flower')

# Tuple unpacking using functions in python 

def emp_check(work_hours):
	current_max = 0
	emp_name = ''

	for emp,hour in work_hours:
		if current_max<hour:
			current_max = hour
			emp_name = emp

		else:
			pass

	return emp_name,current_max


name,hours = emp_check(work_hours)
print(f'employee of the month {name}, hours spent in a month {hours}')
			

# interaction between functions 
# Simple guessing game 
"""Three cup Monte"""


example = [1,2,3,4,5,6,7]

# importing shuffle module 

from random import shuffle 

shuffle(example)

#print(example)

# function to shuffle list 

def shuffle_list(result):
	shuffle(result)
	return result

result = shuffle_list(example)
print(result)

mylist = [' ', 'O', ' ']

#print(shuffle_list(mylist))

# defining a function to take player guess

def player_guess():

	guess = ''

	while guess not in ['0', '1', '2']:
		
		guess = input('enter a number 0,1 or 2 ' )
	return int(guess)

def check_guess(mylist, guess):

	if mylist[guess] == 'O':
		print('Congratulations !!! Your guess is correct.')

	else:
		print('Incorrect guess')
		print(mylist)

# initial list
mylist = [' ', 'O', ' ']

# shuffle list
mixed_list = shuffle_list(mylist)

# user guess
guess = player_guess()

# check_guess
check_guess(mixed_list, guess)



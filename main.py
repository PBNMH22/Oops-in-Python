
def student_info(*args, **kwargs):
	print(args)
	print(kwargs)


subject = ['Math', 'Art']
info = {'name': 'Deepak', 'age': 25}

student_info(*subject,**info)


work_hours = [('Deepak', 100), ('Mayuri', 200), ('Shilpa', 300)]

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
print(name)
			
	


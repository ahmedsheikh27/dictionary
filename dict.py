# Student dictionary

student = {
    "name":'Ahmed',
    "age":'18',
    "grade":'A+',
    'city':'Uk'
}
student['city'] = 'New York'
student['age'] = '20'
del student['city']
# grade = student['grade']
for student_key in student.values():
    print(student_key)
for student_value in student.keys():
    print(student_value)
for student_key,student_value in student.items():
    print(student_key + ' : ' + student_value)    
if "grade" in student:
    print('True, grades exist')
else :
    print('False, grades does not exist')

total_keys = len(student.keys())
print(total_keys)
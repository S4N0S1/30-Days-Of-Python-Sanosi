dog = {} #1
dog['name'] = 'Baxter'
dog['color'] = 'White'
dog['breed'] = 'Chiuaua'
dog['legs'] = 4
dog['age'] = 3
print(dog) #2

student = {
    'name':'Ahmed',
    'surname':'Sanosi',
    'gender':'male',
    'age':'??',
    'martial status':'single variable calculus',
    'skills':['professional sleeping','graphic design', 'animation','primitive coding'],
    'country':'Sudan',
    'city':'Khartoum',
    'address':'Square 1'
} #3

print(len(student)) #4

skills_type = type(student['skills']) #5
print(skills_type)

# student['skills'] = student['skills'].append('Turkish') #! Wrong
student['skills'].append('Turkish') #6
student['skills'].append('CAD Modeling')
print(student['skills'])

skeys = student.keys() #7
print(skeys)

svalues = student.values() #8
print(svalues)

stuple = student.items() #9
print(stuple)

student.pop('martial status')
print(student)

del student
print(student)
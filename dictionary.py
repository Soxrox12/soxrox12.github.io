people = {
    'Mom':43,
    'Dad':51,
    'Eli':6,
    'Francesca':17,
    'Olivia':21,
    'Adrianna':19,
    'Anna':18,
    'Katie':19,
    "All Friends":['Francesca','Olivia', 'Adrianna', 'Anna', 'Katie'],
    'Family': ('Mom', 'Dad', 'Eli')
    }
print(people)
print('My mom is ' + str(people['Mom']) + '.')
print('My dad ' + str(people['Dad']) + '.')
print('My brother ' + str(people['Eli']) + '.')
print('My best friend is ' + str(people['Olivia']) + '.')
print('My friends are: ' + str(people['All Friends']))
print('My family members are: ' + str(people['Family']))
#print(people['Family'[1]])

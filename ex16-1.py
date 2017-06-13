from sys import argv 

script    = argv
file_name = argv[1]

print('Please fill app all info We are asking You! We will save your file log')
print('**********************************************************************')
print('***************** Opening the file ***********************************')

file = open(file_name, 'w')

print ("Truncating the file.  Goodbye!")
file.truncate()
print ("I will ask you few questions.")

#full_name = input('Please add your First & Last Name? ')
dob  = input('Add your date of birt? ')
age  = input('Please add your current age? ')
city = input('Where are you born, please add city? ')

print ("All your info will be saved in file: ", file_name)

file.write(full_name, '/n',dob, '/n', age, '/n', city)

print("Plase check your ", file_name)
file.close()



students = int (input ('Enter the number of students in the class: '))
number_of_pcs = int (input ('Enter the number of PCs in the lab: '))
number_of_classes = students // number_of_pcs


if number_of_pcs <= 25:
    print ('You need 2 labs for all the students')
else:
    print('You need 1 lab for all the students')
students = int (input ('Enter the number of students in the class: '))
number_of_pcs = int (input ('Enter the number of PCs in the lab: '))
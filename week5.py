students = int (input ('Enter the number of students in the class: '))
if students <= 0:
    print('You need at least 1 student')
else:
    number_of_pcs = int (input ('Enter the number of PCs in the lab: '))

    if number_of_pcs <= 0:
        print('You need at least 1 lab')
    full_lab = students // number_of_pcs
    labs_remaining = students % number_of_pcs
    if labs_remaining >= 1:
        print('You need', full_lab+1, 'labs')
    else:
        print('You need', full_lab, 'labs')
def valid_email (email, domain):

    if email.count ('@') !=1:
        print('An @ is required')
    if email [0] == '@':
        print('Needs characters before the @')
    if email [email.find ('@') -1:] != domain:
        print('Enter a valid domain')
    else:
        print(email, 'is valid at', domain)
domain = 'pop.ac.uk'
email = str(input('Enter Your UOP E-mail Address: '))
valid_email(email,domain)


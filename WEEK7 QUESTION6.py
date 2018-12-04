print("Welcome to PopChat. The University of Poppleton's Online Chat")
def valid_email (email, domain):

    if email.count ('@') !=1:
        print('An @ is required')
    if email [0] == '@':
        print('Needs characters before the @')
    if email [email.find ('@') +1:] != domain:
        print('Enter a valid domain')
    else:
        print(email, 'is valid at', domain)

domain = 'pop.ac.uk'
email = str(input('Please Enter your E-mail Address: '))

x = email.split("@")
print(x[0])

if x [1] == 'pop.ac.uk':
    print('My name is ' + (x[0]) + ' and I will be happy to help you today.')
else:
    print('Enter a valid domain')

print('Hello' + (x[0]) + '. How can I help today?')
def string_word(question, word):
    if word in question:
        return True
    else:
        return False
domain = 'unipop.ac.uk'
for count in range (3):
    question = input('Enter the question: ')
    word = input('Enter the answer: ')
    print(string_word(question, word))
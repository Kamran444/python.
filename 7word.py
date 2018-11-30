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
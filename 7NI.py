def ni():
    while 1:
        nii = input('Enter a word: ')
        input_entered = nii.lower()
        print(input_entered)
        if input_entered == 'ni!':
            print('correct')
            exit()
        else:
            print('Incorrect, please try again')
ni()
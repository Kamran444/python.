username = input('Enter your username')
studentid = input('Enter student id')
changed_password = input('Enter your new password')
confirm_password = input('Enter your new password again')
while changed_password:
    if changed_password != confirm_password:
        print('Incorrect. Passwords do not match, try again.')
        changed_password = input('Enter your new password')
        confirm_password = input('Enter your new password again')

    elif changed_password in ('huddersfield', 'justinbieber', 'canalside', 'cheese', studentid, username):
        print('Invalid password, try again')
        changed_password = input('Enter your new password')
        confirm_password = input('Enter your new password again')
    elif len(changed_password)<6 or len(changed_password)>12:
    print('Password must be within 6 & 12 characters')
    changed_password = input('Enter your new password')
    confirm_password = input('Enter your new password again')
    else:
    changed_password == confirm_password
    break
print('Password has successfully been modified')
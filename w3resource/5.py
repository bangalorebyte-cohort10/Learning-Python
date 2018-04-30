#!/usr/bin/env python3

firstname = input('Enter first name ')
lastname = input('Enter last name ')
fullname = firstname + ' ' + lastname
n = len(fullname)
print(fullname[-1:-n])

print(''.join(reversed(fullname)))

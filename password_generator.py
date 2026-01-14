#Random password Generator

import random
import string

#print(string.ascii_letters);
#print(type(string.ascii_letters))
#print(string.digits)
#print(string.punctuation);

password_len = 12;
charValues = string.ascii_letters + string.digits + string.punctuation;
#print(charValues);
'''
password = "";
for i in range(password_len):
    password += random.choice(charValues);


print("Your random password is: ", password);

'''
#List comprehension [function for i in range(n)]
password_len = 8;
result = "".join([random.choice(charValues) for i in range(password_len)]);
print(result);

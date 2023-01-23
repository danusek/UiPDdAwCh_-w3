import random
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
all = upper +lower+number+symbol 
length = random.randint(12,20)
password = ''.join(random.sample(all,length))
print("Your Password is: "+ password)
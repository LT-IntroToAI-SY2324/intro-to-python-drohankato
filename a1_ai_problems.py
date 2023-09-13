# Complete your individualized AI problems here

# def fizbuzz(input_num):
#     if(input_num%3==0):
#         if(input_num%5==0):
#             return 'FizzBuzz'
#         return 'Fizz'
#     elif(input_num%5==0):
#         return 'Buzz'
#     else:
#         return input_num

# assert fizbuzz(1) == 1, "fizzbuzz 1 test"
# assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
# assert fizbuzz(4) == 4, "fizzbuzz 4 test"
# assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
# assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
# assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"




# #random number game

# import random 
# secret_number= random.randint (1,100)
# guess = 10

# while guess !=secret_number:
#     guess=int(input("guess the secret number (1-100):" ))
#     if guess < secret_number:
#         print ("too low, try again" )
#     elif guess > secret_number:
#         print ("too high try again")
#     else:
#         print ("congrats you did it!!!")



#password maker 

import random
import string

def generate_password(length=12):
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password = generate_password(10)  # You can specify the desired length here
print("Generated Password:", password)

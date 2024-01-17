#!/usr/bin/env python
# coding: utf-8

# In[2]:


EXCLUDED_NUMBERS = [1, 5000]

def welcome_message():
    print('Prime Number Checker')
    print()

def prime_checker(number):
    if number < 2:
        return False 
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False 
    return True 

def count_factors(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return count

def main():
    welcome_message()
    try_again = True
    while try_again:
        try:
            num = int(input('Please enter an integer between 1 and 5000: '))
            if num in EXCLUDED_NUMBERS:
                print('Invalid integer. Please try again.')
            elif 1 <= num <= 5000:
                if prime_checker(num):
                    print(f'{num} is a prime number.')
                else:
                    print(f'{num} is NOT a prime number.')
                    factor_count = count_factors(num)
                    print(f'It has {factor_count} factors.')
                    
                print()
                choice = input('Try again? (y/n): ')
                print()

                if choice != 'y':
                    try_again = False
                    print('Bye!')
            else:
                print('Invalid integer. Please try again.')
        except ValueError:
            print('Invalid integer. Please try again.')

if __name__ == '__main__':
    main()


# In[ ]:





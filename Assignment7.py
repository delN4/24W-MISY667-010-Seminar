#!/usr/bin/env python
# coding: utf-8

# In[1]:


def welcome_message(): 
    print('Feet and Meter Converter')
    print()
    
def menu_function():
    print('Conversions Menu:')
    print('a. Feet to Meters')
    print('b. Meters to Feet')
    
def to_meters(feet):
    meters = feet * 0.3048
    return meters 

def to_feet(meters):
    feet = meters / 0.3048 
    return feet  

def main(): 
    welcome_message()
    menu_function()
    while True: 
        welcome_message()
        choice = input ('Select a conversion (a/b): ')
        print()
        if choice == 'a':
            feet = float(input('Enter feet: '))
            meters = to_meters(feet)
            print(round(meters, 2), 'meters')
        elif choice == 'b':
            meters = float(input('Enter meters: '))
            feet = to_feet(meters)
            print(round(feet, 2), 'feet')
        else:
            print('You did not enter a proper conversion')
        print()
        
        more = input('Would you like to perform another conversion? (y/n): ')
        print()
        
        if more !='y':
            print('Thank you, bye!')
            break
            
if __name__ == '__main__':
    main()


# In[ ]:





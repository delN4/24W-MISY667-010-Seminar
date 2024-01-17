#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('The Test Score Program')
print()

more_test = 'y'

while more_test.lower() == 'y':
    print('Enter test scores')
    print("Enter 'end' to end input")
    print('=======================')
    
    counter = 0
    score_total = 0
    test_score = 0
    
##    while True:
##        test_score = input("Enter test score: ")
##        if test_score.lower() == "end":
##            break
##        else:
##            test_score = int(test_score)
##            if test_score >= 0 and test_score <= 100:
##                score_total += test_score
##                counter += 1
##            else:
##                print(f"Test score must be from 0 through 100. "
##                      f"Score discarded. Try again.")

    while (test_score := input('Enter test score:  ').lower()) != 'end':
        test_score = int(test_score)
        if test_score >= 0 and test_score <= 100:
            score_total += test_score 
            counter += 1
        else: 
            print(f'Test score must be from 0 through 100. '
                  f'Score discarded. Try again.')
            
    # calculate average score 
    average_score = round(score_total / counter)
    
    # format and display result 
    print('=====================')
    print(f'Total Score: {score_total}'
          f'\nAverage Score: {average_score}')
    
    
    print()
    more_test = input('Enter another set of test scores (y/n)?')
    print()
    
print('Bye!')


# In[ ]:





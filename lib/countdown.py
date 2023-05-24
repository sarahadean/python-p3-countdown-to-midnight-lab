# Write a function countdown() that takes in an integer argument and uses a while loop to countdown from that integer to 1, outputting f'{number} SECOND(S)!' in each iteration of the loop. The function should print() "HAPPY NEW YEAR!" after the loop finishes:

def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    if number == 0:
        print('HAPPY NEW YEAR!')

# print(countdown(15))

# one integer argument for the countdown and makes the loop pause for one second each trip around
import time
def countdown_with_sleep(number): 
    while number > 0:
        # time.sleep(1)
        print(f'{number} SECOND(S)!')
        number -= 1
        time.sleep(1)
    if number == 0:
        print('HAPPY NEW YEAR!')
    

print(countdown_with_sleep(5))
import random

num = random.randint(1,20)

print("\nChoose level of the game: FROM 3 - expert TO 6 - beginner")
i = int(input())

print("What is your name?")
name = input()
print(f"\nYou know {name}... \ni am thinking about a number \nfrom 1 to 20. \nTry to guess \nYou have {i} attempts.")

#print(number)
for j in range(i):
    number = int(input())
    if number<num:
        print("NO! Your answer is wrong, given number is to small")
        print("Try again!")
   
    elif number>num:
        print("NO! Your answer is wrong, given number is to big")
        print("Try again!")
    
    else:
        print(f"Well done! You needed {j+1} attempts")
        break 

if number != num:
        print(f"Unfortunatelly you didn't make it :( Corect answer: {num}")

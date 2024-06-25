import random
n = random.randint(1, 50)
a = -1
guess = 0
while(a !=n  ):
    guess += 1
    a = int(input("Guess the number: "))
    if( a > n):
        print("Lower number please")
    else:
        print("Higher number please")
        
print(f"Yes you got the number in {guess} attempt")
        
    
import random as r

def isPrime(num):
    isPrime = True
    if num == 0 or num == 1:
         isPrime = False
    else:
        for i in range(2, num):
            remainder = num % i
            if remainder == 0:
                isPrime = False
                break
        return isPrime

def nameNumbers():
    counter=2
    while True:
        if isPrime(counter):
            print(counter)
        counter+= 1

def checkNumbers(num):
    if isPrime(num):
         print("Yes")
    else:
         print("No")
def game():
    points = 0
    lives = 3
    while True:
        num = r.randint(2, 55171)
        answer = input("Is " + str(num) + " prime? (yes or no, or quit)")
        if answer.lower() == "yes":
            numcheck = True
        elif answer.lower() == "no":
            numcheck = False
        elif answer.lower() == "quit":
            print("Thanks for playing! Final score: " + str(points))
            break
        else:
            print("Invalid input")
        if isPrime(num) == numcheck:
            points += 1
            print("Correct! Points: " + str(points))
        else:
            lives -= 1
            print("Wrong! Lives: " + str(lives))
        if lives == 0:
            print("Game over! Final score: " + str(points))
            break

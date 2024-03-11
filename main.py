import prime as p

while True:
    action = input("Enter a number to choose your option:\n1: Name every prime number.\n2: Check individual prime numbers.\n3: Play a prime number game.")

    if action == "1":
        p.nameNumbers()
    elif action == "2":
        num = int(input("What number should be checked?"))
        p.checkNumbers(num)
    elif action == "3":
        p.game()
    else: 
        print("Invalid input")


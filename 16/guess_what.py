import random

number = random.randint(1, 100000)
guesses = 0

while True:
    guess = int(input("Uhodni cislo: "))
    guesses += 1
    
    if guess == number:
        print("Gratulace uhodl jsi cislo na", guesses, "pokus.")
        break
    elif guess > number:
        print("Moc vysoky, zkus znovu.")
    else:
        print("TMoc nizko, zkus znovu.")

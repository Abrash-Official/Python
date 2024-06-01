import random
print("Well'Come to number guessing game")
secret_number=random.randrange(1,100)
attempt=0
while True:
    attempt +=1
    guess_number=int(input("Wrote a number between 1 & 100:"))
    if secret_number<guess_number:
        print("To high try a lower one")
    elif secret_number>guess_number:
        print("To low try a higher one")
    else:
        print(f"Wow!you guess the secret number:{secret_number} in {attempt} attempt!")
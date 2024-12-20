

print("Welcome to my game")
name = input("What is your name?")
age = int(input("What is your age?"))

health = 10

if age >= 18:
    print("Your are old enough to play")

    wants_to_play = input ("Do you want to play? (yes/no)").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health")
        print ("Lets play")
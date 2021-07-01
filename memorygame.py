hidden = []
while len(hidden) < 12:
    import random
    x = random.randrange(1 , 7) # numbers beetween 1-6
    if hidden.count(x) != 2:
        hidden.append(x)

print(hidden)

# 0 for close , 1 for open , 2 for temporary open
situation = [0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]

attempts = 0
attempts_list = []
open_cards = situation.count(1)
answer = "Yes"

while answer == "Yes":

    if open_cards == 12:
        situation = [0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
        open_cards = 0
        attempts = 0
    
    choice_1 = int(input("Choose the first card: "))
    while choice_1 < 0 or choice_1 > 11 or situation[choice_1] != 0: 
        if choice_1 < 0 or choice_1 > 11:
            choice_1 = int(input("I want a card between 0...11: "))
        else:
            choice_1 = int(input("The card must be close! "))
        

    choice_2 = int(input("Choose the second card: "))
    while choice_2 < 0 or choice_2 > 11 or situation[choice_2] != 0 or choice_1 == choice_2: 
        if choice_2 < 0 or choice_2 > 11:
            choice_2 = int(input("I want a card between 0...11: "))
        elif situation[choice_2] != 0:
            choice_2 = int(input("I want a closed card: "))
        else:
            choice_2 = int(input("The second choice must be diferrent from the first! "))
        
    print("")
    situation[choice_1] = 2
    situation[choice_2] = 2
    print("The current situation is " + str(situation))
    print("")

    if hidden[choice_1] == hidden[choice_2]:
        print("These cards are the same! ")
        situation[choice_1] = 1
        situation[choice_2] = 1
    else:
        print("These cards doesn't match! ")
        situation[choice_1] = 0
        situation[choice_2] = 0
    print("")
    print("The current situation is " + str(situation))
    print("")
    
    attempts += 1

    open_cards = situation.count(1)
    if open_cards == 12:

        print("You win with " + str(attempts) + " attempts")
        print("")

        answer = str(input("Do you want to play again? (yes/no): "))
        while answer != "yes" and answer != "no":
            answer = input("Do you want to play again? (Yes/No): ")
        

        attempts_list.append(attempts)

print("")
print("High score attempts was: " + str(min(attempts_list)))
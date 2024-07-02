import random

print('''
Game Info:
    Random number will be rolled between 1 and 7.
    If player rolls 1, score will be set back to 0 and turn will be end.
    If one of the player reaches to the max score, game will end.
    ''')

while True:
    try:
        player_count = int(input(f"Max score set as {(max_score:=int(input('What is the max score for the game? ')))}. How many player will join? [2-4] "))
        if 2 <= player_count <= 4:
            player_scores = [0 for _ in range(player_count)]
            break
        else:
            print("Player count should be between 2 and 4.", end="\n\n") 
            continue
    except:
        print("Please choose a number.", end="\n\n")

for i in range(player_count):  
    print()
    print(f"> Player {i+1} your turn started! Current highest score is {max(player_scores)}.")
    while max(player_scores) < max_score:
        roll = input(f"Press any key to play or q for quit ")
        if roll != 'q':
            random_number = random.randint(1,7)
            if random_number != 1:
                player_scores[i] += random_number
                print(f"Number is {random_number}, your score is {player_scores[i]}.")
                continue
            else:
                player_scores[i] = 0
                print(f"Number is {random_number}, your score is {player_scores[i]} and turn ended.")
                break
        else:
            break
    else:
        break
print()   
if max(player_scores) != 0:
    print(f">> Player {player_scores.index(max(player_scores)) + 1} won the game!", end="\n\n")
else:
    print(">> No one won the game!", end="\n\n")
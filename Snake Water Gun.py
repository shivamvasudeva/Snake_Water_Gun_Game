import random
# Computer has its choice
try_count = 1
comp_score = 0
player_score =0
tie_games = 0
while (try_count <=5):
    comp_list = ['s', 'w', 'g']
    computer = random.choice(comp_list)
    print(" Press s for Snake")
    print(" Press w for Water")
    print(" Press g for Gun")
    player = input("Enter your choice: ")
# If player choose snake
    if player == computer:
        print("Its a Tie")
        print("No Score to both players")
        tie_games = tie_games+1
    elif player == 's' and computer == "w":
        player_score =player_score+1
        print('Player Won!!')
    elif player == 'w' and computer == "s":
        comp_score=comp_score+1
        print('Computer Won!!')
    elif player == 'w' and computer == "g":
        player_score = player_score + 1
        print('Player Won!!')
    elif player == 'g' and computer == "w":
        comp_score =comp_score+1
        print('Computer Won!!')
    elif player == 'g' and computer == "s":
        player_score = player_score + 1
        print('Player Won!!')
    elif player == 's' and computer == "g":
        comp_score =comp_score+1
        print('Computer Won!!')
    else:
        print('Invalid input')
        continue

    print(f"Number of plays left: {5-try_count}")
    try_count = try_count + 1
    if try_count > 5:
        print('End!!!!!!!!')

print(f"Computer Won: {comp_score} number of playes")
print(f"Player Won: {player_score} number of plays")
print(f"Tied Games: {tie_games}")
if comp_score > player_score:
    print(">>>>>>>>>>>.Computer WON the Game!!!!!")
else:
    print(">>>>>>>Player WON the Game!!!!!")


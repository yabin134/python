#RPG game
import random
def game():
    player=input("Enter the players name:")
    enemy=['Dragon','Lion','Dino','Wild Pokemon']
    place=['Hills','Jungle','Street','Beach']

    renemy=random.choice(enemy)
    rplace=random.choice(place)
    print(f'{player} encounters {renemy} at the {rplace}')

    print("\n THE BATTLE BEGINS........")


    playerhealth=100
    enemyhealth=100        
    while playerhealth>0 and enemyhealth>0:
        playerattack=random.randint(1,20)
        enemyhealth=enemyhealth-playerattack

        enemyattack=random.randint(1,20)
        playerhealth=playerhealth-enemyattack
        print(f'{renemy} has attacked and {player}s Health is {playerhealth}')
        print(f'{player} has attacked and the {renemy} Health is {enemyhealth}')
        print( "\n ")

    if playerhealth<0:
        print(f"{player} has been defeated")

    elif enemyhealth<0:
        print(f"{renemy} has been defeated")
            
game()
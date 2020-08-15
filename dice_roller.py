import random
dice_rolls=4
dice_sum=0
for i in range(0,dice_rolls):
    roll=random.randint(1,6)
    dice_sum += roll
    print(f'You rolled a {roll}')
print(f"you have rolled a total of {dice_sum}")

enemies =1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


#There is no Block scope in Python

game_level = 3
enemies_list = ['Skeleton', 'Zombie', 'Alien']
if game_level < 5:
    new_enemy = enemies_list[0]

print(new_enemy)



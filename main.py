from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy1 = Character("Goblin1", 20, 3)
    enemy2 = Character("Goblin2", 20, 3)

    print(hero)
    print(enemy1)
    print(enemy2)
    print()

    while hero.is_alive() and enemy1.is_alive() and enemy2.is_alive() :
        hero.attack(enemy1)
        hero.attack(enemy2)
        if enemy1.is_alive():
            enemy1.attack(hero)
        if enemy2.is_alive():
            enemy2.attack(hero)
        print(hero)
        print(enemy1)
        print(enemy2)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    elif enemy1.is_alive():
        print(f"{enemy1.name} wins!")
    elif enemy2.is_alive():
        print(f"{enemy2.name} wins!")
    elif enemy1.is_alive() and enemy2.is_alive():
        print(f"{enemy2.name} and {enemy1.name} wins!")

if __name__ == "__main__":
    main()


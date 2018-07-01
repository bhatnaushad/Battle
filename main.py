from classes.game import BColors, Person


magic = [{"name": "Fire", "cost": 10, "damage": 100},
         {"name": "Thunder", "cost": 15, "damage": 120},
         {"name": "Blizzard", "cost": 10, "damage": 100}]


player = Person(400, 90, 60, 30, magic)

# print(player.generate_damage())
# print(player.generate_damage())
# print(player.generate_damage())
# print(player.generate_damage())
#
# print(player.generate_spell_damage(0))
# print(player.generate_spell_damage(2))
#
# print(player.take_damage(40))
# print(player.get_spell_name(2))
# print(player.get_spell_cost(1))
# print(player.get_max_hp())

# we will create an enemy now - enemy also is a person
enemy = Person(600, 70, 50, 20, magic)

running = True

print(BColors.FAIL + BColors.BOLD + "AN ENEMY ATTACK" + BColors.ENDC + " Get ready")

while running:
    print("=======================")
    player.choose_action()
    choice = input("Enter a choice: ")
    index = int(choice) - 1    # as index is 1 in choose_action() function
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)  # we are attacking the enemy
        print("you attacked the enemy for = ", dmg, " points of damage. New Enemy Hp = ", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        # magic_dmg = player.generate_spell_damage(magic_number)

    enemy_choice = 1  # Not understood

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked you for = ", enemy_dmg, " points. Your New Hp = ", player.get_hp())

    if enemy.get_hp() == 0:
        print(BColors.OKGREEN + "You won. Hurray! " + BColors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(BColors.FAIL + " You have been defeated. :( " + BColors.ENDC)
        running = False



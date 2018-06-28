from classes.game import BColors, Person


magic = [{"name": "Fire", "Cost": 10, "damage": 60},
         {"name": "Thunder", "Cost": 10, "damage": 70},
         {"name": "Blizzard", "Cost": 10, "damage": 80}]


player = Person(400, 90, 60, 30, magic)

print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
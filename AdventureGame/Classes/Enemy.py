# Base class
class Enemy:
    # Constructor
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    # Damaged the enemy object by a given amount
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            print(f"You defeated the {self.name}!")

    # Shows information of the instance
    def to_string(self):
        print(f"Name: {self.name}, HP: {self.hp}, Damage: {self.damage}")

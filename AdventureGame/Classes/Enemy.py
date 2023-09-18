# Base class
class Enemy:
    # Constructor
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    # Damaged the enemy (object) by a given amount
    # Child classes inherits this function
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            print(f"You defeated the {self.name}!")

    # Shows the stats of the enemy (object)
    # Child classes inherits this function
    def show_stats(self):
        print(f"{self.name}: {self.hp} hp and {self.damage} damage")


# Child class of enemy with its own attribute values
class Skeleton(Enemy):
    def __init__(self):
        self.name = "Skeleton"
        self.hp = 50
        self.damage = 10
        super().__init__(self.name, self.hp, self.damage)


# Child class of enemy with its own attribute values
class Troll(Enemy):
    def __init__(self):
        self.name = "Troll"
        self.hp = 100
        self.damage = 15
        super().__init__(self.name, self.hp, self.damage)

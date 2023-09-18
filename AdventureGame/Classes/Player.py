class Player:
    # Constructor
    def __init__(self, name, max_hp, damage):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage

    # Increases the players hp by a given amount
    def increase_max_hp(self, amount):
        self.max_hp += amount

    # Increases the players damage by a given amount
    def increase_damage(self, amount):
        self.damage += amount

    # Heals the player by a given amount
    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    # Damages the player by a given amount
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    # Checks if the player is alive by having more than 0 health
    def is_alive(self):
        return self.hp > 0

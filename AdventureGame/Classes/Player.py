class Player:
    # Constructor
    def __init__(self, name, max_hp, damage):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage

    def set_player_name(self, name):
        self.name = name

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
            print(f"{self.name}, the sinister depths of Murkwood have proven too perilous for you. As the darkness "
                  f"envelops your life force, your final words echo through the haunted forest, 'Help me!' Your "
                  f"journey in Murkwood has come to a tragic end.")

    def to_string(self):
        print(f"Name: {self.name}, HP: {self.hp}, Damage: {self.damage}")

    # Checks if the player is alive by having more than 0 health
    def is_alive(self):
        return self.hp > 0

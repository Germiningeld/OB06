class Hero():
    def __init__(self, name: str, health: int = 100, attack_power: int = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def __str__(self):
        return f"{self.name} has {self.health} health and {self.attack_power} attack power"

    def attack(self, target):
        target.health -= self.attack_power

    det is_alive(self):
        return self.health > 0

        
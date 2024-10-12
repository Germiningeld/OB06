import random

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

class Game():
    def __init__(self, player: Hero, computer: Hero):
        self.player = player
        self.computer = computer

    def get_initiative(self):
        self.player_initiative = random.randint(0, 3)
        self.computer_initiative = random.randint(0, 3)

        if self.player_initiative >= self.computer_initiative:
            print(f"Инициативу получил {self.player.name}")
            return self.player
        if self.computer_initiative > self.player_initiative:
            print(f"Инициативу получил {self.computer.name}")
            return self.computer

    def start(self):
        initiator = self.get_initiative()
        while self.player.is_alive() and self.computer.is_alive():
            if initiator == self.player:
                self.player.attack(self.computer)
                print(f'Игрок {self.player.name} атаковал {self.computer.name}')
                print(f'У {self.computer.name} осталось {self.computer.health} жизней')
                print(f'У {self.player.name} осталось {self.player.health} жизней')
                initiator = self.computer

            else initiator == self.computer:
                self.computer.attack(self.player)
                print(f'Игрок {self.computer.name} атаковал {self.player.name}')
                print(f'У {self.computer.name} осталось {self.computer.health} жизней')
                print(f'У {self.player.name} осталось {self.player.health} жизней')
                initiator = self.player


        if self.player.is_alive():
            print(f'Победил {self.player.name}')
            print(f'Осталось жизней {self.player.health}')
        else:
            print(f'Победил {self.computer.name}')
            print(f'Осталось жизней {self.computer.health}')

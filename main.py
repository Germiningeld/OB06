import random

class Hero():
    def __init__(self, name: str, health: int = 100, attack_power: int = 20):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.last_attack = 0

    def __str__(self):
        return f"{self.name} has {self.health} health and {self.attack_power} attack power"

    def attack(self, target):
        self.last_attack = self.attack_power - int(self.max_health / self.health) + random.randint(-5, 5)
        target.health -= self.last_attack

    def is_alive(self):
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
        i = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"Ход {i}")
            if initiator == self.player:
                self.player.attack(self.computer)
                print(f'Игрок {self.player.name} атаковал {self.computer.name} с силой {self.player.last_attack}')
                print(f'У {self.computer.name} осталось {self.computer.health} жизней')
                print(f'У {self.player.name} осталось {self.player.health} жизней')
                initiator = self.computer

            else:
                self.computer.attack(self.player)
                print(f'Игрок {self.computer.name} атаковал {self.player.name} с силой {self.computer.last_attack}')
                print(f'У {self.computer.name} осталось {self.computer.health} жизней')
                print(f'У {self.player.name} осталось {self.player.health} жизней')
                initiator = self.player

            print('')
            i += 1


        if self.player.is_alive():
            print(f'Победил {self.player.name}')
            print(f'Осталось жизней {self.player.health}')
        else:
            print(f'Победил {self.computer.name}')
            print(f'Осталось жизней {self.computer.health}')


hero = Hero('Бесшумный ливень', 100, 20)
computer = Hero('Капля огня', 100, 20)
game = Game(hero, computer)
game.start()
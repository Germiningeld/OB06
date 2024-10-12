import random

class Hero():
    def __init__(self, name: str, health: int = 100, attack_power: int = 20):
        # Инициализация героя с именем, здоровьем и силой атаки
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.last_attack = 0

    def __str__(self):
        # Строковое представление героя
        return f"{self.name} имеет {self.health} здоровья и {self.attack_power} силы атаки"

    def attack(self, target):
        # Метод атаки: рассчитывает урон и применяет его к цели
        # Урон зависит от силы атаки, текущего здоровья и случайного фактора
        # Расчет силы атаки
        health_percentage = self.health / self.max_health
        attack_percentage = 0.5 + (health_percentage * 0.5)
        base_attack = self.attack_power * attack_percentage

        # Добавляем случайный фактор
        self.last_attack = int(base_attack + random.randint(-5, 5))

        # Убеждаемся, что атака не будет отрицательной
        self.last_attack = max(0, self.last_attack)

        target.health -= self.last_attack

    def is_alive(self):
        # Проверка, жив ли герой
        return self.health > 0

class Game():
    def __init__(self, player: Hero, computer: Hero):
        # Инициализация игры с игроком и компьютером
        self.player = player
        self.computer = computer

    def get_initiative(self):
        # Определение, кто ходит первым
        self.player_initiative = random.randint(0, 3)
        self.computer_initiative = random.randint(0, 3)

        if self.player_initiative >= self.computer_initiative:
            print(f"Инициативу получил {self.player.name}")
            return self.player
        if self.computer_initiative > self.player_initiative:
            print(f"Инициативу получил {self.computer.name}")
            return self.computer

    def start(self):
        # Основной игровой цикл
        print('Игра началась!')
        initiator = self.get_initiative()
        print('')

        i = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"Ход {i}")
            if initiator == self.player:
                # Ход игрока
                self.player.attack(self.computer)
                print(f'Игрок {self.player.name} атаковал {self.computer.name} с силой {self.player.last_attack}')
                print(f'У {self.computer.name} осталось {self.computer.health} жизней')
                print(f'У {self.player.name} осталось {self.player.health} жизней')
                initiator = self.computer
            else:
                # Ход компьютера
                self.computer.attack(self.player)
                print(f'Игрок {self.computer.name} атаковал {self.player.name} с силой {self.computer.last_attack}')
                print(f'У {self.computer.name} осталось {self.computer.health} жизней')
                print(f'У {self.player.name} осталось {self.player.health} жизней')
                initiator = self.player

            print('')
            i += 1

        # Определение победителя
        if self.player.is_alive():
            print(f'Победил {self.player.name}')
            print(f'Осталось жизней {self.player.health}')
        else:
            print(f'Победил {self.computer.name}')
            print(f'Осталось жизней {self.computer.health}')


# Создание героев и запуск игры
hero = Hero('Бесшумный ливень', 100, 20)
computer = Hero('Капля огня', 100, 20)
print(hero.__str__())
print(computer.__str__())
print()
game = Game(hero, computer)
game.start()
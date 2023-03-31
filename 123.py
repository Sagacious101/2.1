import os


class Humanoid:
    def __init__(
        self,
        name="существо",
        hp=20,
        max_hp=20,
        race="human",
        basic_damage=5,
        money=0,
        equiped_weapon=None,
        inventory=[]
    ):
        self.name = name
        self.hp = hp
        self.race = race
        self.basic_damage = basic_damage
        if equiped_weapon:
            self.damage = (basic_damage + equiped_weapon.damage)
        else:
            self.damage = basic_damage
        self.equiped_weapon = equiped_weapon
        self.money = money
        self.inventory = inventory

    def back_up_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("Инвентарь:")
        if self.inventory:
            for num, i in enumerate(self.inventory):
                if isinstance(i, Item):
                    print(f'{num}.{i.name}')
        else:
            print("Пусто\n")
        print('')

    def show_humanoid(self):
        if self.equiped_weapon:
            self.damage = (self.basic_damage + self.equiped_weapon.damage)
        print('Характеристики:')
        print(f'Имя: {self.name}')
        print(f'Раса: {self.race}')
        print(f'HP: {self.hp}')
        print(f'Монеты: {self.money}')
        if self.equiped_weapon:
            print(f'Урон: {self.damage}({self.basic_damage} + {self.equiped_weapon.damage})')
            print(f'Оружие: {self.equiped_weapon.name}(+{self.equiped_weapon.damage})')
        else:
            print(f'Урон: {self.damage}({self.basic_damage} + 0)')
            print("Оружие: нету")
        print('')

    def equip_weapon(self, weapon_name):
        for i in range(len(self.inventory)):
            if isinstance(self.inventory[i], Weapon):
                if self.inventory[i].name == weapon_name:
                    if self.equiped_weapon:
                        self.inventory.append(self.equiped_weapon)
                    self.equiped_weapon = self.inventory[i]
                    self.inventory.pop(i)


class Item:
    def __init__(self, name=None):
        self.name = name


class Weapon(Item):
    def __init__(self, name=None, damage=0):
        super().__init__()
        self.name = name
        self.damage = damage


def main_menu(player):
    options = [
        "Сражаться",
        "Использовать предмет",
        "Посмотреть характеристики персонажа",
        "Посмотреть инвентарь"
    ]
    show_option(options)
    option = choose_option(options)
    if option == 0:
        pass


def start_fight(hero: Humanoid, enemy: Humanoid) -> None:
    text = "Выберите действие:\n"
    while hero.hp > 0 and enemy.hp > 0:
        os.system("cls")
        hero.show_humanoid()
        enemy.show_humanoid()
        print(text)
        options = [
            "Атаковать противника"
        ]
        show_option(options)
        option = choose_option(options)
        if option == 0:
            combat_turn(hero, enemy)
        combat_turn(enemy, hero)
        input("\nНажмите ENTER чтобы продолжить бой: ")
    combat_result(hero, enemy)


def combat_turn(attacker: Humanoid, defender: Humanoid) -> None:
    if attacker.damage > 0:
        damage = (attacker.damage)
        defender.hp -= damage
        print(f'{attacker.name} атаковал {defender.name} на {damage}!')


def combat_result(hero: Humanoid, enemy: Humanoid) -> None:
    os.system("cls")
    if hero.hp > 0 and enemy.hp <= 0:
        print(f'{hero.name} победил {enemy.name} и в награду получает:')
        hero.money += enemy.money
        print(f'{enemy.money} монет')
        input("Нажмите ENTER чтобы продолжить: ")
    else:
        print("Вы умерли")


def show_option(options: list) -> None:
    for num, option in enumerate(options, 1):
        print(f"{num}. {option[0]}")


def choose_option(hero, options: list) -> int:
    user_option = input("\nВведите номер варианта и нажмите ENTER: ")
    if not user_option.isdigit():
		print("Ошибка! Введены не коректные данные, ввод должен соответсвовать номеру варианта")
		input("Нажмите ENTER чтобы продолжить: ")
		return main_menu(hero)
	idx = int(user_option) - 1
	if not idx < len(options):
		print("Ошибка! Введены не коректные данные, ввод должен соответсвовать номеру варианта")
		input("Нажмите ENTER чтобы продолжить: ")
		return main_menu(hero)


sword_1 = Weapon(name='Ржавый меч', damage=10)
hero = Humanoid(name='Вася', money=15, inventory=[sword_1])
enemy = Humanoid(name='бандит', basic_damage=1)
start_fight(hero, enemy)
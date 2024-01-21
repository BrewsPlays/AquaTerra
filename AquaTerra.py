import art
import random
import time

print(Fore.GREEN + art.text2art("AquaTerra") + Style.RESET_ALL)

class Game:
    def __init__(self, difficulty):
        self.hunger = 100
        self.lives = difficulty
        self.wood = 0
        self.stone = 0
        self.houses = 0
        self.food = 0
        self.tools = 0
        self.boss_hp = 500 if difficulty == 5 else 200
        self.start_time = time.time()
        self.full_game_unlocked = False
        self.farms = 0
        self.trees = 0
        self.difficulty = difficulty

    def print_status(self):
        print(f"{'*' * 50}")
        print(f"🍽️ Hunger: {self.hunger}, ❤️ Lives: {'❤️' * self.lives}")
        print(f"🪵 Wood: {self.wood}, ⛏️ Stone: {self.stone}")
        print(f"🏠 Houses: {self.houses}, 🍖 Food: {self.food}")
        print(f"🛠️ Tools: {self.tools}, 🌾 Farms: {self.farms}, 🌳 Trees: {self.trees}")
        print(f"{'*' * 50}")

    def build_house(self):
        if self.wood >= 10:
            self.houses += 1
            self.wood -= 10
            print("🏠 You built a house!")
        else:
            print("🚫 You don't have enough wood to build a house.")

    def chop_wood(self):
        self.wood += 5
        self.hunger -= self.difficulty
        print("🪓 You chopped some wood.")

    def hunt_boar(self):
        if random.random() < 0.3:
            self.food += 1
            print("🐗 You killed a boar and got some food!")
        else:
            print("🐾 The boar escaped!")

    def eat_food(self):
        if self.food > 0:
            self.hunger += 20
            self.food -= 1
            print("🍽️ You ate some food and you're full!")
        else:
            print("🚫 You don't have any food to eat.")

    def mine_stone(self):
        self.stone += 5
        self.hunger -= self.difficulty
        print("⛏️ You mined some stone.")

    def crafting(self):
        if self.wood >= 2 and self.stone >= 2:
            self.tools += 1
            self.wood -= 2
            self.stone -= 2
            print("🛠️ You crafted a tool!")
        else:
            print("🚫 You don't have enough materials to craft a tool.")

    def fight_boss(self):
        if random.random() < 0.5:
            self.boss_hp -= 100
            print(f"👊 You hit Verzide and he has {self.boss_hp} HP left!")
            if self.boss_hp <= 0:
                self.full_game_unlocked = True
                print("🎉 Congratulations! You defeated Verzide and unlocked the full game!")
        else:
            print("💥 Verzide hit you and you lost a life!")
            self.lives -= 1

    def build_farm(self):
        if self.wood >= 10 and self.stone >= 5:
            self.farms += 1
            self.wood -= 10
            self.stone -= 5
            print("🌾 You built a farm!")
        else:
            print("🚫 You don't have enough materials to build a farm.")

    def plant_tree(self):
        if self.wood >= 1:
            self.trees += 1
            self.wood -= 1
            print("🌳 You planted a tree!")
        else:
            print("🚫 You don't have enough wood to plant a tree.")

    def harvest(self):
        if self.farms > 0:
            self.food += self.farms * 5
            print(f"🌽 You harvested your farms and got {self.farms * 5} food!")
        else:
            print("🚫 You don't have any farms to harvest.")

    def game_loop(self):
        while self.hunger > 0 and self.lives > 0:
            self.print_status()

            if time.time() - self.start_time >= 60 and (self.houses > 0 and self.tools > 0):
                print("💀 Verzide appeared!")
                action = input("Action (f - fight / e - end): ").lower()
                if action == 'f':
                    self.fight_boss()
                elif action == 'e':
                    break
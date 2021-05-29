import random, os, time

class Characters:
    def __init__(self, name, health, power, coins, evadePw, armorPw):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        self.evadePw = evadePw
        self.armorPw = armorPw

    def alive(self):
        if self.health > 0:
            return True
        else: 
            return False

    def print_status(self):
        print("{} has {} health {} power and {} Coins".format(self.name, self.health, self.power, self.coins))

    def alive_status(self):
        if self.health > 0:
            return True
        else:
            print(f"{self.name} is dead.")
            return False

class Hero(Characters):    

    def attack(self, enemy):
        chance = random.randint(1, 10)
        if chance <= 2:
            enemy.health -= 2 * self.power
            print(f"You attacked {enemy.name} with your Double Damage of Doom dance attack! \n{2*self.power} damage done to {enemy.name}!")
        else:
            enemy.health -= self.power
            print(f"You did {self.power} damage to the {enemy.name} with your Wildebeest Wiggle attack!")
    
    def bounty(self, enemy):
        if enemy.health <= 0:
            self.coins += enemy.coins
            print(f"You just stole {enemy.coins} coins from the {enemy.name}s corpse\nYou now have {self.coins} coins.")
        
    def armor(self, enemy):
        if self.armorPw > 1:
            if self.armorPw == 2:
                print(f"{self.name}s armor blocked 1 damage point from {enemy.name}s attack")
                self.health += 1
            elif self.armorPw == 4:
                print(f"{self.name}s armor blocked 2 damage points from {enemy.name}s attack")
                self.health += 2
            elif self.armorPw >= 6:
                print(f"{self.name}s armor blocked 3 damage points from {enemy.name}s attack")
                self.health += 3
        else:
            pass

    def evade(self, enemy):
        chance = random.randint(1, 100)
        blocked = f"{self.name} evaded {enemy.name}s attack"
        hit = f"{self.name} could not evade {enemy.name}s attack"
        enemyCatch = random.randint(1, 4)
        def catchPhrase():
            if enemyCatch == 1:
                print(f"{enemy.name}: 'You won't last long {self.name}'")
            if enemyCatch == 2:
                print(f"{enemy.name}: 'Good luck trying to kill me {self.name}'")
            if enemyCatch == 3:
               print(f"{enemy.name}: 'Catch me if you can {self.name}...'")
            if enemyCatch == 4: 
                print(f"{enemy.name}: 'Looks like I'm having '{self.name}' soup tonight!'")
        pickTool = random.randint(1, 3)
        def kickAss():
            if pickTool == 1:
                print(f"{enemy.name} catapulted {self.name} into a tree! {enemy.power} damage done to you")
            if pickTool == 2:
                print(f"{self.name} sank into {enemy.name}s quick sand! {enemy.power} damage done to you")
            if pickTool == 3:
                print(f"{enemy.name} smushed {self.name} with an anvil! {enemy.power} damage done to you")
        if self.evadePw == 0:
            self.health -= enemy.power
            kickAss()
            catchPhrase()
        elif self.evadePw == 2:
            if chance <= 10:
                print(blocked)
            else:
                print(hit)
                self.health -= enemy.power
                kickAss()
                catchPhrase()
        elif self.evadePw == 4:
            if chance <= 20:
                print(blocked)
            else:
                print(hit)
                self.health -= enemy.power 
                kickAss()
                catchPhrase()
        elif self.evadePw == 6:
            if chance <= 30:
                print(blocked)
            else:
                (hit)
                self.health -= enemy.power
                kickAss()
                catchPhrase()
          
class Goblin(Characters):

    def attack(self, enemy):
        enemy.health -= self.power
        print(f"The {self.name} sprayed you with sewer gunk! {self.power} damage was done to you.")

class Medic(Characters):
   
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"The {self.name} choked you with a medieval stethoscope causing {self.power} damage done to you!")

    def recoup(self):
        chance = random.randint(1, 10)
        if chance <= 2:
            print(f"{self.name} healed itself and gained 2 health")
            print(f"{self.name}: 'Good luck trying to kill me {h_name}'")
            self.health += 2

class Shadow(Characters):
    
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"The {self.name} attacked you with shadow puppets! Did {self.power} damage to you.")

    def evade(self, enemy):
        sideStep = random.randint(1, 100)
        if sideStep >= 11:
            print(f"{self.name} shifted out of the way and escaped your attack.")
            print(f"{self.name}: 'Catch me if you can {h_name}...'")
        else:
            self.health -= enemy.power
            print(f"{enemy.name} caught {self.name} with a holeless butterfly net causing {enemy.power} damage!")

class Zombie(Characters):
    
    def attack(self, enemy):
            enemy.health -= self.power
            print(f"The {self.name} set Zombie Scooby Doo on you! {self.power} damage done to you.")
        
    def zombieAliveCheat(self):
        if self.health > -25:
            return True
        else:
            return False

def storyIntro():
    print(f"[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]\n")
    print(f"Hello {h_name}! You've landed in Heatogon! You can either")
    print(f"leave while you can or fight enemies to become Head Heat!")
    print(f"Each enemy holds coins you can use to make purchases in")
    print(f"the Super Store. There you cann find potions or even call")
    print(f"a friend for help! Which enemy will it take to beat the game?")
    print(f"Only time will tell... \n")
    print(f"[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]=[]\n ")
    input("Press Enter to contine...")

def main():
    hero = Hero(h_name, 20, 4, 5, 0, 0)
    goblin = Goblin("Gooey Goblin", 6, 3, 10, 0, 0)
    medic = Medic("Magic Medic", 10, 3, 15, 0, 0)
    shadow = Shadow("Shifty Shadow", 1, 3, 20, 0, 0)
    zombie = Zombie("Never Dead Zombie", 5, 3, 50, 0, 0)

    while hero.alive():
        print()
        print("============================================")
        if zombie.zombieAliveCheat() == False:
            print(f"\nThe {zombie.name} finally is dead!")
            print(f"Congratulations {h_name} you have beat the game!")
            print(f"You are officially the new Head Heat!")
            print(f"If it weren't for you meddling kids, I'd still be alive {h_name}!")
            break
        hero.print_status()
        print(f"What do you want to do?\n ")
        if goblin.alive():
            time.sleep(.25)
            goblin.print_status()
            print("1. Fight Goblin\n ")
        time.sleep(.25)
        print("Buy supplies but all charaters attack you\n2. Pass turn to enter store\n ")
        if medic.alive():
            time.sleep(.25)
            medic.print_status()
            print("3. Fight Medic\n ")
        if shadow.alive():
            time.sleep(.25)
            shadow.print_status()
            print("4. Fight Shadow\n ")
        if zombie.zombieAliveCheat():
            time.sleep(.25)
            zombie.print_status()
            print("5. Fight Zombie\n ")
        time.sleep(.25)
        print("Trade 5 health for 1 power. No enemies attack you")
        print("6. Visit Wizard for trade\n")
        time.sleep(.25)
        print("Run for dear life!\n7. Flee")
        print("============================================")
        print("> ", end=' ')
        raw_input = input("Enter your number choice: ")
        time.sleep(.25)
        if raw_input == "1":
            if goblin.alive_status():
                hero.attack(goblin)
                if goblin.alive_status():
                    hero.evade(goblin) 
                    hero.armor(goblin)
                else:
                    hero.bounty(goblin)
            else:
                pass
        elif raw_input == "2":
            if hero.coins > 4:
                while hero.coins >= 5:
                    print(f"\nWelcome to the Super Store. You have {hero.coins} coins.")
                    print("1. Buy SuperTonic: Fully restores health // Cost: 10 coins")
                    print("2. Buy ArmyArmor: Blocks 1 attack point for every 2 points // Cost: 5 coins")
                    print("3. EnemyEvade: Evasion increased by 10 percent // Cost: 5 coins")
                    print("4. Phone Call: A friend will send you a mystery number of health points // Cost: 5 coins")
                    print("5. Exit Super Store\n ")
                    store_option = input("What would you like to do: ")
                    if store_option == "1":
                        if hero.health <= 19:
                            if hero.coins >= 10:
                                print("You just bought SuperTonic!")
                                hero.health += (20 - hero.health)
                                print(f"Your health is now {hero.health}") 
                                hero.coins -= 10
                            else:
                                print("You don't have enough coins\n ")
                        else:
                            print("Your health is already full\n")
                    elif store_option == "2":
                        if hero.armorPw <= 5:
                            if hero.coins >=5:
                                print(f"You just bought ArmyArmor!")
                                hero.armorPw += 2
                                print(f"You now have {hero.armorPw} armor points")
                                hero.coins -= 5 
                            else:
                                print("You don't have enough coins\n ")
                        else:
                            print("You already have max armor points\n")
                    elif store_option == "3":
                        if hero.evadePw <= 7:
                            if hero.coins >=5:
                                print(f"You just bought EnemyEvade!")
                                hero.evadePw += 2
                                print(f"Evasion now increased to {hero.evadePw * 10} percent")
                                hero.coins -= 5 
                            else:
                                print("You don't have enough coins\n ")
                        else:
                            print("You already have max evade points\n")
                    elif store_option == "4":
                        if hero.coins >= 5:
                            help = random.randint(1, 3)
                            hero.health += help
                            if hero.health > 20:
                                balance = hero.health - 20
                                hero.health -= balance
                            print("~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~\n ")
                            print(f"{hero.name} just made a phone call!\nYour friend sent you {help} health!")
                            print(f"You now have {hero.health} health points\n")
                            print("~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~\n ")
                            hero.coins -= 5
                            time.sleep(2.5)
                        else:
                            print("You don't have enough coins.\n ")
                    elif store_option == "5":
                        print(f"Now exiting Super Store with {hero.coins} coins\n ")
                        print("============================================")
                        time.sleep(2)      
                        break
                    else:
                        print(f"Invalid input {store_option}")
                else: 
                    print(f"Not enough coins to make more purchases.\nNow exiting Super Store with {hero.coins} coins\n ")
                    print("============================================")
                    time.sleep(3)
                    os.system("clear")
            else:
                print("You do not have enough coins to enter the store.")
                time.sleep(2.5)
                os.system("clear")
            if goblin.alive_status():             
                goblin.attack(hero)
                hero.armor(goblin)
            if medic.alive_status():
                medic.attack(hero)
                hero.armor(medic)
            if shadow.alive_status():
                shadow.attack(hero)
                hero.armor(shadow)
            if zombie.zombieAliveCheat():
                zombie.attack(hero)
                hero.armor(zombie)
                hero.alive_status()
        elif raw_input == "3":
            if medic.alive_status():
                hero.attack(medic)             
                medic.recoup
                if medic.alive_status():
                    hero.evade(medic)
                    hero.armor(medic)
                    hero.alive_status()
                else:
                    hero.bounty(medic)
            else:
                pass
        elif raw_input == "4":
            if shadow.alive_status():
                shadow.evade(hero)
                if shadow.alive_status():
                    hero.evade(shadow)
                    hero.armor(shadow)
                    hero.alive_status()
                else:
                    hero.bounty(shadow)
            else:
                pass
        elif raw_input == "5":
            hero.attack(zombie)
            if zombie.zombieAliveCheat():
                hero.evade(zombie)
                hero.armor(zombie)
                hero.alive_status()
        elif raw_input == "6":
            if hero.health >= 6:
                hero.health -= 5
                hero.power += 1
                print("o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o\n ")
                print(f"You just traded health for power.\nWilly the Wacky Wizard: 'Pleasure doing buisness with you {h_name}'")
                print(f"You now have {hero.health} health and {hero.power} power.\n ")
                print(f"o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o")
                time.sleep(4)
                os.system("clear")
            else:
                print(f"o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o\n ")
                print(f"You do not have enough health to trade")
                print(f"Willy the Wacky Wizard: 'Tough luck kid. Now skat!'")
                print(f"o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o\n ")
                time.sleep(4)
                os.system("clear")
        elif raw_input == "7":
            print(f"Wise choice. {h_name} ran away for dear life.")
            break
        else:
            print("Invalid input {}".format(raw_input))

h_name = input("Enter your hero name: ")
time.sleep(.25)
os.system("clear")
storyIntro()
time.sleep(.25)
os.system("clear")
main()

            
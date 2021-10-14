
from fleet import Fleet
from herd import Herd
import random

class Battlefield():
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()
        self.turn = 1
        self.user_select = 0
        self.opponent_select = 0
        self.select_target = 0
        self.user_team = None
        self.opponent_team = None
        self.user_attacker = None
        self.user_attacked = None
        self.opponent_attacker = None
        self.opponent_attacked = None

      
    def run_game(self):
        self.display_welcome()
        self.fleet.create_fleet()
        self.herd.create_herd()
        
        self.user_choice = input("pick a team, enter 1 for Dinosaurs or 2 for Robots")
        while (self.user_choice != "1") & (self.user_choice != "2"):
            self.user_choice = input("Enter a 1 or a 2!")
        if(self.user_choice == "1"):
            self.user_team = self.herd.dinosaurs
            self.opponent_team = self.fleet.robots
            print("Your team of Dinosaurs is:")
            for dinosaurs in self.user_team:
                print(f"Name - {dinosaurs.name} \nAttack Power - {dinosaurs.attack_points}, \nHealth - {dinosaurs.health_points}")
            print("You will be battling robots to take your rightful throne as the Alphas on Earth! \nYour opponents are as follows:")
            for robots in self.opponent_team:
                print(f"Name - {robots.name} \nAttack Power - {robots.attack_points}, \nHealth - {robots.health_points}")
        else:
            self.user_team = self.fleet.robots
            self.opponent_team = self.herd.dinosaurs
            print("Your team of robots is:")
            for robots in self.user_team:
                print(f"Name - {robots.name} \nAttack Power - {robots.attack_points}, \nHealth - {robots.health_points}")
            print("You will be battling for hummanity as we know it!!! \nYour opponents are as follows:")
            for dinosaurs in self.opponent_team:
                print(f"Name - {dinosaurs.name} \nAttack Power - {dinosaurs.attack_points}, \nHealth - {dinosaurs.health_points}")
        self.battle()
    
    def display_welcome(self):
        print("Welcome to a battle for the free world!")

    def battle(self):
        if self.turn % 2 == 1:
            if self.user_team == self.herd.dinosaurs:
                self.opponent_team == self.fleet.robots
                self.dino_turn()
                if self.opponent_team[self.opponent_select].health_points < 1:
                    print(f"{self.opponent_team[self.opponent_select].name} got clapped!")
                    del self.opponent_team[self.opponent_select]
            else:
                self.robo_turn()
                if self.opponent_team[self.opponent_select].health_points < 1:
                    print(f"{self.opponent_team[self.opponent_select].name} just got clapped!")
                    del self.opponent_team[self.opponent_select]
        else:
            if self.user_team == self.herd.dinosaurs:
                self.robo_turn()
                if self.user_team[self.user_select].health_points < 1:
                    print(f"{self.user_team[self.user_select].name} just got clapped!")
                    del self.user_team[self.user_select]
            else:
                self.dino_turn()
                if self.user_team[self.user_select].health_points < 1:
                    print(f"{self.user_team[self.user_select].name} got clapped!")
                    del self.user_team[self.user_select]
        if len(self.user_team) > 0:
            if len(self.opponent_team) > 0:
                self.opponent_select = 0
                self.turn += 1
                self.battle()
            else:
                print("You have won! The future is yours! The dominate team is:")
                self.display_winners()

        else:
            print("You lost..... The non losers are:")
            self.display_winners()

           

    def dino_turn(self):
        if self.user_team == self.herd.dinosaurs:
            self.user_team[self.user_select]
            print(f"You'e pulling up with {self.user_team[self.user_select].name}")
            print(f"\n Pick a fool to ride on!")
            self.show_robo_opponent_options()
            self.opponent_select = int(input("Enter opponent number to ride on!"))
            while (self.opponent_select < 0) or (self.opponent_select > len(self.opponent_team) - 1):
                self.opponent_select = int(input("Error! Select an opponent"))
            print(f"{self.user_team[self.user_select].name} pulls up on {self.opponent_team[self.opponent_select].name} and did {self.user_team[self.user_select].attack_points} damage!")
            self.user_team[self.user_select].dinosaur_attack(self.opponent_team[self.opponent_select])
            if self.user_select >= (len(self.user_team) - 1):
                self.user_select = 0
            else:
                self.user_select += 1
        else:
            self.select_target = random.randint(0, len(self.user_team) - 1)
            print(f"{self.opponent_team[self.opponent_select].name} pulled up on {self.user_team[self.user_select].name} and did {self.opponent_team[self.opponent_select].attack_points} damage!")
            self.opponent_team[self.opponent_select].dinosaur_attack(self.user_team[self.user_select])
            if self.user_select >= (len(self.user_team) - 1):
                self.user_select = 0


    def robo_turn(self):
        if self.user_team == self.fleet.robots:
            self.user_team[self.user_select]
            print(f"You'e pulling up with {self.user_team[self.user_select].name}")
            print(f"\n Pick a fool to ride on!")
            self.show_dino_opponent_options()
            self.opponent_select = int(input("Enter opponent number to ride on!"))
            while (self.opponent_select < 0) or (self.opponent_select > len(self.opponent_team) - 1):
                self.opponent_select = int(input("Error! Select an opponent"))
            print(f"{self.user_team[self.user_select].name} pulls up on {self.opponent_team[self.opponent_select].name} and did {self.user_team[self.user_select].attack_points} damage!")
            self.user_team[self.user_select].robot_attack(self.opponent_team[self.opponent_select])
            if self.user_select >= (len(self.user_team) - 1):
                self.user_select = 0
            else:
                self.user_select += 1
        else:
            self.select_target = random.randint(0, len(self.user_team) - 1)
            print(f"{self.opponent_team[self.opponent_select].name} pulled up on {self.user_team[self.user_select].name} and did {self.opponent_team[self.opponent_select].attack_points} damage!")
            self.opponent_team[self.opponent_select].robot_attack(self.user_team[self.user_select])
            if self.user_select >= (len(self.user_team) - 1):
                self.user_select = 0

    def show_dino_opponent_options(self):
        for dinosaurs in self.opponent_team:
            print(f"Enter {self.opponent_select} - {dinosaurs.name}")
            self.opponent_select += 1

    def show_robo_opponent_options(self):
        for robots in self.opponent_team:
            print(f"Enter {self.opponent_select} - {robots.name}")
            self.opponent_select += 1

    def display_winners(self):
        if self.user_choice == "1": #1 for dinos 2 for robos\
            if len(self.user_team) == 0:
                for robots in self.fleet.robots:
                    print(f"{robots.name}")
            else:
                for dinosaurs in self.herd.dinosaurs:
                    print(f"{dinosaurs.name}")
        else:
            if len(self.user_team) == 0:
                for dinosaurs in self.herd.dinosaurs:
                    print(f"{dinosaurs.name}")
            else:
                for robots in self.fleet.robots:
                    print(f" {robots.name}")
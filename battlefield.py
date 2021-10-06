from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
import random

from robot import Robot

class Battlefield():
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()
        self.turn = 1
        self.user_turn = 0
        self.opponent_turn = 0
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
                print(f"Name - {dinosaurs.name[0]} \nAttack Power - {dinosaurs.attack_points[0]}, \nHealth - {dinosaurs.health_points[0]}, \nName - {dinosaurs.name[1]} \nAttack Power - {dinosaurs.attack_points[1]}, \nHealth - {dinosaurs.health_points[1]}, \nName - {dinosaurs.name[2]} \nAttack Power - {dinosaurs.attack_points[2]}, \nHealth - {dinosaurs.health_points[2]}, \nName - {dinosaurs.name[3]} \nAttack Power - {dinosaurs.attack_points[3]} \nHealth - {dinosaurs.health_points[3]}")
            print("You will be battling robots to take your rightful throne as the Alphas on Earth! \nYour opponents are as follows:")
            for robots in self.opponent_team:
                print(f"Name - {robots.name[0]} \nAttack Power - {robots.attack_points[0]}, \nHealth - {robots.health_points[0]}, \nName - {robots.name[1]} \nAttack Power - {robots.attack_points[1]}, \nHealth - {robots.health_points[1]}, \nName - {robots.name[2]} \nAttack Power - {robots.attack_points[2]}, \nHealth - {robots.health_points[2]}, \nName - {robots.name[3]} \nAttack Power - {robots.attack_points[3]} \nHealth - {robots.health_points[3]}")
        else:
            self.user_team = self.fleet.robots
            self.opponent_team = self.herd.dinosaurs
            print("Your team of robots is:")
            for robots in self.user_team:
                print(f"Name - {robots.name[0]} \nAttack Power - {robots.attack_points[0]}, \nHealth - {robots.health_points[0]}, \nName - {robots.name[1]} \nAttack Power - {robots.attack_points[1]}, \nHealth - {robots.health_points[1]}, \nName - {robots.name[2]} \nAttack Power - {robots.attack_points[2]}, \nHealth - {robots.health_points[2]}, \nName - {robots.name[3]} \nAttack Power - {robots.attack_points[3]} \nHealth - {robots.health_points[3]}")
            print("You will be battling for hummanity as we know it!!! \nYour opponents are as follows:")
            for dinosaurs in self.opponent_team:
                print(f"Name - {dinosaurs.name[0]} \nAttack Power - {dinosaurs.attack_points[0]}, \nHealth - {dinosaurs.health_points[0]}, \nName - {dinosaurs.name[1]} \nAttack Power - {dinosaurs.attack_points[1]}, \nHealth - {dinosaurs.health_points[1]}, \nName - {dinosaurs.name[2]} \nAttack Power - {dinosaurs.attack_points[2]}, \nHealth - {dinosaurs.health_points[2]}, \nName - {dinosaurs.name[3]} \nAttack Power - {dinosaurs.attack_points[3]} \nHealth - {dinosaurs.health_points[3]}")
        self.battle()
    
    def display_welcome():
        print("Welcome to a battle for the free world!")

    def battle(self):
        if self.turn % 2 == 1:
            if self.user_team == self.herd.dinosaurs:
                self.dino_turn()
                if self.opponent_attacked.health_points < 1:

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    # def show_dino_opponent_options(self):
    #     pass

    # def show_robo_opponent_options(self):
    #     pass

    def display_winners(self):
        pass

from robot import Robot
from weapon import Weapon
class Fleet():
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot_one = Robot("Gipsy Danger", 10000, 5500, Weapon("Chain Sword", 5500))
        robot_two = Robot("Crimson Typhoon", 7500, 2000, Weapon("Three Armed Barrage", 2000))
        robot_three = Robot("Striker Eureka", 8000, 2500, Weapon("Chest Missle Barrage", 2500))
        robot_four = Robot("Cherno Alpha", 8500, 1500, Weapon("Z-14 Tesla Fists", 1500))
        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)
        self.robots.append(robot_four)
from robot import Robot
from weapon import Weapon
class Fleet():
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        self.robots = [Robot("Gipsy Danger", 30000, 5500, Weapon("Chain Sword", 5500)), Robot("Crimson Typhoon", 15000, 2000, Weapon("Three Armed Barrage", 2000)), Robot("Striker Eureka", 20000, 2500, Weapon("Chest Missle Barrage", 2500)), Robot("Cherno Alpha", 22000, 1500, Weapon("Z-14 Tesla Fists", 1500))]
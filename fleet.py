from robot import Robot
from weapon import Weapon
class Fleet():
    def __init__(self):
        self.robots = [Robot("Gipsy Danger", 30000, Weapon("Chain Sword", 5500)), Robot("Crimson Typhoon", 15000, Weapon("Three Armed Barrage", 2000)), Robot("Striker Eureka", 20000, Weapon("Chest Missle Barrage", 2500)), Robot("Cherno Alpha", 22000, Weapon("Z-14 Tesla Fists", 1500))]

    def create_fleet(self):
        pass
from dinosaur import Dinosaur
from weapon import Weapon
class Herd():
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        dinosaur_one = Dinosaur("Slattern", 10000, 5000, Weapon("Triple-Crowned Tail Whip", 5000))
        dinosaur_two = Dinosaur("Raiju", 8000, 1000, Weapon("Armored Headbutt", 1000))
        dinosaur_three = Dinosaur("Otachi", 7500, 2000, Weapon("Acid Spray", 2000))
        dinosaur_four = Dinosaur("Scunner", 8500, 1500, Weapon("Armor pplated four arm claws", 1500))
        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)
        self.dinosaurs.append(dinosaur_four)
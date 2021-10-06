from dinosaur import Dinosaur
from weapon import Weapon
class Herd():
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.dinosaurs = [Dinosaur("Slattern", 30000, 5000, Weapon("Triple-Crowned Tail Whip", 5000)), Dinosaur("Raiju", 20000, 1000, Weapon("Armored Headbutt", 1000)), Dinosaur("Otachi", 15000, 2000, Weapon("Acid Spray", 2000)), Dinosaur("Scunner", 20000, 1500, Weapon("Armor pplated four arm claws", 1500))]
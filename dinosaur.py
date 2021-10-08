from robot import Robot


class Dinosaur():
    def __init__(self, name, health_points, attack_points, weapon):
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points
        self.weapon = weapon

    def dinosaur_attack(self, robots):
        robots.health_points -= self.attack_points
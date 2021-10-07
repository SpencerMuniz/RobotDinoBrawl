class Dinosaur():
    def __init__(self, name, health_points, attack_points, weapon):
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points
        self.weapon = weapon

    def dinosaur_attack(self, robot):
        robot.health_points -= self.attack_points
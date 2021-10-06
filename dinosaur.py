class Dinosaur():
    def __init__(self, name, health_points, attack_points, attack_type):
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points
        self.attack_type = attack_type

    def dinosaur_attack(self, robot):
        robot.robot_attack_points -= self.dinosaur_attack
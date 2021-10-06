class Robot:
    def __init__(self, name, health_points, attack_points):
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points

    def robot_attack(self, dinosaur):
        dinosaur.health_points -= self.attack_points

    
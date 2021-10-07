class Robot:
    def __init__(self, name, health_points, attack_points, weapon):
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points
        self.weapon = weapon

    def robot_attack(self, dinosaur):
        dinosaur.health_points -= self.attack_points

    
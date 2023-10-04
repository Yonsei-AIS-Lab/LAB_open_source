class Star:
    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def __str__(self):
        return f"{self.name} (Mass: {self.mass}, Position: {self.position}, Velocity: {self.velocity})"
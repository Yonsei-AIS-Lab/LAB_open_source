import math

class Constellations:
    def __init__(self):
        self.stars = []

    def add_star(self, star):
        self.stars.append(star)

    def calculate_gravitational_force(self, star1, star2):
        G = 6.67430e-11  # 중력 상수 (m^3 kg^-1 s^-2)
        if star1.position == star2.position:
            return 0
        distance = math.sqrt(sum((x1 - x2)**2 for x1, x2 in zip(star1.position, star2.position)))
        force = (G * star1.mass * star2.mass) / (distance**2)
        return force

    def update_positions(self, time_step):
        for star in self.stars:
            total_force = [0, 0, 0]
            for other_star in self.stars:
                if star != other_star:
                    force = self.calculate_gravitational_force(star, other_star)
                    direction = [(x1 - x2) / math.sqrt(sum((x1 - x2)**2 for x1, x2 in zip(star.position, other_star.position))) for x1, x2 in zip(star.position, other_star.position)]
                    force_vector = [force * d for d in direction]
                    total_force = [f1 + f2 for f1, f2 in zip(total_force, force_vector)]
            acceleration = [f / star.mass for f in total_force]
            star.velocity = [v + a * time_step for v, a in zip(star.velocity, acceleration)]
            star.position = [p + v * time_step for p, v in zip(star.position, star.velocity)]

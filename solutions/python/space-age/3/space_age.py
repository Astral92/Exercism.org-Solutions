"""Calculate age on a planet in the our Solar System"""

class SpaceAge:
    ORBITAL_PERIODS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds):
        self.earth_seconds_unrounded = seconds / 31557600

    def age_on(self, planet):
        return round(self.earth_seconds_unrounded / self.ORBITAL_PERIODS[planet], 2)

    def on_earth(self):
        return self.age_on("earth")

    def on_mercury(self):
        return self.age_on("mercury")

    def on_venus(self):
        return self.age_on("venus")

    def on_mars(self):
        return self.age_on("mars")

    def on_jupiter(self):
        return self.age_on("jupiter")

    def on_saturn(self):
        return self.age_on("saturn")

    def on_uranus(self):
        return self.age_on("uranus")

    def on_neptune(self):
        return self.age_on("neptune")
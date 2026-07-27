"""Calculate age on a planet in the the Solar System"""


class SpaceAge:
    """Convert a duration in seconds to equivalent years on different Solar System planets."""

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

    EARTH_YEARS_SECONDS = 31557600

    def __init__(self, seconds):
        self.earth_years = seconds / self.EARTH_YEARS_SECONDS

    def age_on(self, planet):
        return round(self.earth_years / self.ORBITAL_PERIODS[planet], 2)

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
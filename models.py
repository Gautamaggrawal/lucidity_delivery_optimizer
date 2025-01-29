from dataclasses import dataclass

@dataclass(frozen=True)
class Location:
    name: str
    latitude: float
    longitude: float

    def __hash__(self):
        return hash((self.name, self.latitude, self.longitude))

@dataclass(frozen=True)
class Restaurant(Location):
    prep_time_minutes: float

    def __hash__(self):
        return hash((self.name, self.latitude, self.longitude, self.prep_time_minutes))

@dataclass(frozen=True)
class Consumer(Location):
    restaurant: Restaurant

    def __hash__(self):
        return hash((self.name, self.latitude, self.longitude, self.restaurant))
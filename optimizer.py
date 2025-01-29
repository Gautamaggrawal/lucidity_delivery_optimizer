from math import radians, sin, cos, sqrt, atan2
import itertools
from typing import List, Tuple
from models import Consumer, Location, Restaurant
from config import DEFAULT_SPEED_KMH, EARTH_RADIUS_KM

class DeliveryOptimizer:
    def __init__(self, delivery_agent: Location, restaurants: List[Restaurant], 
                 consumers: List[Consumer], speed_kmh: float = DEFAULT_SPEED_KMH):
        self.delivery_agent = delivery_agent
        self.restaurants = restaurants
        self.consumers = consumers
        self.speed_kmh = speed_kmh

    def calculate_distance(self, loc1: Location, loc2: Location) -> float:
        """Calculate distance between two points using Haversine formula."""
        lat1, lon1 = radians(loc1.latitude), radians(loc1.longitude)
        lat2, lon2 = radians(loc2.latitude), radians(loc2.longitude)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = EARTH_RADIUS_KM * c

        return distance

    def calculate_travel_time(self, distance: float) -> float:
        """Calculate travel time in minutes given distance in kilometers."""
        return (distance / self.speed_kmh) * 60

    def evaluate_route(self, route: List[Location]) -> Tuple[float, List[str]]:
        """Evaluate total time for a given route and return the total time and event log."""
        current_time = 0.0
        current_location = self.delivery_agent
        event_log = []
        pickup_times = {r: 0.0 for r in self.restaurants}
        delivered_orders = set()

        for next_location in route:
            distance = self.calculate_distance(current_location, next_location)
            travel_time = self.calculate_travel_time(distance)
            current_time += travel_time

            if isinstance(next_location, Restaurant):
                prep_time_needed = next_location.prep_time_minutes
                time_since_start = current_time
                wait_time = max(0, prep_time_needed - time_since_start)
                current_time += wait_time
                pickup_times[next_location] = current_time
                event_log.append(
                    f"Arrived at {next_location.name} at {current_time:.1f} min, "
                    f"waited {wait_time:.1f} min"
                )

            elif isinstance(next_location, Consumer):
                if pickup_times[next_location.restaurant] == 0:
                    return float('inf'), []
                
                delivered_orders.add(next_location)
                event_log.append(
                    f"Delivered to {next_location.name} at {current_time:.1f} min"
                )

            current_location = next_location

        if len(delivered_orders) != len(self.consumers):
            return float('inf'), []

        return current_time, event_log

    def find_optimal_route(self) -> Tuple[List[Location], float, List[str]]:
        """Find the optimal delivery route by evaluating all possible permutations."""
        all_locations = self.restaurants + self.consumers
        best_time = float('inf')
        best_route = None
        best_log = None

        for route in itertools.permutations(all_locations):
            total_time, event_log = self.evaluate_route(route)
            if total_time < best_time:
                best_time = total_time
                best_route = route
                best_log = event_log

        return best_route, best_time, best_log
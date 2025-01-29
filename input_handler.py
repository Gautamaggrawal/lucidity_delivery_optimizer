from typing import List, Tuple
from geocoding import get_coordinates
from models import Location, Restaurant, Consumer

def get_input() -> Tuple[Location, List[Restaurant], List[Consumer]]:
    """Get user input for delivery scenario."""
    print("\n=== Delivery Route Optimizer ===")
    
    # Get delivery agent location
    agent_location = input("\nEnter delivery executive's location (e.g., Koramangala 1st Block): ")
    agent_lat, agent_lng = get_coordinates(agent_location)
    delivery_agent = Location("Delivery Agent", agent_lat, agent_lng)

    # Get number of orders
    while True:
        try:
            num_orders = int(input("\nEnter number of orders to deliver (1-5): "))
            if 1 <= num_orders <= 5:
                break
            print("Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number!")

    restaurants = []
    consumers = []

    # Get restaurant and consumer details for each order
    for i in range(num_orders):
        print(f"\n=== Order {i+1} Details ===")
        
        # Restaurant details
        rest_name = input(f"Enter restaurant {i+1} location: ")
        rest_lat, rest_lng = get_coordinates(rest_name)
        
        while True:
            try:
                prep_time = float(input(f"Enter preparation time (minutes) for restaurant {i+1}: "))
                if prep_time > 0:
                    break
                print("Preparation time must be positive!")
            except ValueError:
                print("Please enter a valid number!")

        restaurant = Restaurant(f"R{i+1}", rest_lat, rest_lng, prep_time)
        restaurants.append(restaurant)

        # Consumer details
        cons_name = input(f"Enter consumer {i+1} location: ")
        cons_lat, cons_lng = get_coordinates(cons_name)
        consumer = Consumer(f"C{i+1}", cons_lat, cons_lng, restaurant)
        consumers.append(consumer)

    return delivery_agent, restaurants, consumers
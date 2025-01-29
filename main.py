from optimizer import DeliveryOptimizer
from input_handler import get_input
def main():
    try:
        print("Welcome to the Delivery Route Optimizer!")
        delivery_agent, restaurants, consumers = get_input()

        optimizer = DeliveryOptimizer(
            delivery_agent=delivery_agent,
            restaurants=restaurants,
            consumers=consumers
        )

        best_route, total_time, event_log = optimizer.find_optimal_route()
        
        print("\n=== Results ===")
        print(f"\nOptimal Route:")
        print(" -> ".join(location.name for location in best_route))
        print(f"\nTotal Estimated Time: {total_time:.1f} minutes")
        print("\nDetailed Timeline:")
        for event in event_log:
            print(event)

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again with valid inputs.")

if __name__ == "__main__":
    main()
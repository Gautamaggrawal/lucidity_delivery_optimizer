# Delivery Optimizer

## Overview
The **Delivery Optimizer** is a Python-based application designed to optimize delivery routes for a delivery agent. It uses the Haversine formula to calculate the distance between various locations (such as restaurants and consumers), calculates the required travel time, and evaluates different delivery routes to minimize the total time for completing all deliveries.

The core functionality includes calculating travel times, wait times at restaurants, and ensuring timely delivery to all consumers. The optimal route is determined through permutation-based evaluation of all possible routes.

## Features
- **Distance Calculation**: Computes distances between locations using the Haversine formula.
- **Travel Time Calculation**: Calculates the travel time in minutes based on a fixed speed.
- **Route Evaluation**: Evaluates the total time for a given route, including waiting times at restaurants and delivery times to consumers.
- **Optimal Route Calculation**: Finds the best route by evaluating all possible permutations of the route and selecting the one that minimizes total travel time.

## Modules Overview
### 1. `config.py`
Contains constants and configuration values:
- `DEFAULT_SPEED_KMH`: The default speed (in km/h) of the delivery agent.
- `EARTH_RADIUS_KM`: The radius of the Earth used for distance calculation in kilometers.

### 2. `models.py`
Defines the data models used throughout the application:
- **Location**: A base class representing a geographic location.
- **Restaurant**: Inherits from `Location` and adds attributes like `prep_time_minutes`, which specifies the preparation time at the restaurant.
- **Consumer**: Inherits from `Location` and represents a consumer with a reference to the restaurant where the order was prepared.

### 3. `geocoding.py`
Contains helper functions for handling and manipulating location coordinates, such as converting latitude and longitude into a distance.

### 4. `optimizer.py`
Core optimization logic:
- **DeliveryOptimizer**: The main class responsible for optimizing delivery routes.
  - **Methods**:
    - `calculate_distance(loc1, loc2)`: Computes the distance between two locations using the Haversine formula.
    - `calculate_travel_time(distance)`: Calculates the time required to travel a given distance.
    - `evaluate_route(route)`: Evaluates the total time and event log for a given delivery route.
    - `find_optimal_route()`: Finds the optimal delivery route by evaluating all possible permutations of locations.

### 5. `input_handler.py`
Handles user input functions, such as accepting locations for consumers and restaurants, as well as the delivery agent's starting position.

### 6. `main.py`
The entry point of the application that integrates all modules and triggers the optimization process.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Gautamaggrawal/lucidity_delivery_optimizer.git
    cd lucidity_delivery_optimizer
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up configuration values in `config.py` (e.g., speed, radius).

## Usage
Once the dependencies are installed and the configuration is set, you can run the application through the `main.py` file.

Example:
```bash
python main.py

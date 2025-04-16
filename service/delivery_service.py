from datetime import datetime, timedelta
from typing import List
import uuid
from models.model import Order, OrderRequest, OrderResponse, OrderStatus, Vehicle
from service.pathFinding import PathFinding
import math
import osmnx as ox
import heapq
import matplotlib.pyplot as plt
class DeliveryService:

    @staticmethod
    def get_vehicle_by_weight(weight: float) -> Vehicle:
        if weight < 20:
            return Vehicle.MOTORBIKE
        elif 20 <= weight <= 50:
            return Vehicle.CAR
        else:
            return Vehicle.TRUCK


    @staticmethod
    def make_order(orderRequest: OrderRequest) -> OrderResponse:
         # Calculate straight-line distance (approximate)
        dx = orderRequest.destination.x - orderRequest.start.x
        dy = orderRequest.destination.y - orderRequest.start.y
        distance = round(math.sqrt(dx**2 + dy**2) * 111, 2)  # 1 degree ≈ 111 km

        # Define delivery duration based on vehicle type
        delivery_days_map = {
            Vehicle.CAR: 2,
            Vehicle.TRUCK: 3,
            Vehicle.MOTORBIKE: 1
        }

        days_needed = delivery_days_map.get(orderRequest.delivery_vehicle, 2)

        # Calculate expected delivery date
        expected_date = orderRequest.pickup_date + timedelta(days=days_needed)

        # Set estimated delivery time to 3:00 PM on expected date
        estimated_delivery_time = datetime.combine(expected_date, datetime.min.time()).replace(hour=15)

        # Return the full order object
        return Order(
            id=str(uuid.uuid4()),
            product=orderRequest.product,
            start=orderRequest.start,
            destination=orderRequest.destination,
            delivery_vehicle=orderRequest.delivery_vehicle,
            pickup_date=orderRequest.pickup_date,
            expected_date=expected_date,
            estimated_delivery_time=estimated_delivery_time,
            distance=distance,
            status=OrderStatus.PENDING
        )

    @staticmethod
    def get_optimal_path(order: Order) -> str:
        # Extract coordinates from Location models
        start_coord = (order.start.x, order.start.y)
        dest_coord = (order.destination.x, order.destination.y)

        # Create graph for vehicle type
        G = PathFinding(order.delivery_vehicle).G

        # Find path using coordinates
        route = PathFinding.find_path(start_coord, dest_coord, order.delivery_vehicle)
        # print(route)  # Debugging purpose

        # Plot the route
        fig, ax = ox.plot_graph_route(G, route, route_linewidth=4, node_size=0)
        plt.show()

        return "Path calculated successfully"


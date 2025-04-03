from typing import List
from models.model import OrderRequest, Vehicle


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
    def make_order(OrderRequest: OrderRequest) -> Vehicle:
        pass

    @staticmethod
    def get_optimal_path(order_id: int) -> Vehicle:
        pass


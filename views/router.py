from typing import List
from fastapi import APIRouter
from models.model import Order, OrderRequest, Product, OrderResponse, Vehicle
import uuid
from datetime import date

from service.delivery_service import DeliveryService

router = APIRouter(prefix="/delivery", tags=["Delivery"])


# lay tuyen duong toi uu
# fake data để implement thuật toán
@router.post("/get-path", response_model=str)
def get_path(order: Order):
    return DeliveryService.get_optimal_path(order)

# tao don hang
@router.post("/make-order", response_model=OrderResponse)
def make_order(orderRequest: OrderRequest):
    return DeliveryService.make_order(orderRequest)


#  goi y phuong tien dua tren can nang cua hang hoa
@router.post("/get-vehicles", response_model=Vehicle)
def get_recommended_vehicle(weight: float):
    return DeliveryService.get_vehicle_by_weight(weight)

from typing import List
from fastapi import APIRouter
from models.model import Order, OrderRequest, Product, OrderResponse, Vehicle
import uuid
from datetime import date

from service import delivery_service

router = APIRouter(prefix="/delivery", tags=["Delivery"])


# lay tuyen duong toi uu
@router.post("/get-path/{order_id}")
def get_path():
    return delivery_service.get_optimal_path(order_id)

# tao don hang
@router.post("/make-order", response_model=OrderResponse)
def make_order(orderRequest: OrderRequest):
    return delivery_service.make_order(orderRequest)


#  goi y phuong tien dua tren can nang cua hang hoa
@router.post("/get-vehicles", response_model=List[Vehicle])
def get_recommended_vehicle(weight: float):
    return delivery_service.get_vehicle_by_weight(weight)

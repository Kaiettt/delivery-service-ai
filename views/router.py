from typing import List
from fastapi import APIRouter
from models.model import Order, OrderRequest, Product, OrderResponse, Vehicle
import uuid
from datetime import date

from service import delivery_service

router = APIRouter(prefix="/delivery", tags=["Delivery"])


# lay tuyen duong toi uu
# fake data để implement thuật toán
@router.post("/get-path", ... Trả về cái gì cho frontend ghi vô dùm tui ... tạo model responce mới trong file model.py .....)
def get_path(order: Order):
    return delivery_service.get_optimal_path(order)

# tao don hang
@router.post("/make-order", response_model=OrderResponse)
def make_order(orderRequest: OrderRequest):
    return delivery_service.make_order(orderRequest)


#  goi y phuong tien dua tren can nang cua hang hoa
@router.post("/get-vehicles", response_model=List[Vehicle])
def get_recommended_vehicle(weight: float):
    return delivery_service.get_vehicle_by_weight(weight)

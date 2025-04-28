from typing import Optional, Dict
from pydantic import BaseModel, Field
from datetime import date, datetime
from enum import Enum
import uuid

class Vehicle(str, Enum):
    CAR = "CAR"
    TRUCK = "TRUCK"
    MOTORBIKE = "MOTORBIKE"

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"

class Location(BaseModel):
    name:str =Field(...,example="Thu DUc")
    x: float = Field(..., example=10.7769)
    y: float = Field(..., example=106.7009)

class Product(BaseModel):
    name: str = Field(..., example="Laptop")
    description: Optional[str] = Field(None, example="High-performance gaming laptop")
    weight: float = Field(..., example=2.5, description="Weight in kg")
    dimensions: Optional[Dict[str, float]] = Field(None, example={"length": 30, "width": 20, "height": 5})
    price: float = Field(..., example=1200.99)
    fragile: bool = Field(..., example=True, description="Indicates if the product is fragile")

class Order(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), example="ORD12345")
    product: Product
    start: Location
    destination: Location
    delivery_vehicle: Vehicle
    pickup_date: date = Field(..., example="2024-04-02")
    expected_date: date = Field(..., example="2024-04-05")
    status: OrderStatus = Field(default=OrderStatus.PENDING, example="PENDING")
    estimated_delivery_time: Optional[datetime] = Field(None, example="2024-04-05T15:30:00Z")
    distance: float= Field(...,example = 20)

class OrderRequest(BaseModel):
    product: Product
    start: Location
    destination: Location
    delivery_vehicle: Vehicle
    pickup_date: date

class OrderResponse(Order):
    pass

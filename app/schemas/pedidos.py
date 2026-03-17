from typing import Optional
from datetime import date, time, datetime
from pydantic import BaseModel, Field
from app.core.enums import OrderClient, OrderPlant

class PedidoBase(BaseModel):
    """Campos verdaderamente comunes y opcionales"""
    planta: Optional[int] = None
    fecha_entrega: Optional[date] = None
    hora_entrega: Optional[time] = None
    elemento: Optional[str] = None
    volumen_teorico: Optional[float] = None
    volumen_real: Optional[float] = None
    direccion_entrega: Optional[str] = None
    resistencia_requerida: Optional[float] = None

class PedidoCreate(PedidoBase):
    """Schema para crear pedido - campos REQUERIDOS"""
    client_id: int = Field(..., description="ID del cliente")
    order_date: date = Field(..., description="Fecha del pedido")
    
    # Campos opcionales con valores por defecto específicos
    estado_planta: OrderPlant = Field(default=OrderPlant.pending)
    estado_cliente: OrderClient = Field(default=OrderClient.pending)

    # NO incluir fecha_creacion - se genera automáticamente

class PedidoUpdate(BaseModel):
    """Schema para actualizar - solo campos modificables"""
    planta: Optional[int] = None
    fecha_entrega: Optional[date] = None
    hora_entrega: Optional[time] = None
    elemento: Optional[str] = None
    volumen_teorico: Optional[float] = None
    volumen_real: Optional[float] = None
    direccion_entrega: Optional[str] = None
    resistencia_requerida: Optional[float] = None
    estado_planta: Optional[OrderPlant] = None
    estado_cliente: Optional[OrderClient] = None

class PedidoResponse(PedidoBase):
    """Schema para respuesta - incluye todos los campos de BD"""
    id: int
    client_id: int
    order_date: date
    fecha_creacion: datetime  # Cambié a datetime para coincidir con tu modelo
    fecha_entrega: Optional[date] = None
    hora_entrega: Optional[time] = None
    estado_planta: OrderPlant
    estado_cliente: OrderClient

    class Config:
        from_attributes = True

class PedidoWithRelations(PedidoResponse):
    """Schema con datos de relaciones"""
    cliente_username: Optional[str] = None
    planta_username: Optional[str] = None

# Schemas especializados para operaciones específicas
class PedidoUpdateEstado(BaseModel):
    """Solo para actualizar estados"""
    estado_planta: Optional[OrderPlant] = None
    estado_cliente: Optional[OrderClient] = None

class PedidoUpdateVolumen(BaseModel):
    """Solo para actualizar volumen real"""
    volumen_real: float = Field(..., gt=0, description="Volumen real medido")
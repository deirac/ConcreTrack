from sqlalchemy import Column, Integer, String, Enum, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

from app.core.enums import OrderPlant, OrderClient


class Pedido(Base):
    __tablename__ = "pedidos"

    #identificadores 
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    planta = Column(Integer, ForeignKey("users.id"), nullable=True)

    # fechas y horas
    order_date = Column(DateTime, nullable=False)
    fecha_creacion = Column(DateTime, nullable=False)
    fecha_entrega = Column(DateTime, nullable=True)
    hora_entrega = Column(DateTime, nullable=True)

    # detalles del pedido
    elemento = Column(String, nullable=True)
    volumen_teorico = Column(Float, nullable=True)
    volumen_real = Column(Float, nullable=True)
    direccion_entrega = Column(String, nullable=True)
    resistencia_requerida = Column(Float, nullable=True)

    # estados
    estado_planta = Column(Enum(OrderPlant), default=OrderPlant.pending, nullable=False)
    estado_cliente = Column(Enum(OrderClient), default=OrderClient.pending, nullable=False)

    # relaciones
    client = relationship("User", back_populates="pedidos")
    proveedor = relationship("User", foreign_keys=[planta])


from enum import Enum


class Role(str, Enum):
    super = "superadmin"
    admin = "admin"
    operator = "operador"
    client = "cliente"
    supplier = "Proveedor"
    plant = "planta"


class OrderPlant(str, Enum):
    pending = "pendiente"
    in_progress = "preparacion"
    delivering = "en ruta"
    delivered = "Entregado"
    completed = "completed"
    rejected = "Rechazado"
    

class OrderClient(str, Enum):
    pending = "Pendiente"
    approved = "Aprobado"
    cancelled = "Cancelado"
    delivered = "Entregado"
    completed = "Completado"
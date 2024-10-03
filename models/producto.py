class Producto: 
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.precio = data["precio"]
        self.imagen = data["imagen"]
        self.descripcion = data["descripcion"]
        self.id = data["id"]

Productos = [
    {'id': 1, 'nombre': 'Producto 1', 'precio': 10},
    {'id': 2, 'nombre': 'Producto 2', 'precio': 15},
    {'id': 3, 'nombre': 'Producto 3', 'precio': 20},
]

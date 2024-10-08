from config.db import connectToMySQL

class Producto: 
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.precio = data["precio"]
        self.imagen = data["imagen"]
        self.descripcion = data["descripcion"]
        self.id = data["id"]

    @classmethod
    def get_productos(cls, categoria_id):
        query = f"SELECT * FROM producto WHERE categoria_id={categoria_id}"
        results = connectToMySQL("farmacia_veterinaria").query_db(query)
        productos = []
        for producto in results:
            productos.append(cls(producto))
        return productos
from config.db import connectToMySQL
from models.producto import Producto

class Carrito: 
    def __init__(self, data):
        self.id = data["id"]
        self.usuario_id = data["usuario_id"]
        self.proucto_id= data["producto_id"]
        self.cantidad = data["cantidad"]

        self.product = None

    @classmethod
    def get_element(cls, usuario_id, producto_id):
        query = f"SELECT * FROM carrito WHERE usuario_id={usuario_id} AND producto_id={producto_id}"
        result = connectToMySQL("farmacia_veterinaria").query_db(query)
        productos = []
        for producto in result:
            productos.append(cls(producto))
        return productos

    @classmethod
    def insert(cls, usuario_id, producto_id):
        query = f"INSERT INTO carrito (usuario_id, producto_id, cantidad) VALUES ({usuario_id},{producto_id}, 1)"
        result = connectToMySQL("farmacia_veterinaria").query_db(query)
        return result

    @classmethod
    def select_all(cls, usuario_id):
        query = f"""
            SELECT * FROM carrito 
            LEFT JOIN producto 
            ON carrito.producto_id=producto.id 
            WHERE usuario_id={usuario_id}"""
        result = connectToMySQL("farmacia_veterinaria").query_db(query)
        productos = []
        for producto in result:
            tmp = cls(producto)
            tmp.product = Producto(producto)
            productos.append(tmp)
        return productos

    @classmethod
    def update_cant(cls, cant, id):
        query = f"UPDATE carrito SET cantidad={cant} WHERE id={id}"
        result = connectToMySQL("farmacia_veterinaria").query_db(query)
        return result

    @classmethod
    def delete_cart(cls, usuario_id):
        query = f"DELETE FROM carrito WHERE usuario_id={usuario_id}"
        result = connectToMySQL("farmacia_veterinaria").query_db(query)
        return result
    
        
    @classmethod
    def delete_one(cls, user_id, product_id):
        query = f"DELETE FROM carrito WHERE usuario_id = {user_id} AND producto_id={product_id}"
        results = connectToMySQL("farmacia_veterinaria").query_db(query)
        return results




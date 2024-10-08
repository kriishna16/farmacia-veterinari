from flask import Flask, render_template, request, session, redirect
from flask_bcrypt import Bcrypt
from models.producto import Producto
from models.usuario import Usuario
from models.carrito import Carrito

app = Flask(__name__)

bcrypt = Bcrypt(app)

app.secret_key = 'secreto' 



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/veterinaria')
def veterinaria():
    productos = Producto.get_productos(1)
    print(len(productos))
    return render_template('veterinaria.html', productos=productos)

@app.route('/caballos')
def caballos():
    productos = Producto.get_productos(2)
    print(len(productos))
    return render_template('caballos.html', productos=productos)

@app.route('/herraje')
def herraje():
    productos = Producto.get_productos(3)
    print(len(productos))
    return render_template('herraje.html', productos=productos )

@app.route('/corrales')
def corrales():
    productos = Producto.get_productos(4)
    print(len(productos))
    return render_template('corrales.html',productos=productos)

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Saber si existe un usuario con el username que puso la persona
    user = Usuario.select_by_email(username)

    print(username, password, user)
    
    # No existe un usuario con el username ENtonces mandamos error
    if len(user) == 0:
        ## ERROR
        return 
    #Si existe, tenemos que pedirle a bcrypt que revise si la password que metio la persona calza con la guardada
    else:
        user = user[0]
        #Si no calzan las password
        #Tiramos error
        if not bcrypt.check_password_hash(user.password, password):
            return 
        #Si calzan las password (La entregada por el usuario y la guardad en la base de datos)
        # Le asignamos una sesion al usuario y lo redirigimos al inicio "/"
        else:
            session["id"] = user.id
            session["name"] = f"{user.nombre} {user.apellido}"
            return redirect("/")

@app.route('/registrate')
def registrate():
    return render_template('registrate.html')

@app.route("/registro", methods=["POST"])
def register():
    nombre = request.form.get("name")
    apellido = request.form.get("lastname")
    email = request.form.get("email")
    password = request.form.get("contrasena")

    user = Usuario.select_by_email(email)
    ## Existe un usuario con el email
    if len(user) > 0:
        return "error"
    ##Error

    # Encriptar la password
    password = bcrypt.generate_password_hash(password).decode("utf-8")
    # Insertar usuario en base de datos
    Usuario.insert_one(nombre, apellido, email, password)
    # Redirigir el usuario a la pag. inicial

    return redirect("/")

@app.route('/carrito')
def carrito():
    user_id = session["id"]
    elments = Carrito.select_all(user_id)
    print(elments[0].proucto_id)
    return render_template('carrito.html', carrito_elements=elments)


@app.route("/shopping_cart/delete", methods=["POST"])
def delete_product():
    user_id = session["id"]
    producto_id = request.form.get("producto_id")
    print(user_id, request.form)
    Carrito.delete_one(user_id, producto_id)
    return redirect("/carrito")

@app.route("/shopping_cart/add/", methods=["POST"])
def add_product():
    user_id = session["id"]
    prod_id = request.form.get("prod_id")

    # Revisar si está en el carrito
    print(user_id, prod_id)
    elmt = Carrito.get_element(user_id, prod_id)
    if len(elmt) == 0:
        ## Caso donde hay que insertar
        Carrito.insert(user_id, prod_id)
    else:
        elmt = elmt[0]
        ## caso donde hay que actualizar la cantidad
        cant = elmt.cant + 1
        elmt_id = elmt.id
        Carrito.update_cant(cant, elmt_id)

    print(elmt)
    return redirect("/")

if __name__ == '__main__':
    
    app.run(debug=True)

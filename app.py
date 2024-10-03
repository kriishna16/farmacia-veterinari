from flask import Flask, render_template, request, session, redirect
from flask_bcrypt import Bcrypt
from models producto import Productos
from models.usuario import Usuario

app = Flask(__name__)

bcrypt = Bcrypt(app)

app.secret_key = 'secreto' 



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/veterinaria')
def veterinaria():
    return render_template('veterinaria.html')

@app.route('/caballos')
def caballos():
    return render_template('caballos.html')

@app.route('/herraje')
def herraje():
    return render_template('herraje.html')

@app.route('/corrales')
def corrales():
    return render_template('corrales.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Saber si existe un usuario con el username que puso la persona
    user = Usuario.select_by_email(username)
    
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

    # Insertar usuario en base de datos
    Usuario.insert_one(nombre, apellido, email, password)
    # Redirigir el usuario a la pag. inicial

    return redirect("/")




@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/producto/<int:id>')
def obtener_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    return jsonify(producto)







if __name__ == '__main__':
    
    app.run(debug=True)

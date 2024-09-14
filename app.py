from flask import Flask, render_template

app = Flask(__name__)

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
if __name__ == '__main__':
    
    app.run(debug=True)

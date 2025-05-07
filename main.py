from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "<P>Hola Mariella</P>"

@app.route("/despedida")
def despedida():
    return "<p>Muchas gracias por la visita!!</P>"    

@app.route("/saludo")
def saludo():
    return render_template('Saludos.html')    


@app.route("/saludo_nombre")
def saludo_nombre():
    return render_template('saludar_nombre.html', nombre="Nay")  



@app.route("/saludo_nombre_apellido")
def saludo_nombre_apellido():
    return render_template('saludar_nombre_apellido.html', nombre="Mariella", apellido="Nay") 


@app.route("/saludo_nombre_apellido_edad")
def saludo_nombre_apellido_edad():
    return render_template('saludar_nombre_apellido_edad.html', nombre="Mariella", apellido="Nay", edad=47 ) 


if __name__ == '__main__':
    app.run(debug=True)

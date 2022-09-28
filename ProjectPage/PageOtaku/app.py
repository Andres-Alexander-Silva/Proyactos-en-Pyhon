from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import session
from flask_mail import Mail
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import psycopg2.extras
import re
##Inicializamos la app
app = Flask(__name__)
##Configuracion del envio de correos
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = "andresalexandersp@gmail.com"
app.config["MAIL_PASSWORD"] = "MikuxFutaro07"
mail = Mail()
##Configuracion de la base de datos
DB_HOST = "localhost"
DB_NAME = "PageOtakuDB"
DB_USER = "postgres"
DB_PASS = "kateandres"
coneccion = psycopg2.connect(dbname=DB_NAME,user=DB_USER,
                             password=DB_PASS,host=DB_HOST)
##Llave secreta
app.secret_key = "mysecretkeyotakupageandres"
##Ruta principal
@app.route("/")
@app.route("/inicio")
def inicio():
    titulo = "Inicio"
    return render_template("home.html", title=titulo)
##Ruta de inicio cuando el usuario este logiado
@app.route("/inicio-perfil")
def inicio2():
    titulo = "Inicio"
    return  render_template("home-usuario.html",title=titulo)
##Ruta del apartado de noticias
@app.route("/noticias")
def noticias():
    titulo = "Noticias"
    return render_template("noticias.html", title=titulo)
##Ruta del apartado de los post del blog
@app.route("/blog")
def blog():
    titulo = "Blog"
    return render_template("blog.html", title=titulo)
##Ruta del formulario de contacto
@app.route("/contacto", methods=["GET","POST"])
def contacto():
    titulo = "Contactanos"
    ##Condicional que evalua si los datos se envian por el metodo POST
    if request.method == "POST":
        ##Recopilacion de los campos del formulario
        nombre = request.form.get("nombre_env")
        correo = request.form.get("correo")
        asunto = request.form.get("asunto")
        mensaje = request.form.get("mensaje")
        ##Creacion del mensaje
        msg = Message(subject=asunto,body=f"Nombre del Remitente: {nombre}\nCorreo del Remitente: {correo}\n\n{mensaje}",
                      sender=correo,recipients=[app.config["MAIL_USERNAME"],])
        mail.send(msg)
        ##Mensaje de envio satisfactorio
        flash("Envio del mensaje exitoso.")
        return redirect(url_for("contacto"))
    return render_template("contacto.html", title=titulo)
##Ruta del formulario de inicio de seision
@app.route("/login", methods=["GET","POS"])
def login():
    titulo = "Inicio de Sesion"
    return render_template("login.html", title=titulo)
##Ruta del formulario de registro
@app.route("/sing-up",methods=["GET","POST"])
def sing_up():
    cursor = coneccion.cursor(cursor_factory=psycopg2.extras.DictCursor)
    ##Condicional que evalua que los datos se envien en POST
    if request.method == "POST":
        ##Recopilacion de los datos del formulario
        nombre = request.form["nombre_registro"]
        apellido = request.form["apellido_registro"]
        correo = request.form["email_registro"]
        telefono = request.form["telefono_registro"]
        edad = request.form["edad_registro"]
        genero = request.form["genero_registro"]
        usuario = request.form["usuario_registro"]
        password = request.form["pass_registro"]
        ##Encriptamiento de la contaseña
        password_encirptado = generate_password_hash(password)
        ##Confirmar si una cuenta existe
        cursor.execute("SELECT * FROM users WHERE usuario = %s",(usuario,))
        cuenta = cursor.fetchone()
        ##Mostrar error si la cuenta existe y validar datos
        if cuenta:
            flash("Esta cuenta ya existe.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+",correo):
            flash("Correo invalido.")
        elif not re.match(r"[A-Za-z0-9]+",usuario):
            flash("El usuario debe contener caractere y numeros.")
        elif not usuario or not password or not correo:
            flash("Por favor llenar el formulario.")
        else:
            ##Si la cuenta no existe y los datos no validos del formulario crear usuario en la tabla
            cursor.execute("INSERT INTO users (nombre,apellido,correo,telefono,edad,genero,usuario,contraseña) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                           (nombre,apellido,correo,telefono,edad,genero,usuario,password_encirptado))
            coneccion.commit()
            flash("Usuario registrado exitosamente.")
    titulo = "Registrarse"
    return render_template("sing-up.html", title=titulo)
##Ruta perfil del usuario
@app.route("/perfil")
def perfil():
    titulo = "Perfil"
    return render_template("perfil-usuarios.html", title=titulo)

##@app.route("/salir")
##def salir():
##    session.clear()
##   return redirect(url_for("inicio"))

if __name__ == "__main__":
    mail.init_app(app)
    app.run(debug=True, port=5500)
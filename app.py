from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import os  # Importa os para manejar directorios

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///respuestas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo completo para las respuestas
class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formulario = db.Column(db.String(50), nullable=False)
    
    # Datos del empleado
    nombre = db.Column(db.String(50), nullable=True)
    apellido = db.Column(db.String(50), nullable=True)
    vivienda = db.Column(db.String(100), nullable=True)
    departamento = db.Column(db.String(50), nullable=True)
    estado_civil = db.Column(db.String(20), nullable=True)
    genero = db.Column(db.String(20), nullable=True)
    edad = db.Column(db.Integer, nullable=True)
    salario = db.Column(db.Integer, nullable=True)
    cargo = db.Column(db.String(50), nullable=True)
    estrato = db.Column(db.Integer, nullable=True)

    # Sección Amor
    relacion = db.Column(db.Integer, nullable=True)
    expresion_amor = db.Column(db.Integer, nullable=True)
    apertura_relaciones = db.Column(db.Integer, nullable=True)
    esfuerzo_relaciones = db.Column(db.Integer, nullable=True)
    claridad_amor = db.Column(db.Integer, nullable=True)

    # Sección Economía
    manejo_dinero = db.Column(db.Integer, nullable=True)
    responsabilidad_financiera = db.Column(db.Integer, nullable=True)
    metas_financieras = db.Column(db.Integer, nullable=True)
    habito_ahorro = db.Column(db.Integer, nullable=True)
    satisfaccion_trabajo_estudios = db.Column(db.Integer, nullable=True)

    # Sección Salud
    estado_fisico_mental = db.Column(db.Integer, nullable=True)
    cuidado_cuerpo = db.Column(db.Integer, nullable=True)
    calidad_sueno = db.Column(db.Integer, nullable=True)
    manejo_estres_emociones = db.Column(db.Integer, nullable=True)
    habitos_saludables = db.Column(db.Integer, nullable=True)

    # Sección Desarrollo
    aprendizaje_desarrollo = db.Column(db.Integer, nullable=True)
    claridad_metas_suenos = db.Column(db.Integer, nullable=True)
    esfuerzo_maximo_potencial = db.Column(db.Integer, nullable=True)
    pasion_motivacion = db.Column(db.Integer, nullable=True)
    crecimiento_personal = db.Column(db.Integer, nullable=True)

    fecha_envio = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def empleado():
    if request.method == "POST":
        nueva_respuesta = Respuesta(
            formulario="empleado",
            nombre=request.form["nombre"],
            apellido=request.form["apellido"],
            vivienda=request.form["vivienda"],
            departamento=request.form["departamento"],
            estado_civil=request.form["estado_civil"],
            genero=request.form["genero"],
            edad=request.form["edad"],
            salario=request.form["salario"],
            cargo=request.form["cargo"],
            estrato=request.form["estrato"]
        )
        db.session.add(nueva_respuesta)
        db.session.commit()
        return redirect(url_for("amor", id=nueva_respuesta.id))

    return render_template("empleado.html")

@app.route("/amor/<int:id>", methods=["GET", "POST"])
def amor(id):
    respuesta = Respuesta.query.get_or_404(id)
    if request.method == "POST":
        respuesta.relacion = request.form["relaciones"]
        respuesta.expresion_amor = request.form["expresion_amor"]
        respuesta.apertura_relaciones = request.form["apertura_relaciones"]
        respuesta.esfuerzo_relaciones = request.form["esfuerzo_relaciones"]
        respuesta.claridad_amor = request.form["claridad_amor"]
        db.session.commit()
        return redirect(url_for("economia", id=id))

    return render_template("amor.html", id=id)

@app.route("/economia/<int:id>", methods=["GET", "POST"])
def economia(id):
    respuesta = Respuesta.query.get_or_404(id)
    if request.method == "POST":
        respuesta.manejo_dinero = request.form["manejo_dinero"]
        respuesta.responsabilidad_financiera = request.form["responsabilidad_financiera"]
        respuesta.metas_financieras = request.form["metas_financieras"]
        respuesta.habito_ahorro = request.form["habito_ahorro"]
        respuesta.satisfaccion_trabajo_estudios = request.form["satisfaccion_trabajo_estudios"]
        db.session.commit()
        return redirect(url_for("salud", id=id))

    return render_template("economia.html", id=id)

@app.route("/salud/<int:id>", methods=["GET", "POST"])
def salud(id):
    respuesta = Respuesta.query.get_or_404(id)
    if request.method == "POST":
        respuesta.estado_fisico_mental = request.form["estado_fisico_mental"]
        respuesta.cuidado_cuerpo = request.form["cuidado_cuerpo"]
        respuesta.calidad_sueno = request.form["calidad_sueno"]
        respuesta.manejo_estres_emociones = request.form["manejo_estres_emociones"]
        respuesta.habitos_saludables = request.form["habitos_saludables"]
        db.session.commit()
        return redirect(url_for("desarrollo", id=id))

    return render_template("salud.html", id=id)

@app.route("/desarrollo/<int:id>", methods=["GET", "POST"])
def desarrollo(id):
    respuesta = Respuesta.query.get_or_404(id)
    if request.method == "POST":
        respuesta.aprendizaje_desarrollo = request.form["aprendizaje_desarrollo"]
        respuesta.claridad_metas_suenos = request.form["claridad_metas_suenos"]
        respuesta.esfuerzo_maximo_potencial = request.form["esfuerzo_maximo_potencial"]
        respuesta.pasion_motivacion = request.form["pasion_motivacion"]
        respuesta.crecimiento_personal = request.form["crecimiento_personal"]
        db.session.commit()
        return redirect(url_for("success"))

    return render_template("desarrollo.html", id=id)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/ver_respuestas")
def ver_respuestas():
    respuestas = Respuesta.query.all()
    return render_template("ver_respuestas.html", respuestas=respuestas)

@app.route("/eliminar_respuesta/<int:id>", methods=["POST"])
def eliminar_respuesta(id):
    respuesta = Respuesta.query.get_or_404(id)
    db.session.delete(respuesta)
    db.session.commit()
    return redirect(url_for("ver_respuestas"))

# ==========================
# EXPORTAR DATOS CSV y JSON
# ==========================
@app.route("/exportar_csv")
def exportar_csv():
    try:
        with app.app_context():
            df = pd.read_sql("SELECT * FROM Respuesta", db.engine)

            carpeta = "exportaciones"
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)

            ruta_archivo = os.path.join(carpeta, "respuestas.csv")
            df.to_csv(ruta_archivo, index=False)

        return f"Archivo CSV exportado correctamente en: {ruta_archivo}"
    except Exception as e:
        return f"Error al exportar CSV: {e}"

@app.route("/exportar_json")
def exportar_json():
    try:
        with app.app_context():
            df = pd.read_sql("SELECT * FROM Respuesta", db.engine)

            carpeta = "exportaciones"
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)

            ruta_archivo = os.path.join(carpeta, "respuestas.json")
            df.to_json(ruta_archivo, orient="records", indent=4)

        return f"Archivo JSON exportado correctamente en: {ruta_archivo}"
    except Exception as e:
        return f"Error al exportar JSON: {e}"

if __name__ == "__main__":
    app.run(debug=True)

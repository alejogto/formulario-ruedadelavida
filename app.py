from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Formulario de Empleado (No cambió)
@app.route("/empleado", methods=["GET", "POST"])
def empleado():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        vivienda = request.form["vivienda"]
        departamento = request.form["departamento"]
        estado_civil = request.form["estado_civil"]
        genero = request.form["genero"]
        edad = request.form["edad"]
        salario = request.form["salario"]
        cargo = request.form["cargo"]
        estrato = request.form["estrato"]
        return redirect(url_for("success"))
    return render_template("empleado.html")

#  Formulario de Amor
@app.route("/amor", methods=["GET", "POST"])
def amor():
    if request.method == "POST":
        relaciones = request.form["relaciones"]
        expresion_amor = request.form["expresion_amor"]
        apertura_relaciones = request.form["apertura_relaciones"]
        esfuerzo_relaciones = request.form["esfuerzo_relaciones"]
        claridad_amor = request.form["claridad_amor"]
        return redirect(url_for("success"))
    return render_template("amor.html")

#  Formulario de Economía
@app.route("/economia", methods=["GET", "POST"])
def economia():
    if request.method == "POST":
        manejo_dinero = request.form["manejo_dinero"]
        responsabilidad_financiera = request.form["responsabilidad_financiera"]
        metas_financieras = request.form["metas_financieras"]
        habito_ahorro = request.form["habito_ahorro"]
        satisfaccion_trabajo_estudios = request.form["satisfaccion_trabajo_estudios"]
        return redirect(url_for("success"))
    return render_template("economia.html")

#  Formulario de Salud
@app.route("/salud", methods=["GET", "POST"])
def salud():
    if request.method == "POST":
        estado_fisico_mental = request.form["estado_fisico_mental"]
        cuidado_cuerpo = request.form["cuidado_cuerpo"]
        calidad_sueno = request.form["calidad_sueno"]
        manejo_estres_emociones = request.form["manejo_estres_emociones"]
        habitos_saludables = request.form["habitos_saludables"]
        return redirect(url_for("success"))
    return render_template("salud.html")

#  Formulario de Desarrollo Personal
@app.route("/desarrollo", methods=["GET", "POST"])
def desarrollo():
    if request.method == "POST":
        aprendizaje_desarrollo = request.form["aprendizaje_desarrollo"]
        claridad_metas_suenos = request.form["claridad_metas_suenos"]
        esfuerzo_maximo_potencial = request.form["esfuerzo_maximo_potencial"]
        pasion_motivacion = request.form["pasion_motivacion"]
        crecimiento_personal = request.form["crecimiento_personal"]
        return redirect(url_for("success"))
    return render_template("desarrollo.html")

#  Página de éxito
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)

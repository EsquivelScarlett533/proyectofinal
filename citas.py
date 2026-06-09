from flask import Blueprint, render_template, request, redirect, url_for
from database import db

citas_bp = Blueprint('citas', __name__)
col = db['citas']

@citas_bp.route("/")
def ver_citas():
    lista = list(col.find())
    return render_template('citas.html', citas=lista)

@citas_bp.route("/nueva")
def formulario():
    return render_template('formcitas.html')

@citas_bp.route("/guardar", methods=["POST"])
def guardar():
    ultimo = col.find_one(sort=[("id_cita", -1)])
    nuevo_id = (ultimo["id_cita"] + 1) if ultimo else 1
    
    col.insert_one({
        "id_cita":      nuevo_id,
        "paciente":     request.form.get("paciente"),
        "medico":       request.form.get("medico"),
        "especialidad": request.form.get("especialidad"),
        "consultorio":  request.form.get("consultorio")
    })
    return redirect(url_for('citas.ver_citas'))
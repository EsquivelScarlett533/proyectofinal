from flask import Blueprint, render_template, request, redirect, url_for
from database import db 

pacientes_bp = Blueprint('pacientes', __name__)
col = db['pacientes']

@pacientes_bp.route("/")
def ver_pacientes():
    lista = list(col.find({}, {'_id': 0}))
    return render_template('pacientes.html', pacientes=lista)

@pacientes_bp.route("/nuevo")
def formulario(): 
    return render_template('formpacientes.html')

@pacientes_bp.route("/guardar", methods=["POST"])
def guardar():
    ultimo = col.find_one({"id_paciente": {"$type": "int"}}, sort=[("id_paciente", -1)])
    nuevo_id = (ultimo["id_paciente"] + 1) if ultimo else 1

    col.insert_one({
        "id_paciente":  nuevo_id,
        "nombre":       request.form.get("nombre"),
        "edad":         request.form.get("edad"),
        "diagnostico":  request.form.get("diagnostico"),
        "medicamentos": request.form.get("medicamentos")
    })
    return redirect(url_for('pacientes.ver_pacientes'))
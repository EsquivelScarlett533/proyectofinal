from flask import Flask 
from database import db

app = Flask(__name__)

# Importaciones corregidas (sin el "routes." porque están en la raíz)
from index import index_bp
from pacientes import pacientes_bp
from medicos import medicos_bp
from citas import citas_bp

# Registro de blueprints corregido (sin la "r" extra en la línea de index)
app.register_blueprint(index_bp)
app.register_blueprint(pacientes_bp, url_prefix='/pacientes')
app.register_blueprint(medicos_bp, url_prefix='/medicos')
app.register_blueprint(citas_bp, url_prefix='/citas')

if __name__ == "__main__":
    app.run(debug=True)
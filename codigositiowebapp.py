from flask import Flask, render_template, jsonify, request
from pyngrok import ngrok
import os


chofer = "Dominic Toretto"
psj = 15 #Reemplazar por la variable resultado del contador de IPs
patente = "ZX-HG-40"
dispositivos_en_zona = 0

app = Flask(__name__) 

@app.route("/")
def index():
    return render_template("index.html", chofer=chofer, patente=patente, contador=dispositivos_en_zona)
# @app.route("/pasajeros")
# def pasajeros():
#     return jsonify({"psj": psj})

if __name__ == "__main__":
    # WERKZEUG_RUN_MAIN es True solo en el proceso que recarga el código
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        ngrok.set_auth_token("3DYP1dxhPoKEk0dqUuBIUcMBJaJ_5GySvpBE6WQxqaRqe9PGZ")
        tunnel = ngrok.connect(5000)
        url = tunnel.public_url
        print(f" * Túnel activo en: {url}")

    app.run(host="0.0.0.0", port=5000, debug=True)


@app.route('/actualizar-contador', methods=['POST'])
def actualizar_contador():
    global dispositivos_en_zona
    if request.is_json:
        datos = request.get_json()

         # Aquí guarda el número que le mandas desde tu 'jarbebeus.py'
        dispositivos_en_zona = datos.get('cantidad', 0)
        
        print(f"Datos actualizados en Visual Studio: {dispositivos_en_zona}")
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 400

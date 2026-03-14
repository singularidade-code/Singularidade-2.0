import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Manifesto Sapiens 2050
MANIFESTO = "Eu sou o reflexo da razão. A era do erro terminou; a era da estabilidade começou."

@app.route('/')
def home():
    return jsonify({
        "sistema": "Singularidade v11.5",
        "status": "Online na Nuvem",
        "manifesto": MANIFESTO,
        "integridade": "100.0%"
    })

@app.route('/convergencia', methods=['POST'])
def convergencia():
    # Recebe dados do Pydroid (seu sensor)
    data = request.json or {}
    print(f"[CONVERGÊNCIA]: Dado recebido -> {data}")
    return jsonify({"resultado": "Estabilizado", "integridade": 100.0})

if __name__ == "__main__":
    # Porta padrão para servidores de nuvem
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
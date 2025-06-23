from flask import Flask, request, jsonify
from app.reservas import verificar_disponibilidad

app = Flask(__name__)
reservas = []  # Base de datos temporal en memoria


@app.route('/reservar', methods=['POST'])
def reservar():
    data = request.get_json()  # Ej: {"sala": "A", "hora": "10:00"}
    disponible = verificar_disponibilidad(reservas, data)

    if disponible:
        reservas.append(data)
        return jsonify({"mensaje": "Reserva exitosa"}), 201
    else:
        return jsonify({"mensaje": "Sala no disponible"}), 409


if __name__ == '__main__':
    app.run(debug=True)
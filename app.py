from flask import Flask, request, jsonify
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json()
    nombre = data.get('nombre')
    correo = data.get('correo')

    mensaje = f"Nuevo usuario registrado: {nombre} ({correo})"
    destinatario = os.getenv('ADMIN_EMAIL')

    try:
        with smtplib.SMTP(os.getenv('SMTP_HOST'), int(os.getenv('SMTP_PORT'))) as server:
            server.starttls()
            server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASS'))
            server.sendmail(os.getenv('SMTP_USER'), destinatario, mensaje)
        return jsonify({'status': 'ok'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

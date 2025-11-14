from flask import Flask, request, jsonify
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json()
    nombre = data.get('nombre')
    correo = data.get('correo')

    mensaje = data.get('mensaje', f"Nuevo usuario registrado: {nombre} ({correo})")
    destinatario = os.getenv('ADMIN_EMAIL')

    try:
        msg = MIMEText(mensaje)
        msg['Subject'] = "Nuevo registro de usuario"
        msg['From'] = os.getenv('SMTP_USER')
        msg['To'] = destinatario

        with smtplib.SMTP(os.getenv('SMTP_HOST'), int(os.getenv('SMTP_PORT'))) as server:
            server.starttls()
            server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASS'))
            server.send_message(msg)

        print(f"📤 Correo enviado al administrador: {destinatario}")
        return jsonify({'status': 'ok'}), 200

    except Exception as e:
        print("⚠️ Error al enviar correo:", str(e))
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

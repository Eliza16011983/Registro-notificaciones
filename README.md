# Microservicio de Notificaciones

Este módulo se encarga de enviar correos electrónicos cuando se registra un nuevo usuario.

## Tecnologías
- Python 3
- Flask (opcional)
- SMTP (correo)

## Estructura
- `main.py`: punto de entrada
- `email_sender.py`: lógica para enviar correos
- `.env`: credenciales de correo (no se versiona)

## Configuración
1. Crear entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

2.Instalar dependencias:
pip install -r requirements.txt

3.Ejecutar servicio:
python main.py

Notas

    El backend hace una solicitud HTTP a este servicio para disparar el correo.

    Verificar que las variables de entorno estén correctamente configuradas.

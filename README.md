# Servicio de Notificaciones

Este módulo no contiene un servicio independiente. El envío de correos electrónicos se realiza directamente desde el backend utilizando el sistema de correo de Django (`django.core.mail`), que internamente utiliza la librería `smtplib`.

## 📦 Funcionalidad

Al registrar un nuevo usuario desde el frontend:

1. El backend recibe los datos mediante una solicitud `POST`.
2. Guarda el usuario en la base de datos.
3. Ejecuta la función `send_mail`, que envía un correo de confirmación al usuario registrado.

## 🔐 Seguridad

Las credenciales del correo se gestionan mediante variables de entorno definidas en un archivo `.env`, que no se versiona. Se utiliza la librería `python-dotenv` para cargar estas variables de forma segura.

## 🧪 Pruebas

Se realizaron pruebas con distintos correos electrónicos y se verificó la recepción de los mensajes en la bandeja de entrada. El flujo completo fue validado localmente, incluyendo:

- Registro desde el frontend
- Procesamiento en el backend
- Envío de correo exitoso

## 📁 Estructura

Este repositorio puede incluir documentación o ejemplos relacionados con el envío de correos, pero no contiene un script ejecutable como `main.py`.


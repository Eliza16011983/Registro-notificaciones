# Servicio de Notificaciones- microservicio independiente

Microservicio responsable de procesar las notificaciones cuando se crea un nuevo usuario.
En la opción A del laboratorio, el servicio NO utiliza SES sino un mecanismo simple (por ejemplo loguear o enviar hacia un correo único permitido).


## Funcionalidad
Recibir una solicitud desde la API principal indicando que se creó un usuario, y realizar la acción de “notificar”.

Al registrar un nuevo usuario desde el frontend:

1. El backend recibe los datos mediante una solicitud `POST`.
2. Guarda el usuario en la base de datos.
3. Ejecuta la función `send_mail`, que envía un correo de confirmación al usuario registrado.

## Estructura
main.py / app.py
k8s/
   deployment.yaml
   service.yaml
Dockerfile

## Rutas
Método      Ruta            Descripción
POST       /notify      Recibe datos del nuevo usuario


## Flujo
1- El backend crea un usuario.
2- El backend envía una solicitud al servicio de notificaciones.
3- El servicio procesa la solicitud.
4- Registra el evento en logs.

## Comando para ver logs
kubectl logs -l app=notificaciones --tail=50

## Despliegue
docker build -t notificaciones:latest .
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml




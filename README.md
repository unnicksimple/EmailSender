# EmailSender
/*********************************************
*                                            *
*      Desarrollado por Luis Suárez          *
*      Contacto: unnicksimple@gmail.com      *
*      Licencia: MIT                         *
*                                            *
**********************************************/

# Envío de Correos Automatizado

Este proyecto permite enviar correos electrónicos automatizados a múltiples destinatarios a partir de un archivo CSV. Es ideal para campañas de correo, notificaciones en masa, o comunicación eficiente con listas de contactos.

## Estructura del Proyecto

- `email_sender.py` - Módulo principal que define la clase `EmailSender`, encargada de gestionar la conexión SMTP y el envío de correos electrónicos.
- `send_campaign.py` - Script de implementación para ejecutar el envío en masa utilizando `EmailSender`. Carga destinatarios desde un archivo CSV.
- `.env` - Archivo de configuración que contiene las credenciales de correo electrónico para la autenticación SMTP.

## Requisitos

- Python 3.6+
- Paquetes adicionales: `smtplib`, `dotenv`

## Configuración

1. Clonar el repositorio.
2. Instalar las dependencias con `pip install -r requirements.txt`.
3. Crear un archivo `.env` con las siguientes variables:
   USER=tu_correo@gmail.com
   PASS=tu_contraseña

## Uso

1. Asegúrate de que el archivo CSV con las direcciones de correo electrónico esté en el mismo directorio o proporciona la ruta completa. El archivo debe contener las direcciones en la primera columna.
2. Ejecuta el script de campaña con:
    `python send_campaign.py`

## Licencia
Este proyecto está bajo la licencia MIT.

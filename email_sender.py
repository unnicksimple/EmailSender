import os
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

'''
*******************************************
*   Desarrollado por Luis Suárez          *
*   unnicksimple@gmail.com                *
*   Licencia MIT                          *
*******************************************
'''

class EmailSender:

    def __init__(self):
        load_dotenv()
        self.remitente = os.getenv('USER')
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.remitente, os.getenv('PASS'))

    def send(self, destinatario, asunto, contenido, imagen=None):
        try:
            msg = MIMEMultipart()
            msg['Subject'] = asunto
            msg['From'] = self.remitente
            msg['To'] = destinatario
            msg.attach(MIMEText(contenido,'html'))

            if imagen is not None:
                with open(imagen, 'rb') as f:
                    img = MIMEImage(f.read())
                    img.add_header('Content-ID', '<image1>')
                    msg.attach(img)
            
            self.server.sendmail(self.remitente, destinatario,msg.as_string())

        except smtplib.SMTPRecipientsRefused:
            print(f"Error: La dirección de correo '{destinatario}' fue rechazada.")
        except smtplib.SMTPHeloError:
            print("Error: El servidor SMTP no aceptó el saludo.")
        except smtplib.SMTPSenderRefused:
            print("Error: El servidor rechazó el remitente.")
        except smtplib.SMTPDataError:
            print(f"Error: Se produjo un problema de datos con '{destinatario}'.")
        except Exception as e:
            print(f"Error inesperado al enviar a '{destinatario}': {e}")

    def close_cxn(self):
        self.server.quit()

if __name__ == '__main__':
    correo = EmailSender()
    correo.send('unnicksimple@gmail.com', 'Asunto Test', 'Contenido del mensaje')
    print('enviado!!!')

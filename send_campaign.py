'''
**********************************************
*                                            *
*      Desarrollado por Luis Suárez          *
*      Contacto: unnicksimple@gmail.com      *
*      Licencia: MIT                         *
*                                            *
**********************************************
'''
import email_sender
import csv 


asunto = 'Apoyo a Pymes de la zona'
cuerpo = f'''Cuerpo del mensaje'''

email = email_sender.EmailSender()

# Cargando archvios de csv
with open('datos.csv', 'r') as f:
  reader = csv.reader(f)

  for r in reader:
    try:
      email.send(r[0], asunto, cuerpo)
      print(f'Enviado {r[0]}')
    except Exception as e:
      print(f"Error inesperado al enviar a '{r[0]}': {e}")

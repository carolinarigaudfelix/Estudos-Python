#Enviando E-mails SMTP com Python
import os
import pathlib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv #type: ignore
import smtplib

load_dotenv()

#Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula184.html'


#Dados do remetente
remetente = os.getenv('FROM_EMAIL','')
destinatario = remetente

#Configurações servidores SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

#mensagem de Texto
with open(CAMINHO_HTML, 'r', encoding='utf8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Carol')


#Transformar mensagem em MIMEMultiParte
#quem ta enviando pra quem e assunto
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Esse é o assunto do email'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo() #inicia o server
    server.starttls() #inicia uma conexão segura
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso')
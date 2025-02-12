import os

MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
MYSQL_REPONSE = ''
LIENAPISMS= os.environ.get('LIENAPISMS')
CODECRYPTAGE=os.environ.get('CODECRYPTAGE')


connected_cashiers = {}
socketio  = {}
LIENCLIENT='http://localhost:4200/'


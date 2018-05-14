from client import Client

client = Client()
client.Connect('127.0.0.1',5000)
client.SendInfo('Esto es una prueba.')
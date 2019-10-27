import socket as socket

HOST = '127.0.0.1'
PORT = 5432
MAX_PENDING = 5
MAX_LINE = 256


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen(MAX_PENDING)
  connection, address = s.accept()
  with connection:
    print('Connected with:', address)
    while True:
      data = connection.recv(MAX_LINE)
      if not data:
        break
      print(repr(data))
      connection.sendall(data)


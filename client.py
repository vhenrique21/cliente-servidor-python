import socket as socket
import sys
import re


PORT = 5432
MAX_LINE = 256


if len(sys.argv) > 1:
  userInput = sys.argv[1]
  
  [address, portAndFile] = userInput.split(":",1)
  [port,fileName] = portAndFile.split('/',1)

  regex = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
  result = regex.match(address)
  if not result:
      address = socket.gethostbyname(address)
  if not (port and fileName and address):
    print("Entrada invalida")
  
else:     
  print('usage: simplex-talk host \n', file=sys.stderr)
  exit(1)

hp = socket.gethostbyname(HOST)
if not hp:
  print('simplex-talk: unknowmn host: ' + hp, file=sys.stderr)  
  exit(1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  if not s:
    print('simplex-talk: socket', file=sys.stderr)  
  if not s.connect((hp, PORT)):
    print('simplex-talk: connect', file=sys.stderr)  

  while True:
    line = sys.stdin.readline(MAX_LINE)
    line = line
    print(len(line))
    s.send(str.encode(line))




  # for line in sys.stdin:
  #   s.send(str.encode(line))
import socket as socket
import sys
import re


PORT = 5432
MAX_LINE = 256


if len(sys.argv) > 1:
    userInput = sys.argv[1]

    [address, portAndFile] = userInput.split(":", 1)
    [port, fileName] = portAndFile.split('/', 1)
    name = address
    port = int(port)

    regex = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    result = regex.match(address)

    if not result:
        address = socket.gethostbyname(address)

    if not (port and fileName and address):
        print("Entrada invalida")

else:
    print('usage: simplex-talk host \n', file=sys.stderr)
    exit(1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    if not s:
        print('simplex-talk: socket', file=sys.stderr)

    if not s.connect((address, port)):
        print('simplex-talk: connect', file=sys.stderr)
    print('connected')

    message = "GET /{fileName} HTTP/1.1\nHost: {address}\n".format(
        fileName=fileName, address=name)
    s.send(str.encode(message))

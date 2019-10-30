import socket as socket

HOST = '127.0.0.1'
PORT = 5001
MAX_PENDING = 5
MAX_LINE = 256
MAX_SEND_LINE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(MAX_PENDING)
    while True:
        connection, address = s.accept()
        with connection:
            print('Connected with:', address, "\n")
            while True:
                data = connection.recv(MAX_LINE)
                if not data:   
                    break

                decodeData = data.decode()

                [HTTPmethod, filePath, httpVersion, host, hostName,
                *others] = decodeData.split()

                filePath = filePath.split("/")[1]

                if (HTTPmethod != "GET") or (httpVersion != "HTTP/1.1"):
                    print("Erro")
                    connection.sendall(str.encode("Error"))
                    break

                address = socket.gethostbyname(hostName)

                try:
                    with open(filePath, mode='rb') as file:  # b is important -> binary
                        fileContent = file.read()

                    message = "HTTP/1.1 200 OK\nContent-Length: {fileLength}\nContent-Type: text\n\n".format(
                    fileLength=len(fileContent))
                    connection.send(str.encode(message), MAX_SEND_LINE)
                    connection.sendall(fileContent, MAX_SEND_LINE)
                    file.close()
                    break
                except:
                    errorMessage = "HTTP/1.1 400 ERRO\n\n"
                    connection.send(str.encode(errorMessage), MAX_SEND_LINE)
                    file.close()
                    break
            connection.close()

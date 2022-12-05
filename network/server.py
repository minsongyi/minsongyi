import socket

# TCP/IP 소켓을 생성하고
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓을 포트에 연결
server_address = ('localhost', 10000)
print('Startinf up on {} port {}'.format(*server_address))
sock.bind(server_address)

# 연결을 기다림
sock.listen()

while True:
    #연결을 기다림
    print('waiting..')
    connection, client_address = sock.accept()
    data = connection.recv(5)
    print('received {!r}'.format(data))
    connection.sendall(data)

        
        
'''

"C:/Users/user/AppData/Local/Programs/Python/Python39/python.exe" "c:/Users/user/Desktop/MInsung/network/server.py"

'''
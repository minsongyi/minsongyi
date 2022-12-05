# echo_client.py

import socket




while True :
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    sock.connect(server_address)
    print('input')
    
    a= input()
    print('done')
    # message = ' '.join(format(ord(x), 'b') for x in "hello") # It is very long but will only be transmitted in chunks of 16 at a time'
    # message.replace(" ", "")
    # message = '0b' + message
    # res = ''.join(format(ord(i), '08b') for i in message)
    # print(bin(res))
    # b = bytes('HEllo', 'utf-8')
    my_str = "hello world"
    my_str_as_bytes = str.encode(my_str)
    sock.sendall(my_str_as_bytes)

    data = sock.recv(5)
    print('received {!r}'.format(data))
    sock.close()
    

'''

"C:/Users/user/AppData/Local/Programs/Python/Python39/python.exe" "c:/Users/user/Desktop/MInsung/network/client.py"

'''
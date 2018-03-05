import socket

SERVER = "127.0.0.1"
PORT = 8080



while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))

    out_data='''DELETE /chat_room/test HTTP/1.1
Host: 59.151.215.29:8080
Accept: /
User-Agent: KakaoTalk/Bot 2.0
Via: 1.1 ghost377 (squid/3.1.23)
X-Forwarded-For: unknown
Cache-Control: max-age=259200
Connection: keep-alive

'''
    out_data+=input()
    client.sendall(bytes( out_data, 'UTF-8'))
    if out_data == 'bye':
        break
    in_data = client.recv(1024)
    print("From Server :\n", in_data.decode())
    client.close()

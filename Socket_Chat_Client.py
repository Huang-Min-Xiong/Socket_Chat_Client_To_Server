import socket  

while True:
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #建立Socket
    Host_IP='127.0.0.1' #主機IP
    Host_Port=12345 #主機Port
    Socket.connect((Host_IP,Host_Port)) #連接Server
    message=input('請輸入訊息:')
    Socket.send(message.encode()) #訊息加碼
    print("我說:",Socket.recv(1024).decode()+'\n') #數據解碼
    
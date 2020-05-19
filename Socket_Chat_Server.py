import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #建立Socket
Host_IP='127.0.0.1' #主機IP
Host_Port=12345 #主機Port
sock.bind((Host_IP,Host_Port)) #綁定IP與Port
sock.listen(5) #監聽

while True:  
    try :
        Connect,Address = sock.accept() #當找到連接時接受連接
        Data = Connect.recv(1024) #接收數據
        print('Client說:'+Data.decode()) #數據解碼
        Connect.send(Data) #傳送數據  
        Connect.close()
    except:
        print('Client已結束連線,嘗試連接中...')
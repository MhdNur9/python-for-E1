import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
Last_Modified=''
ETag=''
Content_Length=''
Cache_Control=''
Content_Type=''
all_data=''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    file1=data.decode()
    for lin in file1:
        all_data=all_data+lin


mysock.close()


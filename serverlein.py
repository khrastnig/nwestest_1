#!/usr/bin/env python3

#Phyton Server Lein Programm

# serverlein program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces // alle vorhandenen ip-adressen
PORT = 8080              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #wird s zugeordnet
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))    #Bindet HOST und PORT //"Adresse mit mehreren Türen"
    s.listen(1)   # hört ob daten kommen
    while True:   # client loop
        conn, addr = s.accept() #conn wird socket von client und addr die IP Adresse von client
        with conn:
            print('Connected by', addr)
            count=0
            data = conn.recv(1024)  #Daten vom Client werden empfangen (zahl) gibt die menge der bytes an
                    
            if not data: break      #Wenn keine Daten dann bricht er ab
            outdata ="HTTP/1.1 200 OK\r\n\r\n<html><body><h1>Hi BULME "+str(addr)+"</h1></body></html>"
            answer=outdata.encode()   #UTF-8
            print(answer)
            conn.sendall(answer)   #conn.sendall(data) -> conn.sendall(outdata)   alles wird geschickt
                                        #bis der Inhalt plus alle paketdaten gesendet sind. die Paketgrösse ist
                                    #genormt. ist ein paket größer, wird
            conn.close()            # beendet




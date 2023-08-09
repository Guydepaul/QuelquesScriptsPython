#coding:utf-8

import http.server
import socketserver #qui permet la communication de deux reséaux(source de communication et source de destination)

port = 80 #par defaut pour le port http
adress = ("", port) #comme c'est en local pas besoin de mettre le localhost

#on met en place une gestion qui va gerer les requettes http

handler = http.server.SimpleHTTPRequestHandler #pour mettre le gestionnaire de requette stardar
httpd = socketserver.TCPServer(adress, handler)

print(f"server demarré sur le port {port}")

httpd.serve_forever()
#coding:utf-8

import http.server

port = 80 #par defaut pour le port http
adress = ("", port) #comme c'est en local pas besoin de mettre le localhost

server = http.server.HTTPServer #ici on demarre le server


handler = http.server.CGIHTTPRequestHandler #un gestionnaire pour le http,mais foctionnel pour le script cgi
handler.cgi_directories = ["/"] #là ou il va execute les script on le met par defaut sur le meme ficheir

httpd = server(adress, handler) #ici on crée le server

print(f"server demarre sur le port {port}")

httpd.serve_forever()


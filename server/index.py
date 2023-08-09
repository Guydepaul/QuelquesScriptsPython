#coding:utf-8
import cgi

#on va commence par le donne une entete pour lui precisse le forme de script qu'il va executer
print("content-type: text/html; charset=utf-8\n") #ici on definit l'entete pour lui dire qu'on va seulement utiliser l'affichage html sous forme de script

html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page web</title>
</head>
<body>
    <h1>Bonjour !</h1>
    <p>bla bla bla</p>
</body>
</html>
"""
print(html)
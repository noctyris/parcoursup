#! C:\laragon\bin\python\python-3.6.1\python.exe
# -*- coding: UTF-8 -*-

from datetime import date

import cgi, cgitb
cgitb.enable()

# Ces 3 lignes semblent indispensables pour que les lettres accentuées
# soient prises en compte
today = date.today()

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
###################################################################
# CODE HTML
print ("Content-type:text/html\r\n\r\n")
print('<!DOCTYPE html>')
print ('<html>')
print ('<head>')
print ('<title>Exemple</title>')
print ('''
      <meta charset="utf-8">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css" />
''')

print ('</head>')
print ('<body>')

#ici débute le contenu <body>
print('<div class="container"><h1 class="alert alert-success"> Hello World ! Apache Web + Python </h1></div>')

#ici débute le contenu modifiable

formulaire = cgi.FieldStorage()
nom, prenom, email, souhait, precisions, ddn = formulaire.getvalue('nom'),formulaire.getvalue('prenom'),formulaire.getvalue('email'),formulaire.getvalue('souhait'),formulaire.getvalue('precisions'),formulaire.getvalue('ddn').split("-")

print('<table class="display">')
print(f'<tr><td id="label">Nom</td><td id="info">{nom}</td></tr>')
print(f'<tr><td id="label">Prenom</td><td id="info">{prenom}</td></tr>')
print(f'<tr><td id="label">Email</td><td id="info">{email}</td></tr>')
print(f'<tr><td id="label">Souhait</td><td id="info">{"Être" if souhait=="autre" else "" + souhait}</td></tr>')
print(f'<tr><td id="label">Precisions</td><td id="info">{precisions}</td></tr>' if souhait=="autre" else "")
print(f'<tr><td id="label">Date de naissance</td><td id="info">{"/".join(ddn[::-1])}</td></tr>')
print(f'<tr><td id="label">Âge</td><td id="info">{str(today.year - int(ddn[0]) - ((today.month, today.day) < (int(ddn[1]), int(ddn[2]))))}</td id="info"></tr>')
print('</table>')

#fin de la page

print ('</body>')
print ('</html>')

#Reto semanal 17
# /*
#  * ¡Estoy de celebración! He publicado mi primer libro:
#  * "Git y GitHub desde cero"
#  * - Papel: mouredev.com/libro-git
#  * - eBook: mouredev.com/ebook-git
#  *
#  * ¿Sabías que puedes leer información de Git y GitHub desde la gran
#  * mayoría de lenguajes de programación?
#  *
#  * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
#  * - Hash
#  * - Autor
#  * - Mensaje
#  * - Fecha y hora
#  *
#  * Ejemplo de salida:
#  * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.
#  *
#  */


import requests
import json

url = 'https://api.github.com/repos/mouredev/retos-programacion-2023/commits'
response = requests.get(url)
commits = json.loads(response.text)

variable = 0
for commit in commits[:10]:

    variable+= 1
    hash = commit['sha']
    author = commit['commit']['author']['name']
    message = commit['commit']['message']
    message = message.replace("\n", " ")
    date = commit['commit']['author']['date']

    print(f'Commit {variable} | {hash} | {author} | {message} | {date}')


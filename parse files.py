
import os
import unicodedata
import json 

path = "./files_salud"
dir_list = os.listdir(path)

lista = {}
lista['files'] = []
for elem in dir_list:
    contenido = {}
    contenido['name'] = elem
    contenido['dir'] = './files_salud/'+elem
    lista['files'].append(contenido)

# jsLista = json.dumps(lista, ).encode('utf8')
with open("files_salud.json", "w", encoding='utf8') as outfile:
    json.dump(lista, outfile, ensure_ascii=False)
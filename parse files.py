
import os
import unicodedata
import json 

path = "./files"
dir_list = os.listdir(path)

lista = {}
lista['files'] = []
for elem in dir_list:
    contenido = {}
    contenido['name'] = elem
    contenido['dir'] = './files/'+elem
    lista['files'].append(contenido)

# jsLista = json.dumps(lista, ).encode('utf8')
with open("files.json", "w", encoding='utf8') as outfile:
    json.dump(lista, outfile, ensure_ascii=False)
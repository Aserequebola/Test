
import os
import unicodedata
import json 
import re

path = "./files_slud_2"
dir_list = os.listdir(path)

lista = {}
lista['files'] = []
for elem in dir_list:
    contenido = {}
    val = re.findall("\d+.", elem)[0]
    nombre = elem
    if len(val) == 2:
        nombre = elem.replace(val, '00'+val)
    elif len(val) == 3:
        nombre = elem.replace(val, '0'+val)

    contenido['name'] = nombre.replace('Tabla', 'Cuadro')
    contenido['dir'] = './files_slud_2/'+elem
    lista['files'].append(contenido)

# jsLista = json.dumps(lista, ).encode('utf8')
with open("files_salud.json", "w", encoding='utf8') as outfile:
    json.dump(lista, outfile, ensure_ascii=False)
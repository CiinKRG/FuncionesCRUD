##Script para la función CREATE
##Se creará un documento
import requests
import json
import urllib
import os, sys
from pprint import pprint
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch.serializer import JSONSerializer


#Se pedirá el index al cual se debe de enviar, de no ser encontrado se creará
print("Host:")
host=input()
print("Port:")
puerto=input()
print("Index name:")
name_index=input()
print("Doc type:")
type_document=input()

ES_HOST = {"host": host, "port":puerto}
es = Elasticsearch(hosts=[ES_HOST])

#Se pedirá el directorio y nombre del archivo
print("Ubicación y nombre del archivo (/home/user/folder1/file.json):")
directory='/home/cynthia/Documentos/files/prueba2.json'
#directory=input()

with open(directory, 'r', encoding='utf-8') as f:
    data=json.loads(f.read())
pprint(data)

es.index(index=name_index, doc_type=type_document, body=data)

#Script para la función READ
#Se leerá un index
import requests
import json
import urllib
import os, sys
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch.serializer import JSONSerializer

print("Host:")
host=input()
print("Port:")
puerto=input()

ES_HOST = {"host": host, "port":puerto}
es = Elasticsearch(hosts=[ES_HOST])

#Se pedirá el index que se va a leer y el doc_type
print("Index name:")
name_index=input()
print("Doc type:")
tipo=input()
print("ID:")
identificador=input()

if es.indices.exists(index=name_index):
    resp=es.get(index=name_index, doc_type=tipo, id=identificador)
    print(resp)
else:
    print("El index " + name_index + " no existe")

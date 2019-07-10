#Script para la función UPDATE
#Se actualizará un documento
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

print("Index name:")
name_index=input()
print("Doc type:")
tipo=input()
print("ID:")
identificador=input()

print("Data a actualizar:")
print('Ejemplo: {"name":dato}')
data_new=input()
#data_new={"usuario":"desconocido"}

if es.indices.exists(index=name_index):
    resp= es.get(index=name_index, doc_type=tipo, id=identificador)
    print(resp)
    resp= es.index(index=name_index, doc_type=tipo, id=identificador, body=data_new)
    resp_get= es.get(index=name_index, doc_type=tipo, id=identificador)
    print(resp_get)
else:
    print("El index " + name_index + " no existe")

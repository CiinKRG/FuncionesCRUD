#Script para la función DELETE
#Se borrará un documento
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

#Se pedirá el id que se va a borrar
print("Index name:")
name_index=input()

print("Doc type:")
tipo=input()
print("ID:")
identificador=input()


if es.indices.exists(index=name_index):
    resp = es.delete(index=name_index, doc_type=tipo, id=identificador)
    print(resp)
    print("Se borro el documento con id: " + identificador)
else:
    print("El index " + name_index + " no existe")

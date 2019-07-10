#Script para la función DELETE
#Se borrará un index
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

#Se pedirá el index que se va a borrar
print("Index name:")
name_index=input()


if es.indices.exists(index=name_index):
    resp = es.indices.delete(index=name_index)
    print(resp)
    print("Se borro el index: " + name_index)
else:
    print("El index " + name_index + " no existe")

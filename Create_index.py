##Script para la función CREATE
##Se creará un índice en Elasticsearch
from elasticsearch import Elasticsearch

#Pedir host y port
print("Host:")
host=input()
print("Port:")
puerto=input()
ES_HOST = {"host": host, "port":puerto}
es = Elasticsearch(hosts=[ES_HOST])

#Pedir nombre del index
print("Index name:")
name_index=input()
INDEX_NAME=name_index
response=es.indices.create(index=INDEX_NAME)

print(response)

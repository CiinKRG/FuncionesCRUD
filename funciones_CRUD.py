from elasticsearch import Elasticsearch
import requests
import json
import urllib
import os, sys
from pprint import pprint
from elasticsearch import helpers
from elasticsearch.serializer import JSONSerializer

#----------------------------------------------------------------------
def create_index(HOST,puerto,index_name):

    ES_HOST = {"host": HOST, "port":puerto}
    es = Elasticsearch(hosts=[ES_HOST])

    resp=es.indices.create(index=index_name)
    print(resp)

#----------------------------------------------------------------------
def create_document(HOST,puerto,index_name,type_document):

    ES_HOST = {"host": HOST, "port":puerto}
    es = Elasticsearch(hosts=[ES_HOST])

    print("Ubicación y nombre del archivo (/home/user/folder1/file.json):")
    directory=input()

    with open(directory, 'r', encoding='utf-8') as f:
        data=json.loads(f.read())
    pprint(data)

    es.index(index=index_name, doc_type=type_document, body=data)

#---------------------------------------------------------------------
def read_index(HOST,puerto,index_name):

    ES_HOST = {"host": HOST, "port":puerto}
    es = Elasticsearch(hosts=[ES_HOST])

    if es.indices.exists(index=index_name):
        resp = es.search(index=index_name,filter_path=['hits.hits._id', 'hits.hits._type', 'hits.hits._source'])
        print(resp)
    else:
        print("El index " + index_name + " no existe")

#-------------------------------------------------------------------
def read_document(HOST,puerto,index_name,type_document,identificador):

    ES_HOST = {"host": HOST, "port":puerto}
    es = Elasticsearch(hosts=[ES_HOST])

    if es.indices.exists(index=index_name):
        resp=es.get(index=index_name, doc_type=type_document, id=identificador)
        print(resp)
    else:
        print("El index " + index_name + " no existe")

#----------------------------------------------------------------------
def update_document(HOST,puerto,index_name,type_document,identificador):

    ES_HOST = {"host": HOST, "port":puerto}
    es = Elasticsearch(hosts=[ES_HOST])

    if es.indices.exists(index=index_name):

        print("Data a actualizar")
        i=''
        list_campos=[]
        j=0
        while i != 'n':
            d1=input("Campo a cambiar: ")
            list_campos.append(d1)
            d2=input("contenido del campo: ")
            list_campos.append(d2)
            j=j+2
            i=input("Si desea ingresar más campos presione 0, de lo contrario presione n: ")

        print(list_campos)
        print("Info a actualizarse:")
        resp= es.get(index=index_name, doc_type=type_document, id=identificador)
        print(resp)

        k=0
        while k<j:
            resp= es.update(index=index_name, doc_type=type_document, id=identificador, body={"doc": {list_campos[k]:list_campos[k+1]}})
            k=k+2

        resp_get= es.get(index=index_name, doc_type=type_document, id=identificador)

        print("Info actualizada:")
        print(resp_get)

    else:
        print("El index " + index_name + " no existe")

#--------------------------------------------------------------------
def delete_index(HOST,puerto,index_name):

    ES_HOST = {"host": HOST, "port":puerto}
    es = Elasticsearch(hosts=[ES_HOST])

    if es.indices.exists(index=index_name):
        resp = es.indices.delete(index=index_name)
        print(resp)
        print("Se borro el index: " + index_name)
    else:
        print("El index " + index_name + " no existe")

#-----------------------------------------------------------------
def delete_document(HOST,puerto,index_name,type_document,identificador):

    ES_HOST = {"host": HOST, "port":puerto}
    es = Elasticsearch(hosts=[ES_HOST])

    if es.indices.exists(index=index_name):
        resp = es.delete(index=index_name, doc_type=type_document, id=identificador)
        print(resp)
        print("Se borro el documento con id: " + identificador)
    else:
        print("El id " + identificador + " no existe")

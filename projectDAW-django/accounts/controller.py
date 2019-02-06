import requests, json


def ListarServicio(entidad):
    response = requests.get('http://127.0.0.1:8000/api/' + entidad + '/')
    data = response.json()
    return data


def item_id(entidad, dato):
    response = requests.get('http://127.0.0.1:8000/api/'+entidad+'/'+dato+'/')
    data = response.json()
    return data


def Add(registro):
    response = requests.post('http://127.0.0.1:8000/api/',registro)
    return response


def ListarCita(entidad):
    response = requests.get('http://127.0.0.1:8000/api/'+entidad+'/')
    data = response.json()
    return data



'''
def ElemInd(entidad, dato):
    response = requests.get('http://127.0.0.1:8000/api/v1/'+entidad+'/'+dato+'/')
    data = response.json()
    return data

def Edit(dato, registro):
    response = requests.put('http://127.0.0.1:8000/api/v1/peliculas/'+dato+'/',registro)
    return response

def Delete(dato):
    response = requests.delete('http://127.0.0.1:8000/api/v1/peliculas/'+dato+'/')
    return response
'''



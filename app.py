from metodos import User_presente, Get_userkey

from flask import Flask
from flask import request
import requests
import json



app = Flask(__name__)

raiz_url = 'https://tasks-d8c9c-default-rtdb.firebaseio.com'
f_url = '/.json'







@app.route("/task/list", methods=['GET'])
def Task_List():
    key_user = request.json['key_user']
    
    #veriicando se a chave veio
    if key_user == '':
        return json.dumps({'msg': 'error'})
    
    url = f'{raiz_url}/{key_user}{f_url}'
    response = requests.get(url)
    data = response.json()
    return json.dumps(data)




@app.route("/task/create", methods=['post'])
def Task_Create():
    
    key_user = request.json['key_user']
    title = request.json['title']
    description = request.json['description']
    
    dados = {'title': title, 'description': description}
    url = f'{raiz_url}/{key_user}{f_url}'
    response = requests.post(url, json=dados) 
    
    return json.dumps({'msg': 'Sucess'})


@app.route("/task/update", methods=['patch'])
def Task_Update():
    
    key_user = request.json['key_user']
    key_task = request.json['key_task']
    title = request.json['title']
    description = request.json['description']
    
    
    dados = {'title': title, 'description': description }
    url = f'{raiz_url}/{key_user}/{key_task}{f_url}'
    response = requests.patch(url, json=dados)
    
    return json.dumps({'msg': 'Sucess'})


@app.route("/task/delete", methods=['delete'])
def Task_Delete():
    key_user = request.json['key_user']
    key_task = request.json['key_task']
    
    url = f'{raiz_url}/{key_user}/{key_task}{f_url}'
    response = requests.delete(url)
    
    return json.dumps({'msg': 'Sucess'})




##############################################################

@app.route("/task/auth/create", methods=['POST'])
def User_Create():
    
    
    
    email = request.json['email']
    senha = request.json['senha']
    
    response = requests.get(raiz_url+f_url)
    dic = response.json()
    
    #verifica se o email ja está cadastrado
    if User_presente(dic, email):
        return json.dumps({'msg': 'error'})
    
    dados = {'auth': {'email':email, 'senha':senha}}
    response = requests.post(f'{raiz_url}{f_url}', json=dados)
    print(response.text)
    return json.dumps({'msg': 'sucess'})
    
    



@app.route("/task/auth/connect", methods=['GET'])
def Connect():
    
    #fazer um get no banco
    #depois verificar se o user existe no banco
    # se a senha é igual
    
    email = request.json['email']
    senha = request.json['senha']
    
    response = requests.get(raiz_url+f_url)
    dic = response.json()
    
    chave = Get_userkey(dic, email, senha)
    
    return json.dumps({'key_user': chave})



    

from metodos import User_presente, Get_userkey, Empty_field
from flask import Flask
from flask import request
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

from env import raiz_url
f_url = '/.json'



@app.route("/task/list", methods=['GET', 'POST'])
def Task_List():
    key_user = request.json['key_user']
    
    #veriicando se a chave veio
    if Empty_field(key_user) :
        return json.dumps({'msg': 'error'})  
    
    url = f'{raiz_url}/{key_user}{f_url}'
    response = requests.get(url)
    data = response.json()
    return json.dumps({'msg': 'success', 'dados':data})



@app.route("/task/create", methods=['post'])
def Task_Create():
    
    key_user = request.json['key_user']
    title = request.json['title']
    description = request.json['description']
    
    if Empty_field(key_user, title) :
        return json.dumps({'msg': 'error'})
    
    
    dados = {'title': title, 'description': description}
    url = f'{raiz_url}/{key_user}{f_url}'
    response = requests.post(url, json=dados) 
    
    return json.dumps({'msg': 'sucess'})


@app.route("/task/update", methods=['patch'])
def Task_Update():
    key_user = request.json['key_user']
    key_task = request.json['key_task']
    title = request.json['title']
    description = request.json['description']
    
    if Empty_field(key_user, key_task, title) :
        return json.dumps({'msg': 'error'})
    
    
    dados = {'title': title, 'description': description }
    url = f'{raiz_url}/{key_user}/{key_task}{f_url}'
    response = requests.patch(url, json=dados)
    
    return json.dumps({'msg': 'sucess'})


@app.route("/task/delete", methods=['delete'])
def Task_Delete():
    key_user = request.json['key_user']
    key_task = request.json['key_task']

    print(f"delete\n user: {key_user}\n task: {key_task} ")
    
    if Empty_field(key_user, key_task) :
        return json.dumps({'msg': 'error'})
    
    url = f'{raiz_url}/{key_user}/{key_task}{f_url}'
    response = requests.delete(url)
    
    return json.dumps({'msg': 'success'})




##############################################################

@app.route("/task/auth/create", methods=['POST'])
def User_Create():
    email = request.json['email']
    senha = request.json['senha']
    
    response = requests.get(raiz_url+f_url)
    dic = response.json()
    
    #verifica  se tem campos vazios ou se o email ja está cadastrado
    if Empty_field(email, senha) or User_presente(dic, email):
        return json.dumps({'msg': 'error'})
    
    dados = {'auth': {'email':email, 'senha':senha}}
    response = requests.post(f'{raiz_url}{f_url}', json=dados)
    return json.dumps({'msg': 'success'})
    
    

@app.route("/task/auth/connect", methods=['GET', 'POST'])
def Connect():
    email = request.json['email']
    print(email)
    senha = request.json['senha']
    
    response = requests.get(raiz_url+f_url)
    dic = response.json()
    chave = Get_userkey(dic, email, senha)
    
    #verificando se a chave nao veio
    if chave == '':
        return json.dumps({'msg': 'error'})
    
    
    return json.dumps({'msg': 'success', 'key_user': chave})




if __name__ == '__main__':
    app.run(debug=True)



    

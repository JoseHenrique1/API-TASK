# API TASK

<img src="imagem.png" alt="Exemplo imagem">

> API que gerência um banco de dados, guardando os titulos e descrições das suas atividades.



## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* Você instalou o python e pip.
* Breve conhecimento em Apis.
* Criar o seu projeto no Fire Base.
* Usar o link do seu DataBase.

## 🚀 Instalando API TASK

Para instalar o <nome_do_projeto>, siga estas etapas:

Linux:
```
#criando e ativando o ambiente virtual

python3 -m venv venv
cd venv
cd bin
source activate
cd ..
cd ..

#baixando pacotes 

pip install -r requirements.txt
```

Windows:
```
#criando e ativando o ambiente virtual

py -m venv venv
cd venv
cd Scripts
activate
cd ..
cd ..

#baixando pacotes 

pip install -r requirements.txt

```

## ☕ Usando API TASK

Para usar API TASK, siga estas etapas:

```
flask --app app.py run
```

A API TASK possui seis rotas, em que quatro delas representam o CRUD das tasks e as outras duas fazem parte do processo de autenticação de usuários.


Autenticação

Cadastra um usuário no banco: 
"http://127.0.0.1:5000/task/auth/create" - POST - informe o email e senha

Retorna o key_user: 
"http://127.0.0.1:5000/task/auth/connect" - POST - informe o email e senha


CRUD

Retorna todas as tasks e suas keys: 
"http://127.0.0.1:5000/task/list" - POST - informe o key_user

Cria uma nova tasks: 
"http://127.0.0.1:5000/task/create" - POST - informe o key_user

Edita uma task: 
"http://127.0.0.1:5000/task/update" - PATCH - informe o key_user, key_task, title e description

Exclui uma task: 
"http://127.0.0.1:5000/task/delete" - DELETE - informe o key_user, key_task.




## 🤝 Colaboradores



<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/104796730?v=4" width="100px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>José Henrique</b>
        </sub>
      </a>
    </td>
  </tr>
</table>



## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
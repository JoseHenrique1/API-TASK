"""dic = {
    'kjs45v4jv': {'auth': {'email':'emaillllll', 'senha':'123'}},
    'kas45v4jv': {'auth': {'email':'jose',  'senha':'12jh3'}},
    'kmns45v4jv': {'auth': {'email':'emaillllll',  'senha':'123'}}
}
"""

def Empty_field(*fields):
    for field in fields:
        if field == '':
            return True
    
    return False

def User_presente(dic, email):
    for chave, valor in dic.items():
        if (valor['auth']['email'] == email):
            return True
    return False

def Get_userkey(dic, email, senha):
    if User_presente(dic, email):
        for chave, valor in dic.items():
            if (valor['auth']['email'] == email) and (valor['auth']['senha'] == senha):
                return chave
        
    return ''



#print(get_userkey(dic, 'jose', '123' ))
            
        
    
   
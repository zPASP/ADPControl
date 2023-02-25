import requests

def __trazerEndereco(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    payload = ""
    response = requests.request("GET", url, data=payload)
    return (response.json())

def validarcep(cep):
    if len(str(cep)) < 8 or len(str(cep)) > 8:
        return False
    else:
        endereco = __trazerEndereco(cep)
        if 'erro' in endereco:
            return False
        else:
            return endereco
import requests, sys


# python3 professor-xml.py [ip] [porta]
if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = sys.argv[2]
    url = f"http://{ip}:{port}/chamadasoap?wsdl"
else:
    url = f"http://127.0.0.1:5859/chamadasoap?wsdl"
headers = {'content-type': 'text/xml'}

def mostrarMenu():
    print("1 - Mostrar nome do professor")
    print("2 - Alterar nome do professor")
    print("3 - Alterar nome da disciplina")
    print("4 - Mostrar nome da disciplina")
    print("5 - Mostrar alunos")
    print("0 - Sair")
    opcao = input("Digite a opção desejada: ")
    return opcao

while(True):
    opcao = mostrarMenu()
    if(opcao == '1'):
        try:
            with open("../templates/getProfessor-template.xml", "r") as arquivo:
                payload = arquivo.read()
        except FileNotFoundError:
            print("Arquivo template não encontrado")
            sys.exit()
        resposta = requests.request('POST', url, data=payload, headers=headers)
        print(resposta.text)
    elif(opcao == '2'):
        nome = input("Digite um novo nome para o professor: ")
        try:
            with open("../templates/setProfessor-template.xml", "r") as arquivo:
                payload = arquivo.read().format(nome = nome)
        except FileNotFoundError:
            print("Arquivo template não encontrado")
            sys.exit()
        resposta = requests.request('POST', url, data=payload, headers=headers)
        if(resposta.status_code == 200):
            print("Nome do professor alterado com sucesso")
        else:
            print("Erro ao alterar o nome do professor")
    elif(opcao == '3'):
        nomeDisciplina = input("Digite o nome da disciplina: ")
        try:
            with open("../templates/setDisciplina-template.xml", "r") as arquivo:
                payload = arquivo.read().format(nomeDisciplina = nomeDisciplina)
        except FileNotFoundError:
            print("Arquivo template não encontrado")
            sys.exit()
        resposta = requests.request('POST', url, data=payload, headers=headers)
        if(resposta.status_code == 200):
            print("Nome da disciplina alterado com sucesso")
        else:
            print("Erro ao alterar o nome da disciplina")
    elif(opcao == '4'):
        try:
            with open("../templates/getDisciplina-template.xml", "r") as arquivo:
                payload = arquivo.read()
        except FileNotFoundError:
            print("Arquivo template não encontrado")
            sys.exit()
        resposta = requests.request('POST', url, data=payload, headers=headers)
        if(resposta.status_code == 200):
            print("Nome da disciplina: ", resposta.text)
        else:
            print("Erro ao obter o nome da disciplina")
    else:
        break
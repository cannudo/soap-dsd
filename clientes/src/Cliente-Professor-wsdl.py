import zeep

# python3 professor-xml.py [ip] [porta]
if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = sys.argv[2]
    url = f"http://{ip}:{port}/chamadasoap?wsdl"
else:
    url = f"http://127.0.0.1:5859/chamadasoap?wsdl"

client = zeep.Client(wsdl = url)

def mostrarMenu():
    print("1 - Mostrar nome do professor")
    print("2 - Alterar nome do professor")
    print("3 - Alterar nome da disciplina")
    print("4 - Mostrar nome da disciplina")
    print("5 - Mostrar alunos")
    print("0 - Sair")
    opcao = input("Digite a opção desejada: ")
    return opcao

while client:
    try:
        opcao = mostrarMenu()
        if opcao == '1':
            print(client.service.getProfessor())
        elif opcao == '2':
            nome = input("Digite o nome do professor: ")
            print(client.service.setProfessor(nome))
        elif opcao == '3':
            nomeDisciplina = input("Digite o nome da disciplina: ")
            print(client.service.setDisciplina(nomeDisciplina))
        elif opcao == '4':
            print(client.service.getDisciplina())
        elif opcao == '5':
            print(client.service.getAlunos())
        elif opcao == '0':
            break
    except:
        print("Erro ao executar a operação")

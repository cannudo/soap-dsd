import zeep

url = 'http://10.25.1.14:5859/chamadasoap?wsdl'

client = zeep.Client(wsdl = url)
client.service.getProfessor()

def mostrarMenu():
    print("1 - Mostrar nome do Professor")
    print("2 - Alterar nomde do Professor")
    print("3 - Alterar nome da Disciplina")
    print("4 - Ver nome da Disciplina")
    print("5 - Listar Alunos")
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

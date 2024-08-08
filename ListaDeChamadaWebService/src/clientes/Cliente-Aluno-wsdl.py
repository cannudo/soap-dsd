import zeep

url = 'http://10.25.1.14:5859/chamadasoap?wsdl'

client = zeep.Client(wsdl = url)

matricula = input("Digite a matricula do aluno: ")
nome = input("Digite o nome do aluno: ")

client.service.adicionarAluno(nome, matricula)

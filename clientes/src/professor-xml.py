import requests, sys

# python3 professor-xml.py [ip] [porta]
if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = sys.argv[2]
    url = f"http://{ip}:{port}/chamadasoap?wsdl"
else:
    url = f"http://127.0.0.1:5859/chamadasoap?wsdl"

headers = {'content-type': 'text/xml'}

# tente abrir o arquivo getProfessor-template.xml que está em ../templates/
try:
    with open("../templates/getProfessor-template.xml", "r") as arquivo:
        payload = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
    sys.exit()

requests.request('POST', url, data=payload, headers=headers)
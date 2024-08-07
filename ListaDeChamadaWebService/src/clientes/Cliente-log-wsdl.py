import zeep

url = 'http://10.25.1.14:5859/chamadasoap?wsdl'

client = zeep.Client(wsdl = url)
resposta = client.service.toString()
print(resposta)

with open('log.txt', 'w') as arquivo:
    arquivo.write(resposta)
    arquivo.close()
    

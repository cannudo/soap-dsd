package listadechamadawebservice;

import listadechamadawebservice.ListaDeChamadaWebService;
import javax.xml.ws.Endpoint;

public class PublicadorListaDeChamadaWebService {
    public static void main(String[] args) {
        Endpoint.publish("http://10.25.1.14:5859/chamadasoap", new ListaDeChamadaWebService("Gracon dos Prazos Impossíveis Lima", "Desenvolvimento de Sistemas Distríbuídos", "08/08/2024"));
        System.out.println("[✅ servidor em execução]");
    }
}

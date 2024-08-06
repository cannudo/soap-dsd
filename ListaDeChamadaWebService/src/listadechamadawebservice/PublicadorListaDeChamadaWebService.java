package listadechamadawebservice;

import listadechamadawebservice.ListaDeChamadaWebService;
import javax.xml.ws.Endpoint;

public class PublicadorListaDeChamadaWebService {
    public static void main(String[] args) {
        Endpoint.publish("http://127.0.0.1:5859/chamadasoap", new ListaDeChamadaWebService("Gracon Lima", "Desenvolvimento de Sistemas Distríbuídos", "05/08/2024"));
        System.out.println("[✅ servidor em execução]");
    }
}

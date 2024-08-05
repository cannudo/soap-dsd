package listadechamadawebservice;

import javax.jws.WebService;

@WebService(endpointInterface = "listadechamadawebservice.InterfaceListaDeChamadaWebService")
public class ListaDeChamadaWebService implements InterfaceListaDeChamadaWebService {
    public void adicionarAluno(String matricula, String nome) {
        System.out.println("Nome: " + nome + "\nMatrícula: " + matricula);
        System.out.println("DEBUG");
    }
}

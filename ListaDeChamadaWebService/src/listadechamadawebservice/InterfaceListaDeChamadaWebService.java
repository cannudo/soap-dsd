package listadechamadawebservice;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;

@WebService
@SOAPBinding(style = SOAPBinding.Style.RPC)
public interface InterfaceListaDeChamadaWebService {
    @WebMethod void adicionarAluno(String matricula, String nome);
    
}

package listadechamadawebservice;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;

@WebService
@SOAPBinding(style = SOAPBinding.Style.RPC)
public interface InterfaceListaDeChamadaWebService {
    @WebMethod String getProfessor();
    @WebMethod void setProfessor(String professor);
    @WebMethod String getDisciplina();
    @WebMethod void setDisciplina(String disciplina);
    @WebMethod String getData();
    @WebMethod void setData(String data);
    @WebMethod String getAlunos();
    @WebMethod int getQuantidadeDeAlunos();
    @WebMethod void setQuantidadeDeAlunos(int quantidadeDeAlunos);
    @WebMethod void adicionarAluno(String matricula, String nome);
    @WebMethod String toString();
}

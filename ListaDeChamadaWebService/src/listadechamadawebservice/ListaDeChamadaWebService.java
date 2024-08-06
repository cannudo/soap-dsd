package listadechamadawebservice;

import javax.jws.WebService;

@WebService(endpointInterface = "listadechamadawebservice.InterfaceListaDeChamadaWebService")
public class ListaDeChamadaWebService implements InterfaceListaDeChamadaWebService {
    private String professor;
    private String disciplina;
    private String data;
    private Aluno[] alunos;
    private int quantidadeDeAlunos;
    
    public ListaDeChamadaWebService(String professor, String disciplina, String data) {
        this.professor = professor;
        this.disciplina = disciplina;
        this.data = data;
        this.quantidadeDeAlunos = 0;
        this.alunos = new Aluno[35];
    }
    
    public void adicionarAluno(String matricula, String nome) {
        System.out.println("Nome: " + nome + "\nMatrícula: " + matricula);
    }
}

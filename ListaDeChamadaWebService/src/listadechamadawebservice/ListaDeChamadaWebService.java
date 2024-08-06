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

    public String getProfessor() {
        return professor;
    }

    public void setProfessor(String professor) {
        this.professor = professor;
    }

    public String getDisciplina() {
        return disciplina;
    }

    public void setDisciplina(String disciplina) {
        this.disciplina = disciplina;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public Aluno[] getAlunos() {
        return alunos;
    }

    public void setAlunos(Aluno[] alunos) {
        this.alunos = alunos;
    }

    public int getQuantidadeDeAlunos() {
        return quantidadeDeAlunos;
    }

    public void setQuantidadeDeAlunos(int quantidadeDeAlunos) {
        this.quantidadeDeAlunos = quantidadeDeAlunos;
    }
    
    public void adicionarAluno(String matricula, String nome) {
        this.alunos[this.quantidadeDeAlunos] = new Aluno(matricula, nome);
        this.quantidadeDeAlunos++;
    }
    
    public String toString() {
        String lista = "Lista de Chamada\n";
        lista += "Professor: " + this.professor + "\n";
        lista += "Disciplina: " + this.disciplina + "\n";
        lista += "Data: " + this.data + "\n";
        lista += "Alunos:\n";
        for (int i = 0; i < this.quantidadeDeAlunos; i++) {
            lista += this.alunos[i].getMatricula() + " - " + this.alunos[i].getNome() + "\n";
        }
        lista+= "\n";
        return lista;
    }


}

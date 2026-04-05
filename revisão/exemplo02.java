package revisão;

class Cliente {
    private String nome;
    private String cpf;
    private double limite;
    private Cliente socio;

    public Cliente(String nome, String cpf, double limite) {
        this.nome = nome;
        this.cpf = cpf;
        this.limite = limite;
        this.socio = null;
    }

    public void setSocio(Cliente c) {
        this.socio = c;
        c.socio = this;
    }

    public double getLimite() {
        if (this.socio == null) {
            return this.limite;
        }
        return this.limite + this.socio.limite;
    }

    @Override
    public String toString() {
        if (this.socio == null) {
            return this.nome + " " + this.cpf;
        }
        return this.nome + " " + this.cpf + " " + this.socio.nome;
    }
}

public class exemplo02 {
    public static void main(String[] args) {
        Cliente a = new Cliente("Gilbert", "1234", 1000);
        Cliente b = new Cliente("Eduardo", "4321", 500);
        Cliente c = new Cliente("Jorgiano", "8888", 5000);
        a.setSocio(b);
        System.out.println(a.getLimite());
        System.out.println(b.getLimite());
        System.out.println(c.getLimite());
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        a.setSocio(c);
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}
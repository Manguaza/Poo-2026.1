package aula_03;
class ContaBancaria { 
   public String titular = "";
   public String numero = "";
   public double saldo = 0;
   public void depositar (double v) { 
        this.saldo += v;

   }
   public void sacar (double v) {
        this.saldo -= v;
   }
}
      


public class listapoo01_ex03 {
  static void main (String[] args) {
    ContaBancaria x = new ContaBancaria ();
    x.titular = "Eduardo";
    x.numero = "123";
    System.out.println(x.saldo);
    x.depositar (100);
    System.out.println (x.saldo);
    x.sacar(20);
    System.out.println(x.saldo);
  }
}

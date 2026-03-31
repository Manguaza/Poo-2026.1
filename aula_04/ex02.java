package aula_04;

class viagem {
 private double distancia = 0;
 private double horas = 0;
 private double minutos = 0;
 public void setDistancia(double distancia) {
     this.distancia = distancia;
 }
    public void setHoras(double horas) {
     this.horas = horas;
    
 }
 public void setMinutos(double minutos) {
     this.minutos = minutos;
 }
    public double getDistancia() {
        return distancia;
    }
    public double getTempo() {
        return horas;
 }
  public double getMinutos () {
     return minutos;
  }
  
  public double calcularVelocidadeMedia () {
   double tempoTotalHoras = horas + (minutos/60.00);
   return tempoTotalHoras / distancia;
  }
 }
public class ex02 {
    public static void main(String[] args) {
        viagem v = new viagem();
        v.setDistancia(150);
        v.setHoras(3);
        v.setMinutos(55);
        
        double velocidade = v.calcularVelocidadeMedia();
        
        System.out.println("Distancia: " + v.getDistancia());
        System.out.println("Tempo gasto: " + v.getTempo() + v.getMinutos());
        System.out.println("Velocidade média: " + velocidade);
    }
}

package aula_04;

class viagem {
 private double distancia = 0;
 private double horas = 0;
 private double minutos = 0;
 public void SetDistancia(double distancia) {
     this.distancia = distancia;
 }
    public void setTempo(double tempo) {
   this.tempo = tempo;
    
 }
 public void setminutos(double minutos) {
   this.minutos = minutos;
 }
    public double getDistancia() {
        return distancia;
    }
    public double getTempo() {
        return tempo;
 }
  public double getMinutos () {
     return minutos;
  }
  
  public double calcularVelocidadeMedia () {
   double tempoTotalHoras = horas + (minutos/60.00);
  }
   return tempoTotalHoras / distancia;
 }
public class ex02 {
    public static void main(String[] args) {
        viagem.setdistancia (150);
        viagem.sethoras (3);
        viagem.setminutos (55);
    }
    double velocidade = calcularVelocidadeMedia;

    System.out.println("distancia " + getDistancia);
    System.out.println("Tempogasto" + getTempo);
    System.out.println("velocidade" + velocidade);
}

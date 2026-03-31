package aula_04;

class Triangulo {
    private double b = 0;
    private double h = 0;
    public void setbase (double v) {
        if (v >= 0) this.b = v;
        else throw new IllegalArgumentException("valor não pode ser negativo");
    }
    public void setAltura(double v) {
        if (v >= 0) this.h = v;
        else throw new IllegalArgumentExpection("valor não pode ser negativo");
    }    
    public double getbase(){
        return this.b;
    }
    public double calcArea(){
        return this.b * this.h / 2
    }
}



public class ex01 {
    public static void main(String[] args) {
        Triangulo x =  new Triangulo();
        x.setbase(10);
        x.setAltura(20);
        System.out.println(x.calcArea());
    }
}

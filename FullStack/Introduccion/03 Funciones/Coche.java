package ejerciciotema32;
/* 
Segunda parte:
	Crear una clase coche.
	Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
	Una función que incremente el número de puertas que tiene el coche.
	Crear un objeto miCoche en el main y añadirle una puerta.
	Mostrar el número de puertas que tiene el objeto.
  */
public class Coche {
	private int puertas;
	
	public Coche(int puertas) {
		this.puertas = puertas;
	}
	
	public void incrementaPuertas(int puertas) {
		this.puertas += puertas;
	}
	
	public void imprimepuertas() {
		System.out.println("Cantidad de pueratas : " + puertas);
	}
	
	public static void main(String[] args) {
		Coche miCoche = new Coche(2);
		miCoche.incrementaPuertas(3);
		miCoche.imprimepuertas();
	}
}

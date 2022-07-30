package ejerciciotema3;
/* 
Primera parte:
	Crear una función con tres parámetros que sean números que se suman entre sí.
	Llamar a la función en el main y darle valores.
      */
public class Funcion {
	
	public static void main(String[] args) {
		int resultado = Suma(2,4,6);
		System.out.println(resultado);
	}

	private static int Suma(int i, int j, int k) {
		int sumatoria = i + j + k;
		return sumatoria;
	}
}

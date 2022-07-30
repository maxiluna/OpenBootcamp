package ejerciciotema4;

public class Estructuras {
	public static void main(String[] args) {
		/* 	Usando un if, crear una condici�n que compare si la 
		variable numeroIf es positivo, negativo, o 0. */
		System.out.println("- 1 -");
		int numeroIf=3;
		if (numeroIf==0) {
			System.out.println("La variable numeroIf es igual a :" + numeroIf);
		} else if (numeroIf>0) {
			System.out.println("La variable numeroIf es positiva : " + numeroIf);
		} else {
			System.out.println("La variable numeroIf es negativa: " + numeroIf);
		}
		
		/*	Crea un bucle While, este bucle tendr� que tener como 
		condici�n que la variable numeroWhile sea inferior a 3, 
		el bloque de c�digo que tendr� el bucle deber�:
			Incrementar el valor de la variable en uno cada vez que se ejecute.
			Mostrarlo por pantalla cada vez que se ejecute. */
		System.out.println("- 2 -");
		int numeroWhile=0;
		while(numeroWhile<3) {
			System.out.println("Variable numeroWhile = " + numeroWhile);
			numeroWhile+=1;
		}
		
		/* 	Para el bucle Do While, 
		deber�s crear la misma estructura que en el While, 
		pero solo se debe ejecutar una vez.*/
		System.out.println("- 3 -");
		do {
			System.out.println("Do While Ejecuta = " + numeroWhile);
			numeroWhile+=1;
		} while(numeroWhile<3);
		
		/*	Para el bucle For, 
		crea una variable numeroFor, esta variable tendr� como 
		valor 0 y su condici�n ser� que la variable sea igual o 
		menor que 3, se ir� incrementando en 1 su valor cada vez 
		que se ejecute y deber� mostrarse por pantalla.*/
		System.out.println("- 4 -");
		int numeroFor;
		for(numeroFor=0; numeroFor<=3; numeroFor++) {
			System.out.println("For - Valor de numeroFor = " + numeroFor);
		}
		
		/*	Para el Switch, deber�s crear la variable estacion, y 
		distintos case para las cuatro estaciones del a�o. 
		Dependiendo del valor de la variable estacion se deber� 
		mandar un mensaje por consola informando de la estaci�n 
		en la que est�. Tambi�n habr� que poner un default para 
		cuando el valor de la variable no sea una estaci�n. */
		System.out.println("- 5 -");
		int estacion;
		estacion=2;
		switch(estacion) {
		case 1:
			// Primavera
			System.out.println("La estacion es PRIMAVERA");
			break;
		case 2:
			// Verano
			System.out.println("La estacion es VERANO");
			break;
		case 3:
			// Oto�o
			System.out.println("La estacion es OTO�O");
			break;
		case 4:
			// Invierno
			System.out.println("La estacion es INVIERNO");
			break;
		default:
			System.out.println("No es una estacion");
			break;
		}		
	}
}
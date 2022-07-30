package ejerciciotema4;

public class Estructuras {
	public static void main(String[] args) {
		/* 	Usando un if, crear una condición que compare si la 
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
		
		/*	Crea un bucle While, este bucle tendrá que tener como 
		condición que la variable numeroWhile sea inferior a 3, 
		el bloque de código que tendrá el bucle deberá:
			Incrementar el valor de la variable en uno cada vez que se ejecute.
			Mostrarlo por pantalla cada vez que se ejecute. */
		System.out.println("- 2 -");
		int numeroWhile=0;
		while(numeroWhile<3) {
			System.out.println("Variable numeroWhile = " + numeroWhile);
			numeroWhile+=1;
		}
		
		/* 	Para el bucle Do While, 
		deberás crear la misma estructura que en el While, 
		pero solo se debe ejecutar una vez.*/
		System.out.println("- 3 -");
		do {
			System.out.println("Do While Ejecuta = " + numeroWhile);
			numeroWhile+=1;
		} while(numeroWhile<3);
		
		/*	Para el bucle For, 
		crea una variable numeroFor, esta variable tendrá como 
		valor 0 y su condición será que la variable sea igual o 
		menor que 3, se irá incrementando en 1 su valor cada vez 
		que se ejecute y deberá mostrarse por pantalla.*/
		System.out.println("- 4 -");
		int numeroFor;
		for(numeroFor=0; numeroFor<=3; numeroFor++) {
			System.out.println("For - Valor de numeroFor = " + numeroFor);
		}
		
		/*	Para el Switch, deberás crear la variable estacion, y 
		distintos case para las cuatro estaciones del año. 
		Dependiendo del valor de la variable estacion se deberá 
		mandar un mensaje por consola informando de la estación 
		en la que está. También habrá que poner un default para 
		cuando el valor de la variable no sea una estación. */
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
			// Otoño
			System.out.println("La estacion es OTOÑO");
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
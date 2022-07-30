package ejerciciotema9;

public class Entregable {
	public static void main(String[] args) {
		
		Cliente cliente  = new Cliente();
		cliente.setEdad(40);
		cliente.setTelefono(1131315151);
		cliente.setNombre("Pepe");
		cliente.setCredito(5000);
		System.out.println(cliente.getEdad());
		System.out.println(cliente.getTelefono());
		System.out.println(cliente.getNombre());
		System.out.println(cliente.getCredito());
		
		Trabajador trabajador = new Trabajador();
		trabajador.setEdad(35);
		trabajador.setTelefono(1145457895);
		trabajador.setNombre("Camilo");
		trabajador.setSalario(3000);
		System.out.println(trabajador.getEdad());
		System.out.println(trabajador.getTelefono());
		System.out.println(trabajador.getNombre());
		System.out.println(trabajador.getSalario());
	}
}

class Persona{
	int edad;
	String nombre;
	int telefono;
	
	public Persona() {
		System.out.println("estoy en el constructor de Persona");
	}

	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getTelefono() {
		return telefono;
	}

	public void setTelefono(int telefono) {
		this.telefono = telefono;
	}
	
}

class Cliente extends Persona {
	int credito;
	
	public Cliente() {
		System.out.println("estoy en el constructor de Cliente");
	}
	
	public int getCredito() {
		return credito;
	}

	public void setCredito(int credito) {
		this.credito = credito;
	}
}

class Trabajador extends Persona {
	float salario;
	
	public Trabajador() {
		System.out.println("estoy en el constructor de Trabajador");
	}

	public float getSalario() {
		return salario;
	}

	public void setSalario(float salario) {
		this.salario = salario;
	}
}
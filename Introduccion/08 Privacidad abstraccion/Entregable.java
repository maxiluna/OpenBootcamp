package ejerciciotema8;

public class Entregable {
	public static void main(String[] args) {
		Persona persona1 = new Persona();
		persona1.setEdad(30);
		persona1.setNombre("Carlos");
		persona1.setTelefono(1131514816);
		
		System.out.println(persona1.getEdad());
		System.out.println(persona1.getNombre());
		System.out.println(persona1.getTelefono());
	}
}

class Persona{
	private int edad;
	private String nombre;
	private int telefono;
	
	public int getEdad() {
		return edad;
	}
	public void setEdad(int edad) {
		this.edad = edad;
	}
	public int getTelefono() {
		return telefono;
	}
	public void setTelefono(int telefono) {
		this.telefono = telefono;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
}
package day02;

public class OopTest {
	public static void main(String[] args) {
		Animal ani = new Animal();
		System.out.println(ani.age);
		ani.getOlder();
		System.out.println(ani.age);
	}
}

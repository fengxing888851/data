import java.util.Scanner;

public class Helloworld{
	/* my first program : 
 	 * Hello, world!*/

	public static void main(String[] args){
		Scanner putin=new Scanner(System.in);
		System.out.println("put in your name:");
		String name=putin.next();
		System.out.println("put in your age: ");
		int age=putin.nextInt();
		System.out.println("put in your score: ");
		double score=putin.nextDouble();
		System.out.println("name: "+name);
		System.out.println("age: "+age);
		System.out.println("score: "+score);

	
		int days=48;
		int wek=days/7;
		double weks=days/7;
		int year=(int)(days+weks);
		System.out.println("Hello,world!"); //this is my first program.
		System.out.println(wek);
		System.out.println(weks);
		System.out.println(year);
	}

}



import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day1 {
	public static void main(String args[]) throws FileNotFoundException {
		File f = new File("input.txt");
		Scanner sc = new Scanner(f);
		int[] numbers = new int[(int) f.length()];
		for (int i = 0; sc.hasNextInt(); i++) {
			numbers[i] = sc.nextInt();
		}
		sc.close();
		// Add all pairs of numbers together and print out the result of the
		// multiplication should the addition result in 2020
		int p1 = 0;
		int p2 = 0;
		for (int a : numbers) {
			for (int b : numbers) {
				if (p1 == 0 && a + b == 2020) {
					p1 = a * b;
				}
				for (int c : numbers) {
					if (p2 == 0 && a + b + c == 2020) {
						p2 = a * b * c;
					}
				}
			}
		}
		System.out.println(p1 + " " + p2);
	}
}
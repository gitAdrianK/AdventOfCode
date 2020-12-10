package day_10;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class day10 {

	public static void main(String[] args) throws FileNotFoundException {
		if (solveDay10("test_input.txt") != 35) {
			System.out.println("Failed test_input");
			return;
		}
		if (solveDay10("test_input_2.txt") != 220) {
			System.out.println("Failed test_input_2");
			return;
		}
		System.out.println(solveDay10("input.txt"));
	}

	private static int solveDay10(String input) throws FileNotFoundException {
		int diff1 = 0;
		int diff3 = 1;
		ArrayList<Integer> numbers = new ArrayList<Integer>();
		Scanner sc = new Scanner(new File(input));
		// Charging outlet
		numbers.add(0);
		while (sc.hasNextInt()) {
			numbers.add(sc.nextInt());
		}
		sc.close();
		Collections.sort(numbers);
		for (int i = 0; i < numbers.size() - 1; i++) {
			if (numbers.get(i + 1) - numbers.get(i) == 1) {
				diff1++;
			} else if (numbers.get(i + 1) - numbers.get(i) == 3) {
				diff3++;
			}
		}
		return diff1 * diff3;
	}

}

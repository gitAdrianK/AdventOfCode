package day_10;

import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class AdapterArray {
	public static void main(String[] args) throws FileNotFoundException {
		solveDay10("test_input.txt");
		solveDay10("test_input_2.txt");
		solveDay10("input.txt");
	}

	private static void solveDay10(String input) throws FileNotFoundException {
		List<Integer> numbers = new ArrayList<Integer>();
		Scanner sc = new Scanner(new File(input));
		// Charging outlet
		numbers.add(0);
		while (sc.hasNextInt()) {
			numbers.add(sc.nextInt());
		}
		sc.close();
		// Part 1
		Collections.sort(numbers);
		int diff1 = 0;
		int diff3 = 1;
		for (int i = 0; i < numbers.size() - 1; i++) {
			if (numbers.get(i + 1) - numbers.get(i) == 1) {
				diff1++;
			} else if (numbers.get(i + 1) - numbers.get(i) == 3) {
				diff3++;
			}
		}
		// Part 2
		BigInteger arrange = traverseGraph(numbers);
		System.out.println(input + ", " + diff1 * diff3 + ", " + arrange);
	}
	
	private static BigInteger traverseGraph(List<Integer> arr) {
		ArrayList<BigInteger> cache = new ArrayList<BigInteger>();
		cache.add(BigInteger.valueOf(1));
		for (int i = 1; i < arr.size(); i++) {
			BigInteger sum = BigInteger.valueOf(0);
			for (int j = 1; j <= 3; j++) {
				// Out of bounds protection
				if (i - j < 0) {
					continue;
				}
				if (arr.get(i) - arr.get(i - j) <= 3) {
					sum = sum.add(cache.get(i - j));
				}
			}
			cache.add(sum);
		}
		return cache.get(cache.size() - 1);
	}
}

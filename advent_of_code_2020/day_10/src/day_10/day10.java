package day_10;

import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class day10 {

	public static void main(String[] args) throws FileNotFoundException {
		solveDay10("test_input.txt");
		solveDay10("test_input_2.txt");
		solveDay10("input.txt");
	}

	private static void solveDay10(String input) throws FileNotFoundException {
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
		// Part 1
		Collections.sort(numbers);
		for (int i = 0; i < numbers.size() - 1; i++) {
			if (numbers.get(i + 1) - numbers.get(i) == 1) {
				diff1++;
			} else if (numbers.get(i + 1) - numbers.get(i) == 3) {
				diff3++;
			}
		}
		BigInteger arrange = traverseGraph(0, numbers, new HashMap<Integer, BigInteger>());
		System.out.println(input + ", " + diff1 * diff3 + ", " + arrange);
	}

	private static BigInteger traverseGraph(int start, ArrayList<Integer> graph, HashMap<Integer, BigInteger> cache) {
		if (cache.containsKey(start)) {
			return cache.get(start);
		}
		BigInteger sum = BigInteger.valueOf(0);
		if (start == graph.size() - 1) {
			return BigInteger.valueOf(1);
		}
		for (int i = 1; i <= 3; i++) {
			if (start + i > graph.size() - 1) {
				break;
			}
			if (graph.get(start + i) - graph.get(start) > 3) {
				break;
			}
			sum = sum.add(traverseGraph(start + i, graph, cache));
		}
		cache.put(start, sum);
		return sum;
	}

}
package day_13;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class day13 {
	public static void main(String[] args) throws FileNotFoundException {
		solveDay13("test_input.txt");
		solveDay13("input.txt");
	}

	private static void solveDay13(String input) throws FileNotFoundException {
		List<Integer> numbers = new ArrayList<Integer>();
		Scanner sc = new Scanner(new File(input));
		int arrival = sc.nextInt();
		for (String interval : sc.next().split(",")) {
			if (interval.equals("x")) {
				continue;
			} else {
				numbers.add(Integer.parseInt(interval));
			}
		}
		sc.close();
		int nextBusID = 0;
		int closestNextBus = Integer.MAX_VALUE;
		for (int bus : numbers) {
			int nextBusIn = ((int) Math.ceil(((double)arrival / (double)bus)) * bus) - arrival;
			if (nextBusIn < closestNextBus) {
				nextBusID = bus;
				closestNextBus = nextBusIn;
			}
		}
		System.out.println(nextBusID * closestNextBus);
	}
}

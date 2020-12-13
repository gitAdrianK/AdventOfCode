package day_13;

import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class day13 {
	public static void main(String[] args) throws FileNotFoundException {
		solveDay13("test_input.txt", true, true);
		solveDay13("test_input_2.txt", false, true);
		solveDay13("test_input_3.txt", false, true);
		solveDay13("test_input_4.txt", false, true);
		solveDay13("test_input_5.txt", false, true);
		solveDay13("input.txt", true, true);
	}

	private static void solveDay13(String input, boolean p1, boolean p2) throws FileNotFoundException {
		Scanner sc = new Scanner(new File(input));
		int arrival = sc.nextInt();
		ArrayList<Integer> numbers = new ArrayList<Integer>();
		ArrayList<Integer> remainders = new ArrayList<Integer>();
		int offset = 0;
		for (String s : sc.next().split(",")) {
			if (s.equals("x")) {
				offset++;
			} else {
				int n = Integer.parseInt(s);
				numbers.add(n);
				remainders.add((n - offset) % n);
				offset++;
			}
		}
		sc.close();
		if (p1) {
			System.out.println(input + " p1: " + solvePart1(arrival, numbers));
		}
		if (p2) {
			System.out.println(input + " p2: " + solvePart2(numbers, remainders));
		}
	}
	
	private static int solvePart1(int arrival, List<Integer> numbers) {
		// ID of the bus that arrives next
		int nextBusID = 0;
		// Time until next bus
		int closestNextBus = Integer.MAX_VALUE;
		for (int bus : numbers) {
			int nextBusIn = bus - (arrival % bus);
			if (nextBusIn < closestNextBus) {
				nextBusID = bus;
				closestNextBus = nextBusIn;
			}
		}
		return nextBusID * closestNextBus;
	}

	private static BigInteger solvePart2(List<Integer> numbers, List<Integer> remainders) {
		// Chinese remainder theorem
		BigInteger[] n = new BigInteger[numbers.size()];
		BigInteger[] a = new BigInteger[remainders.size()];
		for (int i = 0; i < numbers.size(); i++) {
			n[i] = BigInteger.valueOf(numbers.get(i));
			a[i] = BigInteger.valueOf(remainders.get(i));
		}
		return (chineseRemainder(n, a));
	}

	public static BigInteger chineseRemainder(BigInteger[] n, BigInteger[] a) {
		BigInteger prod = BigInteger.ONE;
		for (BigInteger b : n) {
			prod = prod.multiply(b);
		}
		BigInteger p, sm = BigInteger.ZERO;
		for (int i = 0; i < n.length; i++) {
			p = prod.divide(n[i]);
			sm = sm.add(a[i].multiply(mulInv(p, n[i]).multiply(p)));
		}
		return sm.mod(prod);
	}

	private static BigInteger mulInv(BigInteger a, BigInteger b) {
		BigInteger b0 = b;
		BigInteger x0 = BigInteger.ZERO;
		BigInteger x1 = BigInteger.ONE;
		if (b == BigInteger.ONE)
			return BigInteger.ONE;
		while (a.compareTo(BigInteger.ONE) > 0) {
			BigInteger q = a.divide(b);
			BigInteger amb = a.mod(b);
			a = b;
			b = amb;
			BigInteger xqx = x1.subtract(q.multiply(x0));
			x1 = x0;
			x0 = xqx;
		}
		if (x1.compareTo(BigInteger.ZERO) < 0)
			x1 = x1.add(b0);
		return x1;
	}
}

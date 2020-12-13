package day_13;

import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class day13 {
	public static void main(String[] args) throws FileNotFoundException {
		System.out.println("295 == " + solvePart1("test_input.txt"));
		System.out.println(solvePart1("input.txt"));
		System.out.println("-I don't like reading the file twice, but I don't want to intersperse p1 and p2 code-");
		System.out.println("1068781 == " + solvePart2("test_input.txt"));
		System.out.println("75018 == " + solvePart2("test_input_2.txt"));
		System.out.println("779210 == " + solvePart2("test_input_3.txt"));
		System.out.println("1261476 == " + solvePart2("test_input_4.txt"));
		System.out.println("1202161486 == " + solvePart2("test_input_5.txt"));
		System.out.println(solvePart2("input.txt"));
	}

	private static int solvePart1(String input) throws FileNotFoundException {
		ArrayList<Integer> numbers = new ArrayList<Integer>();
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
		// Part 1
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

	private static BigInteger solvePart2(String input) throws FileNotFoundException {
		Scanner sc = new Scanner(new File(input));
		sc.nextInt();
		// Chinese remainder theorem
		ArrayList<Integer> numbers = new ArrayList<Integer>();
		ArrayList<Integer> remainder = new ArrayList<Integer>();
		int offset = 0;
		for (String s : sc.next().split(",")) {
			if (s.equals("x")) {
				offset++;
			} else {
				int n = Integer.parseInt(s);
				numbers.add(n);
				remainder.add((n - offset) % n);
				offset++;
			}
		}
		sc.close();
		BigInteger[] n = new BigInteger[numbers.size()];
		BigInteger[] a = new BigInteger[remainder.size()];
		for (int i = 0; i < numbers.size(); i++) {
			n[i] = BigInteger.valueOf(numbers.get(i));
			a[i] = BigInteger.valueOf(remainder.get(i));
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
